from rest_framework import permissions
from rest_framework.views import APIView
from ftl_api.models import User,ActivityPeriod
from .serializers import ActivityPeriodSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
import json
from datetime import datetime


def is_json(json_data):
    is_valid = True
    real_json = json_data
    if not isinstance(json_data,dict):
        try:
            real_json = json.loads(json_data)
        except ValueError:
            is_valid = False
    return is_valid,real_json

class LogUserActivityAPIView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def get(self,request,format=None):
        qs = ActivityPeriod.objects.all()
        serializer = ActivityPeriodSerializer(qs,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        body_ = request.data
        valid_data,data = is_json(body_)
        if valid_data:
            id_list = data['id_list']
            if len(id_list) < 1 :
                return Response(data={"message":"No user provided as input ."},status=200)
            
            output_response = []
            for userid in id_list :
                # check if a valid user is provided !
                try :
                    # lets get the user
                    obj = User.objects.filter(id=userid).values()
                    obj_list = list(obj)
                except User.DoesNotExist:
                    obj = None
                    obj_list = []
                
                if len(obj_list) < 1:
                    continue
                
                member_element = obj_list[0]
                activity_data = ActivityPeriod.objects.filter(user=userid).values()
                activity_data_list = list(activity_data)
                
                
                activity_periods = []
                for activity in activity_data_list:
                    session_date = activity['session_date'].strftime("%b %d %Y")
                    start_time = activity['start_time'].strftime("%I:%M%p")
                    end_time = activity['end_time'].strftime("%I:%M%p")    
                    st_time = str(session_date) + " " + str(start_time)
                    et_time = str(session_date) + " " + str(end_time)
                    curr_activity = {"start_time":st_time,"end_time":et_time}
                    activity_periods.append(curr_activity)
                    member_element['activity_periods'] = activity_periods
                
                output_response.append(member_element)
                    
        return Response(data={"ok":"True","members":output_response},status=200)