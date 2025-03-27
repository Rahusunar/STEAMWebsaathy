# user/validators.py
from django.contrib.auth.password_validation import (
    CommonPasswordValidator as BaseCommonPasswordValidator,
    NumericPasswordValidator as BaseNumericPasswordValidator
)
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomMinimumLengthValidator:
    def __init__(self, min_length=6):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("Your password must contain at least %(min_length)d characters."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _("Your password must contain at least %(min_length)d characters.") % {'min_length': self.min_length}

class CustomCommonPasswordValidator(BaseCommonPasswordValidator):
    def validate(self, password, user=None):
        # Use the method from the parent class to check for common passwords
        super().validate(password, user)
        # If it fails, you can raise a custom message here if needed

class CustomNumericPasswordValidator(BaseNumericPasswordValidator):
    def validate(self, password, user=None):
        super().validate(password, user)  # This will raise a ValidationError if the password is numeric
