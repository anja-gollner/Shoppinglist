from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
import json
from django.utils.text import slugify #slugify wandelt einen String in einen Slug um, also leerzeichen werden durch - ersetzt
from django.urls import reverse

from .dummy_data import gadgets

# Create your views here.

def start_page(request):
    return HttpResponse('Hello, Django!')

def single_gadget_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]['name'])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound('Gadget not found')


def single_gadget_slug_view(request, gadget_slug):
    gadget_match = None

    for gadget in gadgets:
         if slugify(gadget["name"]) == gadget_slug:
              gadget_match = gadget
    
    if gadget_match:
         return JsonResponse(gadget_match)
    raise Http404()
   # return HttpResponse(json.dumps(gadgets[0]), content_type='application/json')

def single_gadget_post_view(request):
    if request.method == 'POST':
       try:
           data = json.loads(request.body)
           print(f"Received data: {data}")
           return JsonResponse({"status": "Data received"})
       except:
           return JsonResponse({"status": "Invalid data"})