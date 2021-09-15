from django.urls import path
from App_Blog import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit-blogs/<pk>', views.UpdateBlog.as_view(), name='edit_blog'),
    path('delete-blogs/<pk>', views.DeleteBlog.as_view(), name='delete_blog'),
    path('apiblogs', views.BlogListAPI.as_view(), name='blog_api')
]
