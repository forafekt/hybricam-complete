from __future__ import unicode_literals
from django.forms import fields, forms
from .models import Subscribe


class SubscribeForm(forms.Form):
    model = Subscribe
    use_required_attribute = False

    email = fields.EmailField(
        label='E-Mail',
        required=True,
        help_text='Please enter a valid email address')

    created_at = fields.DateTimeField()
    updated_at = fields.DateTimeField()