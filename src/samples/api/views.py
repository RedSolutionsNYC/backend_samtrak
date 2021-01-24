from rest_framework.generics import ListAPIView, RetrieveAPIView
from samples.models import Sample
from .serializers import SampleSerializer

class SampleListView(ListAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer

class SampleDetailView(RetrieveAPIView):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer