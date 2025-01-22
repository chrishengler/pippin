from django.core.exceptions import ValidationError

def no_spaces(value):
    if ' ' in value:
        raise ValidationError('The ID field cannot contain spaces.')
