from django.contrib import admin
from .models import (
    Location, Contact, Service, Potential, Property, PropertyPicture,
    SingleRoom, House, Apartment, Hostel, Frame, Land, Office, Feature, 
    ProfilePicture, Amenity, RoomType, Room
)

# Register your models here.

admin.site.register(Apartment)
admin.site.register(Frame)
admin.site.register(Hostel)
admin.site.register(House)
admin.site.register(Land)
admin.site.register(Location) 
admin.site.register(Office)
admin.site.register(PropertyPicture)
admin.site.register(ProfilePicture)
admin.site.register(Potential) 
admin.site.register(Property)
admin.site.register(Contact)
admin.site.register(SingleRoom)
admin.site.register(Service)
admin.site.register(Feature)
admin.site.register(Amenity)
admin.site.register(RoomType)
admin.site.register(Room)
