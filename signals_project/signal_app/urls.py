from django.urls import path
from . import views

urlpatterns = [
    path('q1/', views.q1_view),
path('q2/', views.q2_view),
path('q3/', views.q3_view),

]
