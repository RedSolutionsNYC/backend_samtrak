from django.urls import path
from .views import SampleListView, SampleDetailView

urlpatterns = [
    path('', SampleListView.as_view()),
    path('<pk>', SampleDetailView.as_view())
]