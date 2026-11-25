from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from CategoryApp.models import CategoryModel
# Create your models here.
class ProductModel(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,blank=True)
    content=models.TextField()
    productImage=models.ImageField(upload_to="productImage",null=True,blank=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,related_name="productCategories")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00
    )
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value)
        super().save(*args, **kwargs)
        

    def get_absolute_url(self):
        return reverse("productDetails", kwargs={"slug": self.slug})
    