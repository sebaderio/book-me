from django.contrib import auth
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from authentication import value_objects

User = auth.get_user_model()


@receiver(post_save, sender=User)
def set_permissions(  # type:ignore # pylint: disable=unused-argument
    sender, instance, created, *args, **kwargs
):
    '''Add user of type BARBER to Barber group when created.

    Doesn't work in Django Admin because form will override model groups with
    groups that were chosen in the form.
    https://stackoverflow.com/questions/56365788/django-adding-user-to-groups-in-a-signal
    '''
    if created and instance.account_type == value_objects.AccountType.BARBER.name:
        group = Group.objects.get(name='Barber')
        instance.groups.add(group)
