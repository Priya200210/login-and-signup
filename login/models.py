from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE)
    email_adress = models.CharField(max_length=200)


    def __str__(self):
        return self.username

# class Products(models.Model):
#     brand = models.CharField(max_length= 200)
#     product = models.CharField(max_length= 200)
#     name =  models.CharField(max_length= 200)
#     price = models.IntegerField()
   
#     def __str__(self):
#         return self.username
    
class Pages(models.Model):
    articles_name = models.CharField(max_length=400)
    artticles_site = models.CharField(max_length=400)
    price = models.IntegerField(default= 0)


    def __str__(self):
        return self.articles_name
    

# class Student_detials(models.Model):
#     student_name = models.CharField(max_length=200)
#     student_id = models.IntegerField()
#     branch = models.CharField(max_length=100)


#     def __str__(self):
#         return self.student_name
    
class Student(models.Model):
    name = models.CharField(max_length=200)
    student_id = models.IntegerField()
    department = models.CharField(max_length= 200)


    def __str__(self):
        return self.name
    
class Market(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	market_type = models.CharField(max_length=255, null=True, blank=True)
	zipcode = models.CharField(max_length=10, default='00000')

	# location = gis_models.PointField() 
	# images = ArrayField(models.CharField(max_length=1200), blank=True, default=list)

	def __str__(self):
		return self.name
class BedroomData(models.Model):
		BEDROOM_CHOICES = [
        (1, 'One Bedroom'),
        (2, 'Two Bedroom'),
        (3, 'Three Bedroom'),
        (4, 'Four Bedroom'),
        (5, 'Five Bedroom'),
        (6, 'Six Bedroom'),
    ]
		market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='bedroom_data')
		bedroom_count = models.IntegerField(choices=BEDROOM_CHOICES)
		average_price = models.FloatField(null=True, blank=True)
		average_rent = models.FloatField(null=True, blank=True)
		average_rent_yield = models.FloatField(null=True, blank=True)
		median_price = models.FloatField(null=True, blank=True)
		median_rent = models.FloatField(null=True, blank=True)  # Changed to DateField as per your example
		median_rent_yield = models.FloatField(null=True, blank=True)
		listing = models.IntegerField(null=True, blank=True)

		class Meta:
			unique_together = ('market', 'bedroom_count')

		def __str__(self):
			return f"{self.market.name} - {self.get_bedroom_count_display()}"
		

