from django.db import models

# Create your models here.
class Blogger(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    website = models.URLField()
    company = models.CharField(max_length=100)
    about = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Blogger: {self.name} email: {self.email} phone: {self.phone} address: {self.address} city: {self.city} state: {self.state} zip: {self.zip} website: {self.website} company: {self.company} about: {self.about} created_at: {self.created_at} updated_at: {self.updated_at}"
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 
    
