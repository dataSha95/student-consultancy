from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
