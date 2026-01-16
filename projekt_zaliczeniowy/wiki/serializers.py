from rest_framework import serializers
from model import 

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'
        
class GuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guild
        fields = '__all__'
        
class KingdomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kingdom
        fields = '__all__'
 
class PlagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plague
        fields = '__all__'

class EpicentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epicentre
        fields = '__all__'
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
