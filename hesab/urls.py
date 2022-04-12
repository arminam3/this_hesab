from django.urls import path
from . import views
urlpatterns=[
    path('weeklist/', views.WeekList.as_view(), name='week_list'),
    # path('<int:pk>/weekdetails/', views.WeekDetails.as_view(), name='week_details'),
    path('<int:pk>/refresh/', views.refresh, name='refresh'),
]