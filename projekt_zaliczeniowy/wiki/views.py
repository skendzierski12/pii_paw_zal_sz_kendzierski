from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Continent, Kingdom, Race, Location, Guild, Plague, Epicentre, Item
from .serializers import ContinentSerializer, KingdomSerializer, RaceSerializer, LocationSerializer, GuildSerializer, PlagueSerializer, EpicentreSerializer, ItemSerializer
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .permissions import IsAdminOrEditor
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#Listy API

class ContinentList(generics.ListCreateAPIView):
    queryset=Continent.objects.all()
    serializer_class = ContinentSerializer
    permission_classes = [IsAdminOrEditor]

#@api_view(['GET', 'POST'])
#@permission_classes([IsAdminOrEditor])
#def continent_list(request):
#    if request.method == 'GET':
#        continents = Continent.objects.all()
#        serializer = ContinentSerializer(continents, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = ContinentSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=201)
#        return Response(serializer.errors, status=400)


class KingdomList(generics.ListCreateAPIView):
    queryset=Kingdom.objects.all()
    serializer_class = KingdomSerializer
    permission_classes = [IsAdminOrEditor]

#@api_view(['GET', 'POST'])
#@permission_classes([IsAdminOrEditor])
#def kingdom_list(request):
#    if request.method == 'GET':
#        kingdoms = Kingdom.objects.all()
#        serializer = KingdomSerializer(kingdoms, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = KingdomSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=201)
#        return Response(serializer.errors, status=400)


class RaceList(generics.ListCreateAPIView):
    queryset=Race.objects.all()
    serializer_class = RaceSerializer
    permission_classes = [IsAdminOrEditor]


#@api_view(['GET', 'POST'])
#@permission_classes([IsAdminOrEditor])
#def race_list(request):
#    if request.method == 'GET':
#        races = Race.objects.all()
#        serializer = RaceSerializer(races, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = RaceSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=201)
#        return Response(serializer.errors, status=400)

class LocationList(generics.ListCreateAPIView):
    queryset=Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsAdminOrEditor]



#@api_view(['GET', 'POST'])
#@permission_classes([IsAdminOrEditor])
#def location_list(request):
#    if request.method == 'GET':
#        locations = Location.objects.all()
#        serializer = LocationSerializer(locations, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = LocationSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=201)
#        return Response(serializer.errors, status=400)


class GuildList(generics.ListCreateAPIView):
    queryset=Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = [IsAdminOrEditor]


#@api_view(['GET', 'POST'])
#@permission_classes([IsAdminOrEditor])
#def guild_list(request):
#    if request.method == 'GET':
#        guilds = Guild.objects.all()
#        serializer = GuildSerializer(guilds, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = GuildSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=201)
#        return Response(serializer.errors, status=400)


class EpicentreList(generics.ListCreateAPIView):
    queryset=Epicentre.objects.all()
    serializer_class = EpicentreSerializer
    permission_classes = [IsAdminOrEditor]


#@api_view(['GET', 'POST'])
#@permission_classes([IsAdminOrEditor])
#def epicentre_list(request):
#    if request.method == 'GET':
#        epicentres = Epicentre.objects.all()
#        serializer = EpicentreSerializer(epicentres, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = EpicentreSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=201)
#        return Response(serializer.errors, status=400)


class ItemList(generics.ListCreateAPIView):
    queryset=Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAdminOrEditor]


#@api_view(['GET', 'POST'])
#@permission_classes([IsAdminOrEditor])
#def item_list(request):
#    if request.method == 'GET':
#        items = Item.objects.all()
#        serializer = ItemSerializer(items, many=True)
#        return Response(serializer.data)
#    elif request.method == 'POST':
#        serializer = ItemSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=201)
#        return Response(serializer.errors, status=400)


#Detailsy API


class ContinentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    premission_classes = [IsAdminOrEditor]

#@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAdminOrEditor])
#def continent_detail(request, pk):
#    try:
#        continent = Continent.objects.get(pk=pk)
#    except Continent.DoesNotExist:
#        return Response(status=404)
#    
#    if request.method == 'GET':
#        serializer = ContinentSerializer(continent)
#        return Response(serializer.data)
#    
#    elif request.method == 'PUT':
#        serializer = ContinentSerializer(continent, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=400)
#    
#    elif request.method == 'DELETE':
#        continent.delete()
#        return Response(status=204)

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    premission_classes = [IsAdminOrEditor]



#@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAdminOrEditor])
#def location_detail(request, pk):
#    try:
#        location = Location.objects.get(pk=pk)
#    except Location.DoesNotExist:
#        return Response(status=404)
#    
#    if request.method == 'GET':
#        serializer = LocationSerializer(location)
#        return Response(serializer.data)
#    elif request.method == 'PUT':
#        serializer = LocationSerializer(location, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=400)
#    elif request.method == 'DELETE':
#        location.delete()
#        return Response(status=204)

class RaceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    premission_classes = [IsAdminOrEditor]


#@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAdminOrEditor])
#def race_detail(request, pk):
#    try:
#        race = Race.objects.get(pk=pk)
#    except Race.DoesNotExist:
#        return Response(status=404)
#    
#    if request.method == 'GET':
#        serializer = RaceSerializer(race)
#        return Response(serializer.data)
#    elif request.method == 'PUT':
#        serializer = RaceSerializer(race, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=400)
#    elif request.method == 'DELETE':
#        race.delete()
#        return Response(status=204)


class GuildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    premission_classes = [IsAdminOrEditor]

#@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAdminOrEditor])
#def guild_detail(request, pk):
#    try:
#        guild = Guild.objects.get(pk=pk)
#    except Guild.DoesNotExist:
#        return Response(status=404)
#    
#    if request.method == 'GET':
#        serializer = GuildSerializer(guild)
#        return Response(serializer.data)
#    elif request.method == 'PUT':
#        serializer = GuildSerializer(guild, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=400)
#    elif request.method == 'DELETE':
#        guild.delete()
#        return Response(status=204)

class KingdomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kingdom.objects.all()
    serializer_class = KingdomSerializer
    premission_classes = [IsAdminOrEditor]


#@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAdminOrEditor])
#def kingdom_detail(request, pk):
#    try:
#        kingdom = Kingdom.objects.get(pk=pk)
#    except Kingdom.DoesNotExist:
#        return Response(status=404)
#    
#    if request.method == 'GET':
#        serializer = KingdomSerializer(kingdom)
#        return Response(serializer.data)
#    elif request.method == 'PUT':
#        serializer = KingdomSerializer(kingdom, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=400)
#    elif request.method == 'DELETE':
#        kingdom.delete()
#        return Response(status=204)

class PlagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plague.objects.all()
    serializer_class = PlagueSerializer
    premission_classes = [IsAdminOrEditor]


#@api_view(['GET', 'PUT'])
#@permission_classes([IsAdminOrEditor])
#def plague_detail(request): 
#    plague = Plague.objects.first()
#    
#    if request.method == 'GET':
#        serializer = PlagueSerializer(plague)
#        return Response(serializer.data)
#    elif request.method == 'PUT':
#        serializer = PlagueSerializer(plague, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=400)


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    premission_classes = [IsAdminOrEditor]


#@api_view(['GET', 'PUT', 'DELETE'])
#@permission_classes([IsAdminOrEditor])
#def item_detail(request, pk):
#    try:
#        item = Item.objects.get(pk=pk)
#    except Item.DoesNotExist:
#        return Response(status=404)
    
#    if request.method == 'GET':
#        serializer = ItemSerializer(item)
#        return Response(serializer.data)
#    elif request.method == 'PUT':
#        serializer = ItemSerializer(item, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=400)
#    elif request.method == 'DELETE':
#        item.delete()
#        return Response(status=204)

#HTMLsy

def home(request):
    return render(request, 'wiki/home.html')

def continent_list_html(request):
    continents = Continent.objects.all()
    return render(request, 'wiki/continents/continent_list.html', {'continents': continents})

def continent_details_html(request, pk):
    continent = Continent.objects.get(pk=pk)
    return render(request, 'wiki/continents/continent_details.html', {'continent': continent})

def location_list_html(request):
    locations = Location.objects.all()
    return render(request, 'wiki/locations/location_list.html', {'locations': locations})

def location_details_html(request, pk):
    location = Location.objects.get(pk=pk)
    return render(request, 'wiki/locations/location_details.html', {'location': location})

def race_list_html(request):
    races = Race.objects.all()
    return render(request, 'wiki/races/race_list.html', {'races': races})

def race_details_html(request, pk):
    race = Race.objects.get(pk=pk)
    return render(request, 'wiki/races/race_details.html', {'race': race})

def guild_list_html(request):
    guilds = Guild.objects.all()
    return render(request, 'wiki/guilds/guild_list.html', {'guilds': guilds})

def guild_details_html(request, pk):
    guild = Guild.objects.get(pk=pk)
    return render(request, 'wiki/guilds/guild_details.html', {'guild': guild})

def kingdom_list_html(request):
    kingdoms = Kingdom.objects.all()
    return render(request, 'wiki/kingdoms/kingdom_list.html', {'kingdoms': kingdoms})

def kingdom_details_html(request, pk):
    kingdom = Kingdom.objects.get(pk=pk)
    return render(request, 'wiki/kingdoms/kingdom_details.html', {'kingdom': kingdom})

def item_list_html(request):
    items = Item.objects.all()
    return render(request, 'wiki/items/item_list.html', {'items': items})

def item_details_html(request, pk):
    item = Item.objects.get (pk=pk)
    return render(request, 'wiki/items/item_details.html', {'item': item})

def plague_html(request):
    plague = Plague.objects.first()
    return render(request, 'wiki/plague/plague.html', {'plague': plague})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else: 
            return render(request, 'wiki/auth/login.html', {'error': 'Nieprawidłowe dane logowania'})
    return render(request, 'wiki/auth/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Konto zostało utworzone pomyślnie!')
            return redirect('home')
        else:
            messages.error(request, 'Login lub hasło niepoprawne!')
    else:
        form = UserCreationForm()

    return render(request, 'wiki/auth/register.html', {'form': form})









