from django.db import models

# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / cars_photos/<filename>
    return '{0}/{1}'.format("cars_photos",filename)


class cars_data(models.Model):
    car_Id = models.AutoField(primary_key=True)
    car_Name = models.CharField(max_length=100, blank=False, null=False )
    Car_Model = models.CharField(max_length=100, blank=False, null=False)
    car_Price = models.IntegerField(max_length=15, blank=False, null=False)
    car_Photo = models.FileField(upload_to=user_directory_path, null=True, verbose_name="")

    class Meta:
        db_table = 'cars' 
