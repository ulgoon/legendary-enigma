from ...model import AccountModel
from ..fields import AccountField, ResponseMessageField, AccountResults

from flask_graphql_auth import query_jwt_required


@query_jwt_required
def resolve_account(root, info, **kwargs):
    id = kwargs.get('id', None)
    username = kwargs.get('username', None)

    accounts = AccountModel.objects(id=id, username=username)

    if accounts.first() is None:
        return ResponseMessageField(is_success=False, message="Not found")

    return AccountResults(accounts=[AccountField(id=account.id,
                                                 username=account.username,
                                                 register_on=account.register_on)
                                    for account in accounts])
