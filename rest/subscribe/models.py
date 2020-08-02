from django.db import models
from django.utils.translation import ugettext_lazy as _


class Subscribe(models.Model):
    firstName = models.CharField(
        _("First Name"), max_length=225, blank=True, null=True, )
    lastName = models.CharField(
        _("Last Name"), max_length=225, blank=True, null=True, )
    email = models.EmailField(
        _("Email Subscribe"), max_length=255, blank=True, null=True, unique=True
    )

    accepted = models.BooleanField(
        _("Accept Policy"), default=False)

    class Meta:
        ordering = ()

    def __str__(self):
        return self.email
