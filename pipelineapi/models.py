import uuid

from django.db import models


class Techie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image_url = models.URLField(max_length=200)
    title = models.CharField(max_length=50)
    linkedIn_url = models.URLField(max_length=200)
    github_url = models.URLField(max_length=200)
    portfolio_url = models.URLField(max_length=200)
    resume_url = models.URLField(max_length=200)
    job_type = models.CharField(max_length=50)
    experience_level = models.CharField(max_length=50)
