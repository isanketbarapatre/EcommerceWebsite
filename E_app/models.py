from django.db import models

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=20)
    isActive = models.BooleanField(default=False)

    class Meta:
        db_table = 'master'
    
    def __str__(self):
        return str(self.Email)


gender_choices = (
    ('m', 'male'),
    ('f', 'female'),
    ('o', 'other'),
)

class Profile(models.Model):
    Master  = models.ForeignKey(Master, on_delete=models.CASCADE)
    Fullname = models.CharField(max_length=50, default = "")
    Gender = models.CharField(max_length=10, choices = gender_choices)
    Mobile = models.CharField(max_length=10)
    State = models.CharField(max_length=30)
    City = models.CharField(max_length=30)
    Address = models.TextField()
    
    class Meta:
        db_table = 'profile'


category_choices = (
    ('M', 'Mobile'),
    ('L', 'Laptops'),
    ('Hp', 'Headphones'),
    ('Kb', 'Keyboards'),
    ('Mo', 'Mouse'),
)


class Product(models.Model):
    ProductName = models.CharField(max_length=30)
    Category = models.CharField(max_length=4, choices = category_choices)
    Brand = models.CharField(max_length=20)
    Description = models.TextField()
    Date = models.DateField(auto_now_add=True)
    Price= models.IntegerField()
    Image = models.FileField(upload_to = "images/")

    class Meta:
        db_table = 'product'

    def __str__(self):
        return str(self.ProductName)
        


class OrderItem(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Ordered= models.BooleanField(default=False)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    
    class Meta:
        db_table = 'orderitem'



state_choices = (
    ('Accepted', 'Accepted'),
    ('Packed','Packed'),
    ('On the Way', 'On the Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel')
)

class OrderPlaced(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateField(auto_now_add=True)  
    items = models.ManyToManyField(OrderItem)
    Status= models.CharField(max_length=50, choices = state_choices, default = 'Pending')
    

