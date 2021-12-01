from django.urls import path, include
from rest_framework import routers
from cadastro.views import CadastroViewSet
from conta.views import ContaViewSet
from django.contrib import admin

router = routers.DefaultRouter()
router.register("cadastro", viewset=CadastroViewSet)
router.register("conta", viewset=ContaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
