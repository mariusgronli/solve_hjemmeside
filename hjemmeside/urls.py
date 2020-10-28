from django.urls import path
from hjemmeside.views import HomepageView

app_name = 'hjemmeside'

urlpatterns = [
    path('',HomepageView.as_view(),name='homepage')
]
