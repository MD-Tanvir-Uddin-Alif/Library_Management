from django.urls import path
from .views import detailiView, borrow_view, return_view

urlpatterns = [
    path('book_details/<int:id>/',detailiView.as_view(),name="Details_page"),
    path('borrow/<int:id>/',borrow_view,name="Borrow_page"),
    path('return/<int:id>/',return_view,name="Return_page")
]