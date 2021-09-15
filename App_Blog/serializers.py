from django.db.models import fields
from rest_framework import serializers
from App_Blog.models import Blog


class BlogSerializers(serializers.ModelSerializer):

  class Meta:
    model = Blog
    fields = "__all__"