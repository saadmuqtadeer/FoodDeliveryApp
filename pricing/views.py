from django.shortcuts import render
from django.http import JsonResponse
from .models import Organization, Pricing, Item

def index(request):
    if request.method == "POST":
        zone = request.POST.get('zone')
        organization_id = request.POST.get('organization')
        total_distance = request.POST.get('total_distance')
        item_type = request.POST.get('item_type')
        total_price = calculate_delivery_cost(zone, organization_id, total_distance, item_type)
        return JsonResponse({'total_price': total_price})
        
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def get_organizations(request):
    organizations = Organization.objects.all().values('id', 'name')
    return JsonResponse(list(organizations), safe=False)


def get_item_types(request):
    item_types = Item.objects.values_list('type', flat=True).distinct()
    return JsonResponse(list(item_types), safe=False)

def calculate_delivery_cost(zone, organization_id, total_distance, item_type):
    try:
        item = Item.objects.get(type=item_type)
        print(f"Item: {item}")
        pricing = Pricing.objects.get(organization_id=organization_id, item=item)
        
        print(f"Pricing for {item} in {zone} zone by {organization_id}:")
        print(f"Base Distance: {pricing.base_distance_in_km}")
        print(f"Km Price: {pricing.km_price}")
        print(f"Fix Price: {pricing.fix_price}")
        
        base_distance = pricing.base_distance_in_km
        km_price = pricing.km_price
        fix_price = pricing.fix_price
        
        total_distance = int(total_distance)
        if total_distance <= base_distance:
            total_price = fix_price
        else:
            additional_distance = total_distance - base_distance
            total_price = fix_price + (additional_distance * km_price)

        return total_price
    except Pricing.DoesNotExist:
        return "Pricing details not found"
    except Item.DoesNotExist:
        return f"Item matching query does not exist for type: {item_type}"
    except Exception as e:
        return f"An error occurred: {str(e)}"
    
def pricing_structure(request):
    pricings = Pricing.objects.all()
    return render(request, 'pricing_structure.html', {'pricings': pricings})
