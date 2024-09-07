from django.urls import path
from .views import BlogsListView, BlogDetailView

urlpatterns = [
    path('', BlogsListView.as_view(), name='home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name="blog_detail")
]
