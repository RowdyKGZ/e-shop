from django.contrib import admin

from .models import Category, ProductImage, Product, Comment


class ImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3
    fields = ('image',)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('title', 'uuid', 'price')
    list_display_links = ('uuid', 'title')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)
