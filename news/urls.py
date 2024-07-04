from django.urls import path

from . import views

app_name = "news"

urlpatterns = [
    path("api/news", views.NewsItemApiView.as_view(), name="index"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("suggestion/", views.SuggestionFormView.as_view(), name="suggestion"),
    path('success/', views.SuggestionSuccessView.as_view(), name='success'),
]
