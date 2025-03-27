from django.contrib import admin
from .models import CodingClassEnrollment,exploreKits,Category,Product
# Register your models here.
admin.site.register(CodingClassEnrollment)
admin.site.register(exploreKits)
admin.site.register(Category)
admin.site.register(Product)