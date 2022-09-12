from django.urls import path
from .views import homePageView,samplePageView

urlpatterns = [
    path('', homePageView.as_view(), name="home"),
    path('sample/', samplePageView.as_view(), name="sample"),
]