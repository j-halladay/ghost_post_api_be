from django.db import models


class Message(models.Model):
    title = models.CharField(max_length=40)
    is_boast = models.BooleanField()
    like = models.IntegerField()
    text = models.CharField(max_length=280)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
# class Manufacturer(models.Model):
#     name = models.CharField(max_length=50)
#     website = models.URLField(max_length=250)

#     def __str__(self):
#         return self.name


# class ShoeType(models.Model):
#     style = models.CharField(max_length=50)

#     def __str__(self):
#         return self.style


# class ShoeColor(models.Model):
#     color_name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.color_name


# class Shoe(models.Model):
#     brand_name = models.CharField(max_length=50)
#     manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
#     color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
#     material = models.CharField(max_length=20)
#     shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
#     fasten_type = models.CharField(max_length=20)

#     def __str__(self):
#         return self.brand_name
