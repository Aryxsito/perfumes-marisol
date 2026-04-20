from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("perfume/<int:pk>/", views.perfume_detail, name="perfume_detail"),
    path("perfume/nuevo/", views.perfume_create, name="perfume_create"),
    path("perfume/<int:pk>/editar/", views.perfume_update, name="perfume_update"),
    path("perfume/<int:pk>/eliminar/", views.perfume_delete, name="perfume_delete"),
    path("perfume/<int:pk>/stock/", views.update_stock, name="update_stock"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
