from django.urls import path
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
        
        path('api/login/', obtain_auth_token, name = 'api_login'),
        path('api/register/', views.RegisterAndLoginAPIView.as_view(), name = 'api_register'),
        path('api/', views.APIRootView.as_view(), name='api-root'),
        path('api/continents/', views.ContinentList.as_view(), name = 'continent_list'),
        path('api/locations/', views.LocationList.as_view(), name = 'location_list'),
        path('api/races/', views.RaceList.as_view(), name = 'race_list'),
        path('api/guilds/', views.GuildList.as_view(), name = 'guild_list'),
        path('api/kingdoms/', views.KingdomList.as_view(), name = 'kingdom_list'),
        path('api/epicentres/', views.EpicentreList.as_view(), name = 'epicentre_list'),
        path('api/items/', views.ItemList.as_view(), name = 'item_list'),

        path('api/continents/<int:pk>/', views.ContinentDetail.as_view(), name='continent_detail'),
        path('api/locations/<int:pk>/', views.LocationDetail.as_view(), name='location_detail'),
        path('api/races/<int:pk>/', views.RaceDetail.as_view(), name='race_detail'),
        path('api/guilds/<int:pk>/', views.GuildDetail.as_view(), name='guild_detail'),
        path('api/kingdoms/<int:pk>/', views.KingdomDetail.as_view(), name='kingdom_detail'),
        path('api/items/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
        path('api/plague/<int:pk>', views.PlagueDetail.as_view(), name='plague_detail'),

        path('', views.home, name='home'),
        path('continents/', views.continent_list_html),
        path('continents/<int:pk>/', views.continent_details_html, name='continent_details'),
        path('locations/', views.location_list_html, name='location-list'),
        path('locations/<int:pk>/', views.location_details_html, name='location-details'),
        path('races/', views.race_list_html, name='race-list'),
        path('races/<int:pk>/', views.race_details_html, name='race-details'),
        path('guilds/', views.guild_list_html, name='guild-list'),
        path('guilds/<int:pk>/', views.guild_details_html, name='guild-details'),
        path('kingdoms/', views.kingdom_list_html, name='kingdom-list'),
        path('kingdoms/<int:pk>/', views.kingdom_details_html, name='kingdom-details'),
        path('items/', views.item_list_html, name='item-list'),
        path('items/<int:pk>/', views.item_details_html, name='item-details'),
        path('plague/', views.plague_html, name='plague'),

        path('login/', views.MyLoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
        path('register/', views.RegisterView.as_view(), name='register'),


     
        
        ]
