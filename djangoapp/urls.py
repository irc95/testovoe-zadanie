from django.urls import path
from .views import main


urlpatterns = [
    path('home/', main, {'name': 'Home'}, name='home'),
    path('company/', main, {'name': 'About company'}, name='company'),
    path('development/', main, {'name': 'Development'}, name='development'),
    path('development/cpp', main, {'name': 'Development C++'}, name='development_cpp'),
    path('development/cpp/qt', main, {'name': 'Development C++/Qt'}, name='development_cpp_qt'),
    path('development/python', main, {'name': 'Development Python'}, name='development_python'),
    path('development/python/django', main, {'name': 'Development Python/Django'}, name='development_python_django'),
    path('development/python/tornado', main, {'name': 'Development Python/Tornado'}, name='development_python_tornado'),
    path('prices/', main, {'name': 'Prices'}, name='prices'),
]