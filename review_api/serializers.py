from rest_framework import serializers
from .models import Region

class RegionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Region
		fields = ('reg_id','sentiment','emotion')
	reg_id = serializers.IntegerField()
	sentiment = serializers.CharField()
	emotion = serializers.CharField()

