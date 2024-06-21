from django.db import models

# Create your models here.


class GamesList(models.Model):
    name = models.CharField(max_length=30)
    alias = models.CharField(max_length=30)
    icon = models.CharField(max_length=60)
    _domain = models.CharField(max_length=30, null=True, blank=True)
    _url = models.CharField(max_length=60, null=True, blank=True)
    max_size = models.IntegerField(null=True, blank=True)

    @property
    def url(self):
        """If domain in database -> redirect to queue, else redirect to url in database"""

        if self._domain:
            return f"/queue/{self.alias}"
        return self._url


