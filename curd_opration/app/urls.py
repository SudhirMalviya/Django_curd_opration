from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logindata/',views.logindata,name='logindata'),
    path('singup/',views.singup,name='signup'),
    path('product/',views.product,name='product'),
    path('about/',views.about),
    path('award/',views.award),
    path('contact/',views.contact),
    path('savedata/',views.savedata,name='savedata'),
    path('Query/<str:email>/', views.query_view, name='query_view'),
    path('delete_view/<int:pk>/', views.delete_view, name='delete_view'),
    path('edit_query/<int:pk>/',views.edit_query,name="edit_query"),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
