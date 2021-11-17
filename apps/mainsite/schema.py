import graphene

import badgeuser.schema
import directaward.schema
import institution.schema
import issuer.schema
import lti_edu.schema
import lti13.schema


class Query(institution.schema.Query,
            badgeuser.schema.Query,
            issuer.schema.Query,
            lti13.schema.Query,
            lti_edu.schema.Query,
            directaward.schema.Query,
            graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
