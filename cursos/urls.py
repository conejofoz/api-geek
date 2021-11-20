from django.urls import path

from .views import AvaliacaoAPIView, CursoAPIView, CursoSerializer, AvaliacaoSerializer

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacaoAPIView.as_view(), name='avaliacoes'),
]
