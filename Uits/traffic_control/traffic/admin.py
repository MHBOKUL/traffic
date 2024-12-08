from django.contrib import admin
from .models import LicenceOwner, Fine, Expiry

admin.site.register(LicenceOwner)
admin.site.register(Fine)
admin.site.register(Expiry)

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')