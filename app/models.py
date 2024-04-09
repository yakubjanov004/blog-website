from django.db import models

# Create your models here.

class Profile(models.Model):
 full_name = models.CharField(max_length=50, verbose_name="To'liq ism")
 bio = models.TextField()
 image = models.ImageField(upload_to='profile')
 link = models.URLField()

 def __str__(self):
  return f"{self.id}-{self.full_name}"
 

class Service(models.Model):
 name = models.CharField(max_length=50)
 icon = models.CharField(max_length=50)
 order = models.IntegerField()
 description = models.TextField()

 def __str__(self):
  return f"{self.id}-{self.name}"

class Blog(models.Model):
  title = models.CharField(max_length=50)
  published_at = models.DateField(auto_now=True)
  poster = models.ImageField(upload_to='blog')
  author = models.CharField(max_length=50)
  description = models.TextField()
  view_count = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.id}-{self.title}"

class Skill(models.Model):
 name = models.CharField(max_length=50)
 percentage = models.IntegerField(default=0)
 order = models.IntegerField(default=0)

 def __str__(self):
  return f"{self.id}-{self.name}"

class Category(models.Model):
 name = models.CharField(max_length=50)

 def __str__(self):
  return f"{self.id}-{self.name}"

class About(models.Model):
 body = models.TextField()
 amount = models.FloatField()
 project_count = models.IntegerField()
 customer_count = models.IntegerField()

 def __str__(self):
  return f"{self.id}-{self.body}"

class Project(models.Model):
 name = models.CharField(max_length=50)
 category_id = models.ForeignKey(Category, on_delete=models.PROTECT)
 poster = models.ImageField()
 link = models.URLField()
 description = models.TextField()
 completed_at = models.DateField(null=True)

 def __str__(self):
  return f"{self.id}-{self.name}"
