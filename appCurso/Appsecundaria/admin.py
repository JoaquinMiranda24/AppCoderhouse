from django.contrib import admin
from .models import *

# Register your models here.
#carga los modelos al admin, por eso en admin podemos ver avatar

admin.site.register(Avatar)

