from django.conf.urls import url, include

from . import views
from currency.views import CurrencyConverter


urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^currency/$',CurrencyConverter.as_view())

]