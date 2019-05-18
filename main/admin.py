from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField


MySpecialAdmin = lambda model: type('SubClass'+model.__name__, (admin.ModelAdmin,), {
    'list_display': [x.name for x in model._meta.fields],
    'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField,))]
})

from .models import CenterModel, CenterDistanceModel, ProductModel, LoadModel, LoadDistanceModel, OrderModel

admin.site.register(CenterModel,  MySpecialAdmin(CenterModel))
admin.site.register(CenterDistanceModel, MySpecialAdmin(CenterDistanceModel))
admin.site.register(ProductModel, MySpecialAdmin(ProductModel))
admin.site.register(LoadModel,  MySpecialAdmin(LoadModel))
admin.site.register(LoadDistanceModel, MySpecialAdmin(LoadDistanceModel))
admin.site.register(OrderModel, MySpecialAdmin(OrderModel))