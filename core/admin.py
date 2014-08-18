from django.contrib import admin

from tips.core.models import Tag
from tips.core.models import Tip
from tips.core.models import Vote

admin.site.register(Tag)
admin.site.register(Tip)
admin.site.register(Vote)

