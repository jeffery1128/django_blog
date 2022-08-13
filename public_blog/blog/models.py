from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=5000)
    create_date = models.DateTimeField(timezone.now())
    publish_date = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


class comment(models.Model):
    post = models.ForeignKey('blog.post',on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    create_date = models.DateTimeField(timezone.now())
    approved = models.BooleanField(default = False)

    def approve_comment(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text

