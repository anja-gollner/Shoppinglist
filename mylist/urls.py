from django.urls import path
from .views import start_page, single_gadget_int_view, GadgetView, RedirectToGadgetView

urlpatterns = [
    path('start/', start_page),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view), # <int:gadget_id> ist ein Parameter, der an die Funktion single_gadget_view übergeben wird
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),
   
]