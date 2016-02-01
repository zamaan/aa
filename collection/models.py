from django.contrib.auth.models import User
from django.db import models


class Timestamp(models.Model):
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True


class Thing(Timestamp):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price=models.IntegerField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, blank=True, null=True)

    def __unicode__(self):
    	return self.name

    def get_absolute_url(self):
    	return "/things/%s/" %self.slug

class Social(models.Model):
	SOCIAL_TYPES=(('twitter','Twitter'),('facebook','Facebook'),('pinterest','Pinterest'),('instagram','Instagram'),)
	network=models.CharField(max_length=255, choices=SOCIAL_TYPES)
	username=models.CharField(max_length=255)
	thing=models.ForeignKey(Thing, related_name="social_accounts")

	class Meta:
		verbose_name_plural="Social media links"

class Timestamp(models.Model):
	created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	class Meta:
		abstract=True

def get_image_path(instance,filename):
	return '/'.join(['thing_images', instance.thing.slug,filename])

class Upload(models.Model):
	thing=models.ForeignKey(Thing,related_name="uploads")
	image=models.ImageField(upload_to=get_image_path)
