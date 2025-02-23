from django.urls import path
from .views import start_page, single_gadget_view, single_gadget_slug_view, single_gadget_post_view

urlpatterns = [
    path('', start_page),
    path('gadget/<int:gadget_id>', single_gadget_view), # <int:gadget_id> ist ein Parameter, der an die Funktion single_gadget_view übergeben wird
    path('gadget/<slug:gadget_slug>', single_gadget_slug_view, name="gadget_slug_url"),
    path('gadget/send_gadget', single_gadget_post_view),
]