from django.shortcuts import render
from .csv_handler import CSV_Interface
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import math
inventory=CSV_Interface("/Users/franciscoavila/Desktop/assessment-3/ecom_pro/ecom_app/data/inventory.csv")
cart=CSV_Interface("/Users/franciscoavila/Desktop/assessment-3/ecom_pro/ecom_app/data/mycart.csv")
links=['Games', 'Consoles', 'Chairs']
# Create your views here.
def home(request):
    data={
        "navlinks":links
    }
    return render(request, 'pages/home.html', data)


def displayItems(request, category):
    allInventory=inventory.get_data()
    # print(allInventory)
    inventoryDis=[]
    for i in allInventory:
        if i["category"]== category.lower():
            inventoryDis.append(i)
    category=category.upper()
    data={
        "navlinks":links,
        "inventory": inventoryDis,
        "category":category
    }
    return render(request, 'pages/inventory.html', data)

@csrf_exempt
def add_to_cart(request, id):
    try:
        all_inventory=inventory.get_data()
        for item in cart.get_data():
            if int(item['id'])==id:
                original_price=math.floor(float(item["price"])/int(item['quantity']))
                new_quantity=int(item["quantity"])+1
                item["quantity"]=new_quantity
                item["price"]=original_price*new_quantity
                cart.write_all_rows_to_file(cart.all_data)
                return JsonResponse({"success":"item quantity changed"})
        for i in all_inventory:
            if int(i['id']) == id:
                i["quantity"]=1
                cart.append_one_row_to_file(i)
                return JsonResponse({"success":"item added to cart"})
        return JsonResponse({"success":False})
    except Exception as e:
        print(e)
        return JsonResponse(
            {
                'success': False,
                'failure': e
            })
    
def myCart(request):
    total=0
    for i in cart.get_data():
        total += math.floor(float(i['price']))
    data={
        "cart":cart.get_data(),
        'total':total,
        "navlinks":links
    }
    return render(request, 'pages/cart.html', data)