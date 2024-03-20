from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.

def get_auth_for_user(user):
	tokens = RefreshToken.for_user(user)
	return {
		'user': UserSerializer(user).data,
		'tokens': {
			'access': str(tokens.access_token),
			'refresh': str(tokens),
		}
	}

class GetView(APIView):
	permission_classes = [AllowAny]

	def post(self, request):
		new_user =ProductSerializer(data=request.data)
		new_user.is_valid(raise_exception=True)
		user = new_user.save()

		user_data = get_auth_for_user(user)

		return Response(user_data)


class CompanyView(ListAPIView):
	authentication_classes = []

	def get(self, request, format=None):
		info_to_serialize = Companies.objects.filter(product_set__extra_tag='AMZ').distinct()
		women_category = CompaniesSerializer(info_to_serialize, many=True, context={"request":request}).data
		return Response({}, status=status.HTTP_200_OK)


class ProductListView(ListAPIView):
	authentication_classes = []
	serializer_class = ProductSerializer
	model = Product
	queryset = Product.objects.all()

	def get_serializer_context(self):
		context = super(ProductListView, self).get_serializer_context()
		context.update({"request": self.request})
		return context