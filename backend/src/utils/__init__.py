import re
from typing import Dict, Any

def validate_email(email: str) -> bool:
    """
    Validate email format using regex.

    Args:
        email (str): Email address to validate

    Returns:
        bool: True if email format is valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_password_strength(password: str) -> Dict[str, Any]:
    """
    Validate password strength.

    Args:
        password (str): Password to validate

    Returns:
        Dict[str, Any]: Validation result with 'valid' boolean and 'errors' list
    """
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter")

    if not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter")

    if not re.search(r'\d', password):
        errors.append("Password must contain at least one digit")

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }

def sanitize_input(text: str) -> str:
    """
    Sanitize user input by removing potentially harmful characters.

    Args:
        text (str): Input text to sanitize

    Returns:
        str: Sanitized text
    """
    # Remove potentially harmful characters/sequences
    sanitized = text.replace('<script', '&lt;script').replace('javascript:', 'javascript&#58;')
    return sanitized.strip()

def format_api_response(success: bool, data: Any = None, message: str = "") -> Dict[str, Any]:
    """
    Format a standardized API response.

    Args:
        success (bool): Whether the operation was successful
        data (Any): Optional data to return
        message (str): Optional message to return

    Returns:
        Dict[str, Any]: Formatted API response
    """
    return {
        "success": success,
        "data": data,
        "message": message
    }