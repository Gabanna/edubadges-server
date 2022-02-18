# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [6.0.0] - 2022-02-21
- Changed subject of earned emails and several minor other email tekst.
- Added issuing on behalf of issuer groups.
- Added LTI functionality.
 
## [5.4.0] - 2022-01-17
- Bump Django from 2.2.24 to 2.2.26
- Bump pillow from 8.3.2 to 9.0.0

## [5.3.0] - 2021-12-20
- Minor changes to the information in the mail temlates.
- Added remark to make your edubadges public in the confirmation mail.
- First logout to prevent missing authCode.
- Badgeclass with not revoked assertions is limited updateable.
- Upgraded openbadges.
- Upgrade pypng.
- Added support for signed JWT's in the baked image.
- Do not return archived issuers.

## [5.2.0] - 2021-11-15
- New submodule commits.
- Bugfix for non-unique deny reason enrolllment.
- Check provisionments.
- Added deny_reason to enrollment.
- Proxy call to validator git info.
- Added backpack user count to insights.
- Use connect domain for SURF default.
- Maintain whitelisted url's from Django admin view.
- Imported badges unique for users.
- Fix for multiple whitelisted domains.
- Force build.
- Added public_institution to hide institutions from catalog.

## [5.1.0] - 2021-10-18
- Validate imported badge.
- Added import external open badge functionality.
- New endpoint to delete users by institution admins.
- Do not convert SVG to images for watermark.
- Use the new endpoint in eduID for EPPN's.
- Upgraded graphene django as incompatible with OTP django-object dependency.
- Added 2FA to admin site.
- Allow impersonation by super users.
- Award non-formal edubadge with no validated name.
- Include archived status in catalog.
- If there are validated names, use them.
- Bugfix case-sensitive EPPN rel 5.0.1.
- Added collection functionality to backpack.
- Added evidence information to direct_awards.
- Either Dutch or English attribute is required.
- Added offline exporting JS.
- Bugfix for AnonymousUser does not have is_student.
- Do not fetch accepted enrolments.
- Use database counts for the insights module.
- Updated dependency Pillow.

## [5.0.0] - 2021-08-30
- Added feedback option.
- Overview of all open requested edubadges. 
- Bugfic: multiple emails from same provider are allowed.
- Use cron for scheduling.
- Delete expired direct_awards.
- Clear cache after denied enrollment.
- Migration for formal non-MBO StudyLoad extensions.
- New extension TimeInvestment.
- Show denied enrollments.
- Bugfix for multiple invites.
- Send emails async for direct awards.
- Non-formal badges can be awarded to users with validated name.

## [4.2.0] - 2021-07-19
- Updated dependency Django

## [4.1.0] - 2021-06-21
- Added an option to the badgeclass to make Narrative and Evicence mandatory.
- Expose new badgeclass attributes in graphql.
- Always retrieve EPPN and Schac homes.
- Updated dependencies Django and Pillow.

## [4.0.0] - 2021-05-31
- Better error message if there are no terms.
- UID has changed.
- Added safe checks to str method.
- Badgeclass drives allowed institution.
- Added allowed institutions to badgeclass.
- Allow awarding and approval of badges of other institutions.
- Revoked assertions do not account for in edit permission.
- Added award other institutions columns.
- Allowed inistitutions to award badges to.
- Added a new demo environment setting to test and experience the edubadges platform.
- Fix the transparancy of composite images in watermark badgeclass image.


## [3.1.0] - 2021-05-03
- Added multi-language support for images
- Added badgeclass counter in catalog
- Updated Django, Pillow
- Issuer must be part of a faculty
- Added direct_awarding_enabled to institution
- Added direct_award graphene endpoints
- Fixed provisionment email institution admin not sent
- Added fetching EPPN from eduID
- Added endpoints for revoking assertions and direct awards in bulk
- Multi langual Name change is allowed if the name is empty
- Added is_demo field to badgr_app
- Name is not required in evidence
- Fixed issues with special characters in names

## [3.0.0] - 2021-03-15
- Added multilanguage fields for Institution, Issuer Group & Issuer
- Added public endpoints for catalog

## [2.1.3] - 2021-03-01
- Bugfix eduID
- Added usage reporting.

## [2.1.2] - 2021-02-15
- Adds archiving option to Issuer Group
- Adds swagger api documentation
- Adds evidence and narrative to assertion data

## [2.1.1] - 2021-01-18
 - Added bilangual email (NL/EN).
 - Adds archiving option to Badgeclass and Issuer

## [2.1.0] - 2020-12-28
 - Added endpoints for public institution page.
 - Added English and Dutch language options for description fields.
 - Added option to indicate if an institution supports formal, non-formal or both badgeclasses.
 - Extended logging.
 - Better handling of duplicate issuer names.
 - Added institution name to endpoints.
 - Updated cryptography from 2.3 to 3.2.
 - Several bug fixes.
