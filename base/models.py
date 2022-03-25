from pyexpat import model
from random import choice, choices
from xml.dom.minidom import CharacterData
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.utils.text import slugify


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=10)
    bio=models.CharField(max_length=20)
    avatar=models.FileField(null=True, blank=True, upload_to='images/')
    instagram=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    telegram=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(unique=True, blank=True, null=True)
    

    def save(self, *args, **kwargs):
        self.slug =slugify(self.slug)
        super(Profile, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    
    #for creating userprofile for every registered user after registtration
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    class Meta:
        verbose_name='Profile'
        verbose_name_plural='Profile'        


class ProfileLink(models.Model):
    user=models.ForeignKey(Profile, default=1, on_delete=models.CASCADE, db_constraint=False, related_name='linkowner')
    link_name=models.CharField(max_length=12, null=True, )
    link=models.CharField(max_length=200, null=True, )

    def __str__(self):
        return self.link_name

    class Meta:
        verbose_name='Profile Link'
        verbose_name_plural='Profile Link'


class Contact(models.Model):
    name=models.CharField(max_length=20)
    surname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    topic_choice=(
        ('Registration','Registration'),
        ('Profile Avatar','Profile Avatar'),
        ('Profile Settings','Profile Settings'),
        ('Another','Another'),
    )
    summary=models.CharField(max_length=25, choices=topic_choice)
    topic=models.TextField(max_length=200)
    created=models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name='Contacts'
        verbose_name_plural='Contacts'

    def __str__(self):
        return self.summary

