from django.urls import path
from rest_framework.generics import ListAPIView
from .views import(
    PizzeriaListAPIView,
    PizzeriaRetrieveAPIView,

)

urlpatterns = [
    path('', PizzeriaListAPIView.as_view(), name="pizzeria_list"),
    path('<int:id>/', PizzeriaRetrieveAPIView.as_view(), name="pizzeria_detail"),

]
