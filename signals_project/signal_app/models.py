from django.db import models, connection

# Create your models here.
from django.db.models.signals import post_save
import time
import threading
signal_log = []

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default="Test author")
    price = models.FloatField(default=0.0)

def signal_q1(sender, instance, **kwargs):
    signal_log.append("Signal started, delay 3sec")
    time.sleep(3)
    signal_log.append("Signal finished")


def signal_q2(sender, instance, **kwargs):
    signal_log.append(f"Signal thread id: {threading.get_ident()}")

def signal_q3(sender, instance, **kwargs):
    signal_log.append(f"Signal in_atomic: {connection.in_atomic_block}")
