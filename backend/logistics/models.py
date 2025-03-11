from django.db import models



class Order(models.Model):
    order_number = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200)
    order_date = models.DateTimeField("date published")

    def __str__(self):
        title = "Order #%s: %s" % (self.order_number, self.customer_name)
        return title

class Waypoint(models.Model):
    class Waypoint_types(models.TextChoices):
        PICKUP = "P", "Pickup"
        DELIVERY = "D", "Delivery"



    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    waypoint_type = models.CharField(max_length=1, choices=Waypoint_types.choices)

    def __str__(self):
        return str(self.order) + " - " + self.address