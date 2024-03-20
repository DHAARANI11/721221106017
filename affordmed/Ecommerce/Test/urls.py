from django.urls import path
from .views import CompanyView,ProductListView,Get

urlpatterns=[
    path('get/',GetView.as_view()),
    path('company/',CompanyView.as_view()),
    path('product/',ProductListView.as_view()),

]