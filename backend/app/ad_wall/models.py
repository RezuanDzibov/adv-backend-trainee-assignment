from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    primary_image_url = models.URLField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"

    def __str__(self) -> str:
        return f"{self.name} ${self.price}"


class Image(models.Model):
    headline = models.CharField(max_length=200)
    url = models.URLField()
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="images")

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self) -> str:
        return f"{self.headline} {self.ad.name}"
