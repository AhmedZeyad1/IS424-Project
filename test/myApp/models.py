from django.db import models 

class User(models.Model):
    user_name=models.CharField(max_length=50 ,blank=True)
    user_email=models.CharField(max_length=20 , blank=True)
    user_phoneNumber=models.IntegerField(blank=True , unique=True, default=0)
    user_password = models.CharField(max_length=100 , blank=True)
    def __str__(self):
        return f"user name :{self.user_name}  user email : {self.user_email} user phone number {self.user_phoneNumber}  user_password={self.user_password}"

class Author(models.Model):
    autName = models.CharField(max_length=50, default="", blank=True)

    def __str__(self):
        return self.autName if self.autName else "Unknown Author"

class book(models.Model):
    title = models.CharField(max_length=100, default="", blank=True)
    publicationDate = models.CharField(max_length=20, default="", blank=True)
    ISBN = models.CharField(max_length=13, default="", blank=True,unique=True)
    bookGenre = models.CharField(max_length=30, default="", blank=True)
    author = models.ManyToManyField(User, blank=True, related_name = 'book')
    

    def __str__(self):
        return f"{self.title} - ISBN: {self.ISBN} - Genre: {self.bookGenre} - Author: {self.author}"

# Make many-to-many, between aut&book..



