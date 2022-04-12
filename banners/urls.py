from django.urls import path

from . import views

app_name="banners"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.BannerDetailView.as_view(), name='detail'),
]
