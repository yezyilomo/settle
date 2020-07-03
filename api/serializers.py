from rest_framework import serializers
from django.contrib.auth.models import Group
from django.core.exceptions import ObjectDoesNotExist
from django_restql.mixins import DynamicFieldsMixin
from django_restql.fields import NestedField
from django_restql.serializers import NestedModelSerializer

from .models import (
    Location, Contact, Service, Potential, Property, Feature,
    PropertyPicture, Room, House, Apartment, Hostel, Frame, Land,
    Office, Amenity, User, ProfilePicture
)


class ProfilePictureSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ('id', 'url', 'src')

    def create(self, validated_data):
        """function for creating a profile picture """
        request = self.context.get('request')
        user = request.user

        validated_data.update({"owner": user})
        picture = super().create(validated_data)
        return picture


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    picture = ProfilePictureSerializer(read_only=True)
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )
    class Meta:
        model = User
        fields = (
            'id', 'url', 'username', 'email', 'password', 'phone', 'groups',
            'date_joined', 'is_staff', 'full_name', 'is_active', 'picture',
            'biography'
        )
        read_only_fields = (
            'date_joined', 'is_staff'
        )
        

class GroupSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class LocationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id', 'url', 'country', 'region', 'distric',
            'street1', 'street2', 'longitude', 'latitude'
        )


class ContactSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'url', 'name', 'email', 'phone')


class AmenitySerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ('id', 'url', 'name')


class ServiceSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'url', 'name')


class PotentialSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Potential
        fields = ('id', 'url', 'name')


class PropertyPictureSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = PropertyPicture
        fields = ('id', 'url', 'is_main', 'property', 'tooltip', 'src')

    def create(self, validated_data):
        """function for creating a property picture """
        request = self.context.get('request')
        user = request.user

        property = validated_data.get("property", None)

        if property.owner != user:
            raise serializers.ValidationError(
                {"property": f"You don't own a property with `id={property.pk}`"},
                "Value error"
            )

        return super().create(validated_data)


class FeatureSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'url', 'property', 'name', 'value')


class PropertySerializer(DynamicFieldsMixin, NestedModelSerializer):
    pictures = PropertyPictureSerializer(many=True, read_only=True)
    location = NestedField(LocationSerializer, many=False)
    amenities = NestedField(AmenitySerializer, many=True, required=False)
    services = NestedField(ServiceSerializer, many=True, required=False)
    potentials = NestedField(PotentialSerializer, many=True, required=False)
    contact = NestedField(ContactSerializer, many=False, required=False)
    other_features = NestedField(FeatureSerializer,
        many=True, required=False, create_ops=["create"],
        update_ops=["update", "create", "remove"]
    )
    owner = UserSerializer(many=False, read_only=True)
    type = serializers.CharField(read_only=True)
    class Meta:
        model = Property
        fields = (
            'id', 'url', 'type', 'available_for', 'available_for_options', 'price',
            'price_rate_unit', 'payment_terms', 'is_price_negotiable', 'rating',
            'currency', 'descriptions', 'location', 'owner', 'amenities',
            'services', 'potentials', 'pictures', 'other_features', 'contact',
            'post_date',
        )

    def create(self, validated_data):
        """function for creating a property """
        request = self.context.get('request')
        user = request.user

        validated_data.update({"owner": user})
        property = super().create(validated_data)
        return property


class RoomSerializer(PropertySerializer):
    class Meta:
        model = Room
        fields = ()

    Meta.fields = PropertySerializer.Meta.fields + Meta.fields


class HouseSerializer(PropertySerializer):
    class Meta:
        model = House
        fields = ()

    Meta.fields = PropertySerializer.Meta.fields + Meta.fields


class ApartmentSerializer(PropertySerializer):
    class Meta:
        model = Apartment
        fields = ()

    Meta.fields = PropertySerializer.Meta.fields + Meta.fields


class LandSerializer(PropertySerializer):
    class Meta:
        model = Land
        fields = (
            'width', 'length', 'area', 'is_registered',
        )

    Meta.fields = PropertySerializer.Meta.fields + Meta.fields


class FrameSerializer(PropertySerializer):
    class Meta:
        model = Frame
        fields = ()

    Meta.fields = PropertySerializer.Meta.fields + Meta.fields


class OfficeSerializer(PropertySerializer):
    class Meta:
        model = Office
        fields = ()

    Meta.fields = PropertySerializer.Meta.fields + Meta.fields


class HostelSerializer(PropertySerializer):
    class Meta:
        model = Hostel
        fields = ()

    Meta.fields = PropertySerializer.Meta.fields + Meta.fields

