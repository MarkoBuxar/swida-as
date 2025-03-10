from django.db import models

WAYPOINT_TYPE_CHOICES = {
    "P": "Pickup",
    "D": "Delivery"
}


class Order(models.Model):
    order_number = models.IntegerField()
    customer_name = models.CharField(max_length=200)
    order_date = models.DateTimeField("date published")

    def __str__(self):
        title = "Order #%s: %s" % (self.order_number, self.customer_name)
        return title

class Waypoint(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    waypoint_type = models.CharField(max_length=1, choices=WAYPOINT_TYPE_CHOICES)

    def __str__(self):
        return str(self.order) + " - " + self.address