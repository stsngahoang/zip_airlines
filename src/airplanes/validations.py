from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_passengers(value):
    if value <= 0:
        raise ValidationError(
            _("passengers should be greater than 0"),
            params={"value": value},
        )
