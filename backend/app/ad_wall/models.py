from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    primary_image_url = models.URLField()

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"


class Image(models.Model):
    url = models.URLField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
