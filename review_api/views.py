from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Sentiment,Emotion,Offense,CategoryData,Category, Region
import json
from rest_framework.views import APIView

# Create your views here.



class ReviewView(APIView):
 def get(self,request):
 	
	#request_data = dict(request.data)
 	business_id = request.GET['id']
 	sentiment_obj = Sentiment.objects.get(pk=business_id)
 	emotion_obj = Emotion.objects.get(pk=business_id)
 	offense_obj = Offense.objects.get(pk=business_id)
 	response_dict = {}
 	response_dict['positive'] = sentiment_obj.positive
 	response_dict['negative'] = sentiment_obj.negative
 	response_dict['happy'] = emotion_obj.happy
 	response_dict['angry'] = emotion_obj.angry
 	response_dict['sad'] = emotion_obj.sad
 	response_dict['joy'] = emotion_obj.joy
 	response_dict['surprise'] = emotion_obj.surprise
 	response_dict['love'] = emotion_obj.love
 	response_dict['offensive'] = offense_obj.offensive
 	response_dict['non_offensive'] = offense_obj.non_offensive
 	categories = Category.objects.filter(business=business_id)
 	cid_list = []
 	for cat in categories:
 		cid_list.append(cat.id)
 	cat_dict = {}
 	for cid in cid_list:
 		cat_obj = CategoryData.objects.get(category_id=cid)
 		cat_name = Category.objects.get(pk=cid).category_name
 		cat_dict[cat_name] = {'positive':cat_obj.positive,'negative':cat_obj.negative,'happy':cat_obj.happy,
 										'angry':cat_obj.angry,'sad':cat_obj.sad,'joy':cat_obj.joy,'surprise':cat_obj.surprise,
 										'love':cat_obj.love,'offensive':cat_obj.offensive,'non_offensive':cat_obj.non_offensive}

 	response_dict["categories"] = cat_dict
 	return Response(response_dict)



class RegionView(APIView):
	def get(self,request):

		business_id = request.GET['id']
		regions = Region.objects.filter(business_id = business_id)
		print(regions)
		response_dict = {}

		for region in regions:
			response_dict[region.reg_id] = {'sentiment':region.sentiment,'emotion':region.emotion}
		return Response(response_dict)


