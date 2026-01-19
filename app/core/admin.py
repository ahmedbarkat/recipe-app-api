from django.contrib import admin
from core import models as core_model
# Register your models here.
admin.site.register(core_model.User)
admin.site.register(core_model.Reciepe)

