from django.contrib import admin
from .models import Post, Product, NewTable


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "pub_date")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("sku", "name", "price", "size", "qty")


class NewTableAdmin(admin.ModelAdmin):
    list_display = (
        "bigin_f",
        "bool_f",
        "data_f",
        "char_f",
        "decimal_f",
        "float_f",
        "int_f",
        "text_f",
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(NewTable, NewTableAdmin)
