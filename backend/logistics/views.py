import datetime
import json
from django.http import HttpResponse, JsonResponse
from .models import Order, Waypoint
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return HttpResponse("Hello, world")


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


    queryset = orders.values("pk", "customer_name", "order_date")
    data = list(queryset)

    for e in data:
        e["waypoints"] = []
        for w in Waypoint.objects.filter(order=e["pk"]).all():
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

        order = Order(order_number=int(body["order_number"]), customer_name=body["customer"], order_date=datetime.datetime.now().date())
        order.save()

        return JsonResponse({"response: 200"}, safe=False)
    else: 
        return JsonResponse({}, safe=False)

@csrf_exempt
def create_waypoint(request, order_id):
    if request.method == "POST":
        # create waypoint
        return JsonResponse({}, safe=False)
    else: 
        return JsonResponse({}, safe=False)
