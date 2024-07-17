from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(null=True)
    content2 = models.CharField(max_length=200,null=True)
    pub_date =models.DateTimeField(auto_now_add=True)   

    Author = models.ForeignKey(Author,on_delete=models.CASCADE) 

    def __str__(self):
        return self.title