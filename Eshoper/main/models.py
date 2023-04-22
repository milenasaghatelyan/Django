from django.db import models

# Create your models here.
class Contact(models.Model):
    phone= models.CharField('phone number:',max_length=455)
    email=models.EmailField('email ',max_length=442)

    def __str__(self) -> str:
        return 'contact'
    

    class Meta:
        verbose_name='contact'
        verbose_name_plural='contacts'

class SocialMedia(models.Model):
    facebook=models.CharField('facebook ',max_length=455)
    twitter=models.CharField('twitter ',max_length=455)
    linkedin=models.CharField('linkedin ',max_length=455)
    google_plus=models.CharField('google_plus ',max_length=455)
  

    def __str__(self) -> str:
        return 'Social Media'
    

    class Meta:
        verbose_name='social media account'
        verbose_name_plural='socila media accounts'

class GeneralSliderActive(models.Model):
    name=models.CharField('shop name :',max_length=332)
    title=models.CharField('product title',max_length=444)
    txt=models.TextField('product info ')
    img=models.ImageField('product image:',upload_to='media')
    sale=models.ImageField('product sale:',upload_to='media',null=True)

    def __str__(self) -> str:
        return 'generalslideractive'
    

    class Meta:
        verbose_name='generalslideractive'
        verbose_name_plural='generalslideractive'


class GeneralSlider(models.Model):
    name=models.CharField('shop name :',max_length=332)
    title=models.CharField('product title',max_length=444)
    txt=models.TextField('product info ')
    img=models.ImageField('product image:',upload_to='media')
    sale=models.ImageField('product sale:',upload_to='media',null=True)

    def __str__(self) -> str:
        return 'generalslider'
    

    class Meta:
        verbose_name='generalslider'
        verbose_name_plural='generalslider'


class Features_Items(models.Model):
    money=models.CharField('money',max_length=44)
    name=models.CharField('product name',max_length=44)
    img=models.ImageField('image',upload_to='media')
 
    def __str__(self) -> str:
        return 'features_items'
    

    class Meta:
        verbose_name='features_items'
        verbose_name_plural='features_items'
