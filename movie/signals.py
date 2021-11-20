from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from .models import Movie
from django.core.mail import send_mail


@receiver(post_delete, sender=Movie)
def notify_admins(**kwargs):
    instance = kwargs.get('instance')
    print("The deleted movie is {}".format(instance))

#
# @receiver(post_save, sender=Movie)
# def my_handler(sender, instance, created, *args, **kwargs):
#     send_mail(
#         subject='New Movie Created Subject',
#         message='Dear User {} has been created '.format(instance.name),
#         from_email='notifiersys@mail.com',
#         recipient_list=['minasamy65@gmail.com', 'khalil.gazairly@gmail.com', 'elsayedali3632@gmail.com'],
#         fail_silently=False
#     )
