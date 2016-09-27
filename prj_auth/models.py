from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):

    class Meta:
        verbose_name = 'мой пользователь'
        verbose_name_plural = 'мои пользователи'
