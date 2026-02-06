from secrets import token_urlsafe

PREFIX_BOT_TOKEN = "bot_"

def generate_token() -> str:
    """Generate API Token for bot"""
    return token_urlsafe(32)