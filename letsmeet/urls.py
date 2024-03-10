from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='linkup-list'),   #domain.com/meetups
    path('<slug:linkup_slug>/success', views.confirm_event_signup, name='confirm-event-signup'),
    path('<slug:linkup_slug>', views.linkup_details, name='linkup-details')
]