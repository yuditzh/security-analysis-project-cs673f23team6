from rest_framework import serializers

from account.models import CustomUser

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ["user", "title", "description", "price"]

	def post(self, validated_data):
		product = Product.objects.create(**validated_data)
		return product
