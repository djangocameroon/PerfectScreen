from django.db import models


class SocialPost(models.Model):
    username = models.CharField(max_length=200)
    platform = models.CharField(max_length=50)
    screenshot = models.ImageField(upload_to='screenshots/')
    post_url = models.URLField()
    has_tagged_digitalocean = models.BooleanField(default=False)
    has_starred_repo = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username} - {self.platform}"
