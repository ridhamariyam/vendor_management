from django.shortcuts import render
from rest_framework import generics, permissions
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime
from django.utils import timezone
from django.db.models import Q

# Create your views here.
class VendorView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailsView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    lookup_field = 'id'

class PurchaseOrderView(generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderCreateSerializer


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)


class PurchaseOrderCRUDView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [permissions.IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'id'


class POAknowledgeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=id)
            if purchase_order.acknowledgment_date == None:
                purchase_order.acknowledgment_date = datetime.now()
                purchase_order.save()
                avg_response_time = average_response_time(purchase_order.issue_date, purchase_order.acknowledgment_date, purchase_order)
                vendor = purchase_order.vendor
                vendor.average_response_time = avg_response_time
                vendor.save()

                performance = Performance.objects.get(vendor=vendor)
                performance.average_response_time = avg_response_time
                performance.date = datetime.now()
                performance.save()
                
                serializer = PurchaseOrderSerializer(purchase_order)
                return Response(serializer.data)
            return Response({'message':'already acknowledged'}, status=404)
        except PurchaseOrder.DoesNotExist:
            return Response({'message': 'Purchase Order not found'}, status=404)
        except Exception as e:
            print(e)
            return Response({'message': 'An error occurred'}, status=500)

#for finding the average response time
def average_response_time(issue, aknowledge, purchase_order):
    deff = (aknowledge.date() - issue.date()).days
    count = PurchaseOrder.objects.filter(acknowledgment_date__isnull=False, vendor = purchase_order.vendor).count()
    return ((purchase_order.vendor.average_response_time*(count-1)) + deff) / count


class PODevliveryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=id)   
            if purchase_order.status == 'pending':
                purchase_order.status = 'completed'
                purchase_order.save()

                vendor = purchase_order.vendor

                on_time_delivery_rate = get_on_time_delivery_rate(purchase_order)
                fullfilment_rate = get_fulfillment_rate(purchase_order)
                vendor.on_time_delivery_rate = on_time_delivery_rate
                vendor.fulfillment_rate = fullfilment_rate
                vendor.save()

                performance = Performance.objects.get(vendor=vendor)
                performance.on_time_delivery_rate = on_time_delivery_rate
                performance.date = datetime.now()
                performance.fulfillment_rate = fullfilment_rate
                performance.save()

                serializer = PurchaseOrderSerializer(purchase_order)
                return Response(serializer.data)
            return Response({'message':'already delivered'})
        except PurchaseOrder.DoesNotExist:
            return Response({'message': 'Purchase Order not found'}, status=404)
        except Exception as e:
            # Log the exception
            print(e)
            return Response({'message': 'An error occurred'}, status=500)


def get_on_time_delivery_rate(purchase_order):

    completed_count = PurchaseOrder.objects.filter(vendor=purchase_order.vendor, status = 'completed').count()

    if completed_count == 0:
        return 0
    
    if purchase_order.delivery_date > timezone.now():
        on_time_count = purchase_order.vendor.on_time_delivery_rate * (completed_count-1) / 100
        on_time_count += 1
        return (on_time_count / completed_count * 100)
    
    else:
        on_time_count = purchase_order.vendor.on_time_delivery_rate * (completed_count-1) / 100
        on_time_count -= 1
        return (on_time_count / completed_count * 100)

def get_fulfillment_rate(purchase_order):
    completed_count = PurchaseOrder.objects.filter(vendor=purchase_order.vendor, status = 'completed').count()
    count = PurchaseOrder.objects.filter(vendor=purchase_order.vendor).count()
    return completed_count /count * 100


class PORatingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, id):
        try:
            purchase_order = PurchaseOrder.objects.get(id=id)
            quality_rating = int(request.data.get('qualityRating'))
            if int(quality_rating) > 10:
                return Response({"errors":'Rating should be less than 3'})
            quality_rating_avg = get_quality_rating_avg(purchase_order, quality_rating)

            purchase_order.quality_rating = quality_rating
            purchase_order.save()

            vendor = purchase_order.vendor
            vendor.quality_rating_avg = quality_rating_avg
            vendor.save()

            performance = Performance.objects.get(vendor=vendor)
            performance.date = datetime.now()
            performance.quality_rating_avg = quality_rating_avg
            performance.save()

            serializer = PurchaseOrderSerializer(purchase_order)
            return Response(serializer.data)

        except PurchaseOrder.DoesNotExist:
            return Response({'message': 'Purchase Order not found'}, status=404)
        except Exception as e:
            # Log the exception
            print(e)
            return Response({'message': 'An error occurred'}, status=500)

            

def get_quality_rating_avg(purchase_order, quality_rating):

    count = PurchaseOrder.objects.filter(quality_rating__isnull=False, vendor = purchase_order.vendor).count()
    last_total_rating = purchase_order.vendor.quality_rating_avg * count

    if purchase_order.quality_rating:
        new_avg = (last_total_rating - purchase_order.quality_rating + quality_rating) / count
    else:
        new_avg = (last_total_rating + quality_rating) / (count + 1)

    return new_avg

class VendorPerformanceView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Performance.objects.all()
    serializer_class = PerfomanceSerializer
    lookup_field = 'id'

    def get_object(self):
        id = self.kwargs.get(self.lookup_field)
        return self.queryset.filter(vendor__id = id).first()