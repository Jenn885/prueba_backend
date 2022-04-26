from asyncio.windows_events import NULL
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JobItemSerializer
from .models import Job


# Create your views here.

           
class JobItemsViews(APIView):
     def post(self, request):
        
        serializer = JobItemSerializer(data=request.data)
        name = request.data['name']
        
        if Job.objects.filter(name=name).exists():
         
            return Response({ "id": None, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                serializer.save()
                return Response({ "id": serializer.data['id'], "sucess": True}, status=status.HTTP_200_OK)
                
            else:
                return Response({ "id": serializer.errors, "sucess": False}, status=status.HTTP_400_BAD_REQUEST)

    

class JobListItemViews(APIView):
    
    def get(self, request, id=None):
        if id:
            item = Job.objects.get(id=id)
            serializer = JobItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Job.objects.all()
        serializer = JobItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    