from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .seralizier import StudentSerializer
# Create your views here.


@api_view(['GET'])
def list_data(request):
    qs = Student.objects.all()
    serializer = StudentSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_Detail(request, pk):
    qs = Student.objects.get(id=pk)
    serializer = StudentSerializer(qs)
    return Response(serializer.data)


@swagger_auto_schema("POST", request_body=StudentSerializer, responses={200: StudentSerializer})
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_created(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("Error")


@swagger_auto_schema("POST", request_body=StudentSerializer, responses={200: StudentSerializer})
@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_update(request, pk):
    id = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=id, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("Error")


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def list_Delete(request, pk):
    id = Student.objects.get(id=pk)
    id.delete()
    return Response("Successfully deleted")
