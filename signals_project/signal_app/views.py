from django.http import HttpResponse
from .models import Book, signal_log, signal_q1, signal_q2, signal_q3
from django.db.models.signals import post_save
from django.db import transaction
import threading


def q1_view(request):
    signal_log.clear()

    post_save.disconnect(receiver=signal_q2, sender=Book)
    post_save.disconnect(receiver=signal_q3, sender=Book)
    post_save.connect(signal_q1, sender=Book)

    signal_log.append("View started")
    book = Book()
    book.title = "Test book"
    book.author = "Test author"
    book.price = 120.5
    book.save()
    signal_log.append("View finished")
    signal_log.append("Django signals are executed synchronously by default, because The view waited for the signal to complete before reaching View finished")
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Consolas, monospace;
                background-color: #f4f4f4;
                padding: 30px;
            }}
            .log-box {{
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 8px rgba(0,0,0,0.1);
            }}
            .log-line {{
                margin-bottom: 10px;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <div class="log-box">
            {"".join(f'<div class="log-line">{line}</div>' for line in signal_log)}
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def q2_view(request):
    signal_log.clear()

    post_save.disconnect(receiver=signal_q1, sender=Book)
    post_save.disconnect(receiver=signal_q3, sender=Book)
    post_save.connect(signal_q2, sender=Book)

    signal_log.append(f"View thread id: {threading.get_ident()}")
    book = Book()
    book.title = "Test book"
    book.author = "Test author"
    book.price = 120.5
    book.save()
    signal_log.append("Both thread id's are exactly the same.This proves that Django signals run in the same thread as the caller.")

    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Consolas, monospace;
                background-color: #f4f4f4;
                padding: 30px;
            }}
            .log-box {{
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 8px rgba(0,0,0,0.1);
            }}
            .log-line {{
                margin-bottom: 10px;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <div class="log-box">
            {"".join(f'<div class="log-line">{line}</div>' for line in signal_log)}
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

def q3_view(request):
    signal_log.clear()

    post_save.disconnect(receiver=signal_q1, sender=Book)
    post_save.disconnect(receiver=signal_q2, sender=Book)
    post_save.connect(signal_q3, sender=Book)

    with transaction.atomic():
        book = Book()
        book.title = "Test book"
        book.author = "Test author"
        book.price = 120.5
        book.save()
        signal_log.append("Using connection.in_atomic_block, we proved that Django signals run inside the same DB transaction as the caller")
    html = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Consolas, monospace;
                background-color: #f4f4f4;
                padding: 30px;
            }}
            .log-box {{
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 8px rgba(0,0,0,0.1);
            }}
            .log-line {{
                margin-bottom: 10px;
                color: #333;
            }}
        </style>
    </head>
    <body>
        <div class="log-box">
            {"".join(f'<div class="log-line">{line}</div>' for line in signal_log)}
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)





