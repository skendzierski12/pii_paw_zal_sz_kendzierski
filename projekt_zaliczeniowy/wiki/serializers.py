from rest_framework import serializers
from .models import Continent, Location, Race, Guild, Kingdom, Plague, Epicentre, Item
from django.contrib.auth.models import User



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

#class UserRegisterSerializer(serializers.ModelSerializer):
#    password = serializers.ChatField(write_only=True)
#
#    class Meta:
#        model = User
#        fields = ['username', 'email', 'password']
#    def create(self, validated_data):
#        user = User.objects.create_user(
#            username=validated_data['username'],
#            email=validated_data.get('email', ''),
#            password=validated_data['password']
#        )
#        return user        

class RegisterAndLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
