from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, View, TemplateView, DeleteView
from rest_framework import serializers
from App_Blog.models import Blog
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from App_Blog.serializers import BlogSerializers
# Create your views here.

class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = "App_Blog/my_blogs.html"


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image',)
    template_name = 'App_Blog/create_blog.html'

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        blog_obj.slug = blog_obj.blog_title.replace(
            " ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'


@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)


    dict = {
        'blog': blog,
    }
    return render(request, 'App_Blog/blog_details.html', context=dict)




class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image',)
    template_name = 'App_Blog/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:blog_details', kwargs={'slug': self.object.slug})

class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'App_Blog/delete_blog.html'


    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:my_blogs', kwargs={})


class BlogListAPI(APIView):
  def get(self, request):
    BlogAPI = Blog.objects.all()
    serializers = BlogSerializers(BlogAPI, many=True)

    return Response(serializers.data)

  def post(self):
    pass

