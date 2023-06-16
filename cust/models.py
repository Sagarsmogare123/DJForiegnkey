from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, null=False)
    mobile = models.CharField(max_length=100, null=True)
    email = models.EmailField()
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    tagname = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.tagname


class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
    )
    pname = models.CharField(max_length=256, null=False)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=48, choices=CATEGORY)
    image = models.ImageField(upload_to="product", blank=True)
    created_at = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.pname


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out_For_Delivery', 'Out_For_Delivery'),
        ('Delivered', 'Delivered'),
    )
    created_at = models.DateField(auto_now_add=True, null=True)
    customer = models.ForeignKey('Customer', null=True, on_delete=models.CASCADE)
    product = models.ManyToManyField('Product', null=True)
    tag = models.ManyToManyField('Tag', null=True)
    Status = models.CharField(max_length=200, null=True, choices=STATUS)

# Create your models here.
