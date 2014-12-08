from django.contrib import admin
from counter.models import Counter

# Register your models here.
class CounterAdmin(admin.ModelAdmin):
    list_display = ("ip",)
    exlude = ("ip",)
    readonly_fields = ("ip",)

admin.site.register(Counter, CounterAdmin)