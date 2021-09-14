import threading

from django.db import IntegrityError, transaction
from rest_framework import serializers

from directaward.models import DirectAward, DirectAwardBundle
from issuer.serializers import BadgeClassSlugRelatedField
from mainsite.exceptions import BadgrValidationError


class DirectAwardSerializer(serializers.Serializer):
    class Meta:
        model = DirectAward

    badgeclass = BadgeClassSlugRelatedField(slug_field='entity_id', required=False)
    eppn = serializers.CharField(required=False)
    recipient_email = serializers.EmailField(required=False)
    status = serializers.CharField(required=False)
    evidence_url = serializers.URLField(required=False, allow_blank=True, allow_null=True)
    narrative = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    description = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def update(self, instance, validated_data):
        [setattr(instance, attr, validated_data.get(attr)) for attr in validated_data]
        instance.save()
        return instance


class DirectAwardBundleSerializer(serializers.Serializer):
    class Meta:
        DirectAwardBundle

    badgeclass = BadgeClassSlugRelatedField(slug_field='entity_id', required=False)
    direct_awards = DirectAwardSerializer(many=True, write_only=True)
    entity_id = serializers.CharField(read_only=True)
    batch_mode = serializers.BooleanField(write_only=True)
    notify_recipients = serializers.BooleanField(write_only=True)

    def create(self, validated_data):
        badgeclass = validated_data['badgeclass']
        batch_mode = validated_data.pop('batch_mode')
        notify_recipients = validated_data.pop('notify_recipients')
        direct_awards = validated_data.pop('direct_awards')
        user_permissions = badgeclass.get_permissions(validated_data['created_by'])
        if user_permissions['may_award']:
            successfull_direct_awards = []
            with transaction.atomic():
                direct_award_bundle = DirectAwardBundle.objects.create(initial_total=direct_awards.__len__(),
                                                                       **validated_data)
                for direct_award in direct_awards:
                    direct_award['eppn'] = direct_award['eppn'].lower()
                    try:
                        da_created = DirectAward.objects.create(bundle=direct_award_bundle, badgeclass=badgeclass,
                                                                **direct_award)
                        successfull_direct_awards.append(da_created)
                    except IntegrityError:
                        pass
            if notify_recipients:
                def send_mail(awards):
                    for da in awards:
                        da.notify_recipient()

                thread = threading.Thread(target=send_mail, args=(successfull_direct_awards,))
                thread.start()
            if batch_mode:
                direct_award_bundle.notify_awarder()
            direct_award_bundle.badgeclass.remove_cached_data(['cached_direct_awards'])
            direct_award_bundle.badgeclass.remove_cached_data(['cached_direct_award_bundles'])

            return direct_award_bundle
        raise BadgrValidationError("You don't have the necessary permissions", 100)
