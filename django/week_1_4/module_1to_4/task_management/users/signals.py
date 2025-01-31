from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail

@receiver(post_save,sender=User)
def send_activation_email(sender,instance,created,**kwarg):
  if created:
    token = default_token_generator.make_token(instance)
    activation_url = f"{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}"
    subject = 'Activate Your Account'
    message = f'Hi {instance.username},\n\nPlease activate your account by clicking the link below:\n{activation_url}\n\nThank You!'
    recipient_list = [instance.email]
    try:
      send_mail(subject, message,settings.EMAIL_HOST_USER,recipient_list)
    except Exception as e:
      print (f"Failed to send email to {instance.email}: {str(e)}")