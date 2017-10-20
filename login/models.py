from django.db import models

# Create your models here.

class User(models.Model):
	user_id = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	confirm_password = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	is_active = models.BooleanField('Active?', default=True)

	def __unicode__(self):
		return self.user_id

	def get_absolute_url(self):
		return reverse('register_edit', kwargs={'pk': self.pk})