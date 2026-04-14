from django.db import models


class Enquiry(models.Model):
    BATCH_CHOICES = [
        ("morning", "Morning (8-12 yrs, 10am-12pm)"),
        ("afternoon", "Afternoon (12+ yrs, 3pm-5pm)"),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    child_age = models.PositiveIntegerField()
    batch = models.CharField(max_length=20, choices=BATCH_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.batch}"
