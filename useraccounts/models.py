from django.db import models
# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=100,default='')
    first_name = models.CharField(max_length=100,default='')
    last_name = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=500,default='')
    password2 = models.CharField(max_length=500,default='')
    address = models.CharField(max_length=100,default='')
    phone1 = models.CharField(max_length=100,default='')
    phone2 = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    def register(self):
        self.save()


    @staticmethod
    def get_user_by_username(username):
        try:
            return UserProfile.objects.get(username=username)
        except:
            return False

