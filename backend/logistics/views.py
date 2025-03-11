import datetime
import json
from django.http import HttpResponse, JsonResponse
from .models import Order, Waypoint
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse("Hello, world")

@csrf_exempt
def get_orders(request):
    params = request.GET
    customer = params.get("customer")
    date_start = params.get("date_start")
    date_end = params.get("date_end")
    orders = Order.objects.all()

    if customer:
        orders = orders.filter(customer_name__iexact=customer)
    if date_start:
        orders = orders.filter(order_date__gte=date_start)
    if date_end:
        orders = orders.filter(order_date__lte=date_end)


    queryset = orders.values("order_number", "customer_name", "order_date")
    data = list(queryset)

    for e in data:
        e["waypoints"] = []
        for w in Waypoint.objects.filter(order=e["order_number"]).all():
            wp_obj = {
                'address': w.address, 
                'waypoint_type': w.get_waypoint_type_display()
                }
            e["waypoints"].append(wp_obj)

    return JsonResponse(data, safe=False)
   

@csrf_exempt
def create_order(request):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        print(body)

        order = Order(customer_name=body["customer"], order_date=datetime.datetime.now().date())
        order.save()

        return JsonResponse({}, safe=False)
    else: 
        return JsonResponse({}, safe=False)

@csrf_exempt
def create_waypoint(request, order_number):
    if request.method == "POST":
        body = json.loads(request.body.decode('utf-8'))
        order = Order.objects.filter(order_number=order_number).get()
        # pickup by default / if invalid entry
        wp_type = Waypoint.Waypoint_types.DELIVERY if (body["waypoint_type"].lower() == "d" or body["waypoint_type"].lower() == "delivery") else Waypoint.Waypoint_types.PICKUP

        waypoint = Waypoint(order=order, address=body["address"], waypoint_type=wp_type)
        waypoint.save()

        return JsonResponse({}, safe=False)
    else: 
        return JsonResponse({}, safe=False)
