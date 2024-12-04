from django.db import models

# from resume_core.general.models import CreatedModified


class Dashboard(models.Model):
    title = models.CharField(max_length=200)
    graph_type = models.TextField()

    def __str__(self):
        return self.title
