from django.db import models
from django.contrib.auth.models import User




class Profile(models.Model):
  name = models.CharField(max_length = 250)
  profile_photo = models.ImageField(upload_to = "images/")
  bio = models.TextField()

  def save_profile(self):
    self.save()
  
  def delete(self):
    Profile.objects.get(id = self.id).delete()
  
  def update(self,field,val):
    Profile.objects.get(id=self.id).update(field=val)
    

  def __str__(self):
    return self.bio

class Share(models.Model):
  myid = models.PositiveIntegerField(null= True)
  story = models.TextField()

  def save_share(self):
    self.save()
  
  def delete(self):
    Share.objects.get(id = self.id).delete()

  def update(self,fields,val):
    Share.objects.get(id=self.id).update(field=val)

  def __int__(self):
    return self.annonid

class Comments(models.Model):
    comm = models.CharField(max_length = 100, blank = True)
    share = models.ForeignKey(Share,on_delete=models.deletion.CASCADE)
    user = models.ForeignKey(User,on_delete=models.deletion.CASCADE)
    

def save_comment(self):
    self.save()

def delete_comment(self):
    Comments.objects.get(id = self.id).delete()
    
def update_comment(self,new_comment):
    comm = Comments.objects.get(id = self.id)
    comm.comment = new_comment
    comm.save()
