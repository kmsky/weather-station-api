from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Measurement
from .serializers import MeasurementSerializer


@api_view(["GET"])
def measurement_collection(request):
    if request.method == "GET":
        date1 = request.query_params.get("date1", None)
        date2 = request.query_params.get("date2", None)

        if date1 and date2 is not None:
            measurements = Measurement.objects.filter(measure_date__gte=date1, measure_date__lte=date2)

        else:
            measurements = Measurement.objects.all()

        serializer = MeasurementSerializer(measurements, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def measurement_element(request, pk):
    try:
        measurement = Measurement.objects.get(pk=pk)
    except Measurement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = MeasurementSerializer(measurement)
        return Response(serializer.data)


@api_view(["GET"])
def measurement_last(request):
    try:
        measurement = Measurement.objects.last()
    except Measurement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = MeasurementSerializer(measurement)
        return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def measurement_post(request, format=None):
    if request.method == "POST":
        serializer = MeasurementSerializer(data=request.data)
        return response_and_save(serializer, status=201)


@api_view(["PUT", "PATCH", "DELETE"])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def measurement_update(request, pk, format=None):
    try:
        measurement = Measurement.objects.get(pk=pk)
    except Measurement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "PATCH":
        serializer = MeasurementSerializer(measurement, data=request.data, partial=True)
        return response_and_save(serializer)

    elif request.method == "PUT":
        serializer = MeasurementSerializer(measurement, data=request.data)
        return response_and_save(serializer)

    elif request.method == "DELETE":
        measurement.delete()
        return Response("Object successfully deleted")


def response_and_save(serializer, status=200):
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status)
    return Response(serializer.errors, status=404)
