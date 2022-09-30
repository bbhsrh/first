from django.forms import inlineformset_factory
from .models import *

PhotoInlineFormSet = inlineformset_factory(Region2,
                                           Photo,
                                           fields=['image', 'title', 'price', 'description'],
                                           extra = 2)