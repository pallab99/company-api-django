from rest_framework import viewsets, status
from rest_framework.response import Response
from base.responseMessage import RESPONSE_MESSAGE
from .models import Company
from .serializers import CompanySerializer
from rest_framework.decorators import action
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @method_decorator(cache_page(60))
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(
            {"success": True, "message": RESPONSE_MESSAGE["get_all_data_success"],
                "data": response.data},
            status=status.HTTP_200_OK
        )

    @method_decorator(cache_page(60))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {"success": True,
                "message": RESPONSE_MESSAGE["get_single_data_success"], "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        company_exists = Company.objects.filter(name=name).exists()
        if (company_exists):
            return Response(
                {"success": False, "message": "Duplicate company", }, status=status.HTTP_409_CONFLICT
            )
        response = super().create(request, *args, **kwargs)
        updated_queryset = self.get_queryset()
        serialized_data = self.get_serializer(updated_queryset, many=True).data
        cache.set('{}_list'.format(self.get_cache_key_prefix()),
                  serialized_data, 60)
        return Response(
            {"message": "Company created successfully",
                "data": response.data, }, status=status.HTTP_201_CREATED
        )

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        cache.delete('{}_list'.format(self.get_cache_key_prefix()))
        return Response(
            {"message": "Company updated successfully",
                "data": response.data, "status": response.status_code},
        )

    def destroy(self, request, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        cache.delete('{}_list'.format(self.get_cache_key_prefix()))
        return Response(
            {"message": "Company deleted successfully",
                "status": response.status_code, },
        )

    @action(detail=True, methods=["PATCH"], name="Toggle company status")
    def update_status(self, request, pk=None):
        try:
            companyObject = Company.objects.get(pk=pk)
            companyObject.active = not companyObject.active
            serializer = CompanySerializer(companyObject)
            companyObject.save()
            cache.delete('{}_list'.format(self.get_cache_key_prefix()))
            return Response(
                {"success": True, "message": "Company status updated successfully", "data": serializer.data})

        except AttributeError as e:
            return Response(
                {"success": False, "message": "Internal Server Error", "error": str(e)})

        except Exception as e:
            return Response(
                {"success": False, "message": "Internal Server Error", "error": str(e)})

    def get_cache_key_prefix(self):
        # Create a unique cache key prefix for this viewset
        return 'company_viewset'
