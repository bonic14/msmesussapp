from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.welcome, name='home'),
    path('product/',views.Product, name='product'),
    path('ussdapp/',views.ussdapp, name='ussdapp'),
    path('registration/',views.registration,name='register'),
    path('<int:id>deleteInfos/',views.delreg,name='deleteInfos'),
    path('<int:id>updateInfos/',views.updatereg,name='updateInfos'),
    path('reg/endpoints/',views.registerEndpoint,name='endpoints'),
    path('deleteEndpoint/<int:id>/',views.deleteEndpoint,name='deleteEndpoint')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 