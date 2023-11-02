from django.urls import path
from.views import max, top_sellers,advertisement_post,tovar_details

urlpatterns = [
    path('', max, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advertisement_post , name='adv-post'),
    path('advertisement/<int:pk>',tovar_details,name='tov-detail'),
]