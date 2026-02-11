from iam.authentication.token_auth import TokenAuthentication

def create_token_jwt(data: dict) -> str:
    return TokenAuthentication.create_token_jwt(data)