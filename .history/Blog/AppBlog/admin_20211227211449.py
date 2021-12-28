from django.contrib import admin

# Register your models here.
from .models import *

from .models import Post 

admin.site.register(Post)



admin.site.register(Blog)
admin.site.register(Blogger)