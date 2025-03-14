from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('package/',views.package,name="package"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('register/',views.register,name="register"),
    path('vendorlog/',views.vendorlog,name="vendorlog"),
    path('userlog/',views.userlog,name="userlog"),
    path('vendorreg/',views.vendorreg,name="vendorreg"),
    path('userreg/',views.userreg,name="userreg"),
    path('successreg/',views.successreg,name="successreg"),
    path('vendordash/',views.vendordash,name="vendordash"),
    path('create/',views.create,name="create"),
    path('userdash/',views.userdash,name="userdash"),
    path('payment/',views.payment,name="payment"),
    path('book/',views.book,name="book"),
    path('book1/',views.book1,name="book1"),
    path('book2/',views.book2,name="book2"),
    path('book3/',views.book3,name="book3"),
    path('book4/',views.book4,name="book4"),
    path('book5/',views.book5,name="book5"),
    path('book6/',views.book6,name="book6"),
    path('book7/',views.book7,name="book7"),
    path('book8/',views.book8,name="book8"),
    path('book9/',views.book9,name="book9"),
    path('delete_item/<int:id>/',views.delete_item, name='delete_item'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('logout/', views.user_logout, name='logout')

    
]
