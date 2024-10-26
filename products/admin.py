from django.contrib.admin import ModelAdmin, register, StackedInline, display
from .models import Category, Product, ProductImage, Color, Order, OrderItem


class ProductImageStackedInline(StackedInline):
    model = ProductImage
    fields = 'image', 'product'


class ColorStackedInline(StackedInline):
    model = Color
    fields = 'name', 'product'


@register(Product)
class ProductModelAdmin(ModelAdmin):
    inlines = ProductImageStackedInline, ColorStackedInline
    list_display = 'name', 'category', 'price', 'quantity', 'bazada_qolgan'
    list_editable = 'price', 'category', 'quantity'
    list_filter = 'category', 'price'
    list_per_page = 1

    @display(ordering='quantity')
    def bazada_qolgan(self, product):
        if product.quantity < 10:
            return 'Kam'
        return 'Kop'



@register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass

@register(Order)
class OrderModelAdmin(ModelAdmin):
    pass

@register(OrderItem)
class OrderItemModelAdmin(ModelAdmin):
    pass