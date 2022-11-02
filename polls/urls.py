app_name = 'polls'
from django.urls import path
from . import views

### Generic view(class-based view)
urlpatterns=[
    # ex: /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results.
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:ok>/vote/', views.vote, name='vote')
]