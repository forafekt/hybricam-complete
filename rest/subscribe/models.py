from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Subscribe(models.Model):
    email = models.EmailField(
        _("Email Subscribe"), max_length=255, blank=True, null=True, unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.email

    