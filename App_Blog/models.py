from django.db import models
from django.contrib.auth.models import User
from App_Blog.utils import generate_unique_slug
from django.utils.text import slugify

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=264, verbose_name="Put a Title")
    slug = models.SlugField(max_length=264, unique=True)
    blog_content = models.TextField(verbose_name="What is on your mind?")
    blog_image = models.ImageField(
        upload_to='blog_images', verbose_name="Image")
    publish_date = models.DateTimeField(auto_now_add=True)
    update_view = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publish_date',)

    def save(self, *args, **kwargs):
        if self.slug:  # edit
            if slugify(self.blog_title) != self.slug:
                self.slug = generate_unique_slug(Blog, self.blog_title)
        else:  # create
            self.slug = generate_unique_slug(Blog, self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.blog_title

