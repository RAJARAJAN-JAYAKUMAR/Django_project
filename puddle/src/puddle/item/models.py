from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    # Define the meta options for the model
    class Meta:
        
        # Specify the default ordering for queries
        ordering = ('name',) #whenever you create an object this cmd will arrange the object alphabetically
        verbose_name_plural = 'Categories' # this changes the name of the category to categories in the admin page

    def __str__(self) -> str:
        return self.name #it replaces object naming 'category' to 'name of the object' in the admin page

class Item(models.Model):
    '''
    foreign key relationship with the Category model
    on_delete=models.CASCADE will delete the associated instance created using the foreign key 
    ipo category modelah ethachum nu delete panna atha use panni create panna items ellam delete airum model.cascade kudutha
    '''
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True,null=True)  #install - pip install pillow 
    is_sold = models.BooleanField(default=False)
    
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name