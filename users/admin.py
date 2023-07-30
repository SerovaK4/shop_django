from django.contrib import admin

from catalog.models import Product

# Register your models here.


class ABCAdmin(admin.ModelAdmin):
    fields = ['description', 'category', 'is_published', ]

    def get_fields(self, request, obj=None):
        if request.user.groups.filter(name="Модератор"):
            return ['description', 'category', 'is_published', ]
        elif request.user.is_superuser:
            return [i.name for i in Product._meta.fields if i.name != "id"]
        else:
            return []





admin.site.unregister(Product)
admin.site.register(Product, ABCAdmin)