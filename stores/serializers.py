from django.db.models import fields
from rest_framework import serializers
from rest_framework import filters
from rest_framework.reverse import reverse
from rest_framework.utils import model_meta

from .models import Pizzeria


class PizzeriaListSerializer(serializers.ModelSerializer):
    """
    List information of the Pizzeria
    Fields:(
        1.id,
        2.pizzeria_name,
        3.city,
        4.zip_code,

    )
    """
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'city',
            'zip_code',



        ]

        def get_absolute_url(self, obj):
            return reverse('pizzeria_detail', args=(obj.pk,))


class PizzeriaDetailSerializer(serializers.ModelSerializer):
    """
    Hold detail information of the Pizzeria
    Fields:(
        1.id,
        2.logo_image,
        3.pizzeria_name,
        4.city,
        5.zip_code,
        6.website,
        7.phone_number,
        8.description,
        9.logo_image,
        10.email,
        11.active
    )
    """
    class Meta:
        model = Pizzeria
        fields = [
            'id',
            'pizzeria_name',
            'street',
            'city',
            'state',
            'zip_code',
            'website',
            # 'phone_number',
            'description',
            'logo_image',
            'email',
            'active',

        ]
