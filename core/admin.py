from django.contrib import admin
from .models import Product,Client
# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')

class ClientAdmin(admin.ModelAdmin):
    list_display=('name','email')

from .models import Product,Client
admin.site.register(Product,ProdutoAdmin)
admin.site.register(Client,ClientAdmin)