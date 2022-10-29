from django.contrib import admin

from core import models

# Register your models here.


class UserSchemaAdmin(admin.ModelAdmin):

    readonly_fields = [
        "id",
        "created_at",
    ]


admin.site.register(models.UserSchema, UserSchemaAdmin)
