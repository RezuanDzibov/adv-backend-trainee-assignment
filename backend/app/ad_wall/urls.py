from django.urls import path

from ad_wall import views

urlpatterns = [
    path("", views.AdListView.as_view()),
    path("<int:pk>/", views.AdRetrieveView.as_view())
]
