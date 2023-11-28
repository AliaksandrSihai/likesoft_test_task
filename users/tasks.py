from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task()
def welcome_message(email):
    """ Приветственное сообщение """
    send_mail(
        subject='Добро пожаловать!',
        message='Поздравляем с успешной регистрацией на нашей платформе',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
    return
