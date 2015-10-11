from .base import BaseTransformer

class AccountTransformer(BaseTransformer):

    def transform(self, account):
        return {
            "id"      : account.id,
            "username": account.username,
            "email"   : account.email,
            "role"    : account.role
        }
