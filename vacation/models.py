from django.db import models
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from accounts.models import Account


class Vacation(models.Model):
    STATUS = (
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DENIED', 'Denied'),
    )
    TYPE_OF_VACATION = (

        ('ANNUAL_LEAVE', 'Annual Leave'),
        ('SICK_LEAVE', 'Sick Leave'),
        ('PAID_VACATION', 'Paid Vacation'),
        ('OTHER', 'Other'),
    )
    owner = models.ForeignKey(Account, verbose_name='Employe', on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')
    type_vacation = models.CharField(max_length=20, choices=TYPE_OF_VACATION, default='Other')
    date_vacation = models.DateTimeField(verbose_name='vacation date', auto_now_add=True)
    start_date = models.DateTimeField(verbose_name='start vacation')
    end_date = models.DateTimeField(verbose_name='end vacation')
    comments = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        # return  str(self.owner.id)
        return self.owner.username + " vacation status: " + self.status

    class Meta:
        ordering = ['-date_vacation']
