from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
TYPE_CHOICES = (
    ('film', 'Film'),
    ('book', 'Book'),
    ('general', 'General'),
)

class Post(models.Model):
    title = models.CharField(max_length = 200, unique=True)
    slug = models.SlugField(max_length = 200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='general')
    # other fields and methods

class Meta:
    ordering = ['-created_on']

class PageViews(models.Model):
    count = models.IntegerField(default=0)
    
def __str__(self):
    return self.title
