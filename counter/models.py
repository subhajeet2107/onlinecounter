from django.db import models

# Create your models here.
class Counter(models.Model):
    ip = models.IPAddressField(verbose_name="IP Address", db_column="visitor_ip")
    visited_time = models.TimeField(verbose_name="Visited Time", db_column="visitor_time", auto_now_add=True)

    class Meta:
        db_table = "online_counter"
        verbose_name_plural = "Online Counter"
