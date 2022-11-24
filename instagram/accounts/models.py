from django.contrib.auth.models import AbstractUser
from django.db import models



class Profile(AbstractUser):
    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар'
    )
    birthday = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения'
    )
    liked_posts = models.ManyToManyField(verbose_name='Понравившиеся публикации', to='posts.Post', related_name='user_likes')
    subscriptions = models.ManyToManyField(verbose_name='Подписки', to='accounts.Profile', related_name='subscribers')
    commented_posts = models.ManyToManyField(verbose_name='Прокомментированные публикации', to='posts.Post', related_name='user_comments')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
