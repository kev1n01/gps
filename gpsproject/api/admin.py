from django.contrib import admin
from .models import Driver, Bus, Student, StopPoint, TravelRegister, TravelRegisterDetail, User

# Register your models here.
admin.site.register(Bus)
admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Student)
admin.site.register(StopPoint)
admin.site.register(TravelRegister)
admin.site.register(TravelRegisterDetail)