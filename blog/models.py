from django.db import models
from django.urls import reverse
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='resume/images/',default=True)

    date = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={
                'blog_id':self.id
        })
