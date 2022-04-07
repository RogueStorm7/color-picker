from django.urls import path

from paintapp.views import PaintView

urlpatterns = [
    # paintapp/
    path('', PaintView.as_view(), name='paint'),
]