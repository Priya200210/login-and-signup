from .models import Market, BedroomData
from rest_framework import serializers


class MarketSerializer(serializers.ModelSerializer):
	class Meta:
		model = Market
		fields = "__all__"
            

class BedroomDataSerializer(serializers.ModelSerializer):
	class Meta:
		model =BedroomData
		fields = "__all__"