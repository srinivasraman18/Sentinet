from django.db import models

# Create your models here.



class Business(models.Model):
	business_name = models.CharField(max_length = 30)


class Category(models.Model):
	business = models.ForeignKey(Business,on_delete = models.CASCADE)
	category_name = models.CharField(max_length = 30)

class Sentiment(models.Model):
	business = models.ForeignKey(Business, on_delete = models.CASCADE)
	positive = models.IntegerField(default=0)
	negative = models.IntegerField(default=0)

class Emotion(models.Model):
	business = models.ForeignKey(Business, on_delete = models.CASCADE)
	happy = models.IntegerField(default=0)
	sad = models.IntegerField(default=0)
	angry = models.IntegerField(default=0)
	surprise = models.IntegerField(default=0)
	love = models.IntegerField(default=0)
	joy = models.IntegerField(default=0)

class Offense(models.Model):
	business = models.ForeignKey(Business,on_delete =models.CASCADE,default=1)
	offensive = models.IntegerField()
	non_offensive = models.IntegerField()

class CategoryData(models.Model):
	category_id = models.ForeignKey(Category, on_delete = models.CASCADE)
	positive = models.IntegerField()
	negative = models.IntegerField()
	happy = models.IntegerField()
	sad = models.IntegerField()
	angry = models.IntegerField()
	surprise = models.IntegerField()
	love = models.IntegerField()
	joy = models.IntegerField()
	offensive = models.IntegerField()
	non_offensive = models.IntegerField()


class Region(models.Model):
	business_id = models.ForeignKey(Business, on_delete = models.CASCADE)
	reg_id = models.IntegerField()
	sentiment = models.CharField(max_length = 10)
	emotion = models.CharField(max_length = 10)




