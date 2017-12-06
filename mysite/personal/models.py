# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length = 140)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length =50)
    file = models.FileField(null=True, blank=True)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse("personal:detail", kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title) #slugify the title in url
    if new_slug is not None:       #new slug is not none
        slug = new_slug
    qs = Post.objects.filter(slug = slug).order_by("-id") #check if slug title exists
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id) #if exists, then brand new instance again
        return create_slug(instance, new_slug = new_slug)
    return slug

def pre_save_post_receiver(sender,instance,*args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Post)
    	