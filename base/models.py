from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import random

#profile model for users
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
    slug=models.SlugField( blank=True, null=True)
    verif=models.BooleanField(default=False)

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
        ('Request for API','Request for API'),
    )
    summary=models.CharField(max_length=25, choices=topic_choice)
    topic=models.TextField(max_length=200)
    created=models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name='Contacts'
        verbose_name_plural='Contacts'

    def __str__(self):
        return self.summary



#not migrated for now
class Blog(models.Model):
    pass


class Projects(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    avatar_name=models.CharField(max_length=20, default='main stack: Django', help_text='what was your main stack', null=True, blank=True)
    project_name=models.CharField(max_length=25, default='my project name', help_text='your project name', null=True, blank=True)
    project_link=models.CharField(max_length=200, null=True,)
    project_description=models.TextField(max_length=100, default='summary about your project', help_text='pitch the main part of your project', null=True, blank=True)
    project_date=models.DateTimeField(auto_now_add=True, null=True, blank=True)


    class Meta:
        verbose_name='Projects'
        verbose_name_plural='Projects'
        ordering=['-project_date']

    def __str__(self):
        return self.project_name








