from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    labels = {
        'name': 'Name',
        'verbose_name': 'Verbose name'
    }

    class Meta:
        verbose_name = 'Menu category'
        verbose_name_plural = 'Menu categories'

    name = models.CharField(labels['name'], max_length=255, blank=True, null=False)
    verbose_name = models.CharField(labels['verbose_name'], max_length=255, blank=True, null=False)

    def __str__(self):
        return self.verbose_name


class Menu(models.Model):
    labels = {
        'name': 'Name',
        'category': 'Category',
        'path': 'Link',
        'parent': 'Parent item'
    }

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'
    
    name = models.CharField(labels['name'], max_length=255, blank=True, null=False)
    category = models.ForeignKey(MenuCategory,verbose_name=labels['category'], on_delete=models.CASCADE, blank=False, null=False)
    path = models.CharField(labels['path'], max_length=1000, blank=True, null=False)
    parent = models.ForeignKey('self', verbose_name=labels['parent'], on_delete=models.SET_DEFAULT, null=True, blank=True,default=0)
    
    def __str__(self):
        return self.name