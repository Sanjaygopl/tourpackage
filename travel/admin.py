from django.contrib import admin
from .models import Explores
from .models import Venreg
from .models import Venlog
from .models import Usereg
from .models import Uselog
# Register your models here.
class ExploreAdmin(admin.ModelAdmin):
    list_display = ('title','destination','image','duration','price','expiry','approved')
admin.site.register(Explores,ExploreAdmin)
class VenregAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')
admin.site.register(Venreg,VenregAdmin)
class VenlogAdmin(admin.ModelAdmin):
    list_display = ('username','password')
admin.site.register(Venlog,VenlogAdmin)
class UseregAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')
admin.site.register(Usereg,UseregAdmin)
class UserlogAdmin(admin.ModelAdmin):
    list_display = ('username','password')
admin.site.register(Uselog,UserlogAdmin)


