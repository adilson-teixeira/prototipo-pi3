from django.urls import path

from .views import TreeDetailView, TreeListView

app_name = "trees"

urlpatterns = [
    path("", TreeListView.as_view(), name="list"),
    path("<slug:slug>/", TreeDetailView.as_view(), name="detail"),
    path("square/<slug:slug>/", TreeListView.as_view(), name="list_by_square"),
]



