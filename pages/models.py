from django.db import models


x=[('aviliability','aviliability'),('rental','rental'),('sold','sold')]
class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class books(models.Model):
    title=models.CharField(max_length=50)
    authorname=models.CharField(max_length=50)
   # image=models.ImageField(upload_to='photos/%y/%m/%d',default='photos/20/10/29/photo1.png')
    number_of_pages=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.CharField(max_length=50,choices=x)
    book_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title