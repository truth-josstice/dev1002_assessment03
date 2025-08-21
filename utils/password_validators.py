import re
from marshmallow import ValidationError

def validate_password_complexity(password):
    password_requirement = "Password be at least 8 letter and contain at least: one uppercase letter, one number and one special character."
    
    if len(password) < 8:
        raise ValidationError(password_requirement)
    
    if not re.search(r'[A-Z]', password):
        raise ValidationError(password_requirement)
    
    if not re.search(r'[0-9]', password):
        raise ValidationError(password_requirement)
    
    if not re.search(r'[!@#$%^&*()":{}|<>]', password):
        raise ValidationError(password_requirement)

def validate_password_for_schema(password):
    validate_password_complexity(password)
    return True