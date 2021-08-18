import graphene
from flask_graphql_auth import AuthInfoField

from .fields import ResponseMessageField, AccountResults, PostResults


AccountUnion = type("AccountUnion", (graphene.Union,), {
    "Meta": type("Meta", (), {
        "types": (AccountResults, ResponseMessageField, AuthInfoField)
    })
})


PostUnion = type('PostUnion', (graphene.Union, ), {
    "Meta": type("Meta", (), {
        "types": (PostResults, ResponseMessageField, AuthInfoField)
    })
})


class MutationUnion:
    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)


ResponseUnion = type("ResponseUnion", (MutationUnion, graphene.Union), {
    "Meta": type("Meta", (), {
        "types": (ResponseMessageField, AuthInfoField)
    })
})

AuthUnion = ResponseUnion
RefreshUnion = ResponseUnion
