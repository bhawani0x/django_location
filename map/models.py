from django.db import models
from location_field.models.spatial import LocationField


class CommonModelFieldsBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        abstract = True


class BaseAddress(CommonModelFieldsBase):
    address = models.TextField(null=True, blank=True)
    location = LocationField(based_fields=['address'], zoom=7, null=True, blank=True)

    def __str__(self):
        return self.address

    def save_model(self, request, obj, form, change):
        if not obj.location:
            api_key = ''  # Replace with your actual API key
            url = f'https://maps.googleapis.com/maps/api/geocode/json?address={obj.address}&key={api_key}'
            response = requests.get(url)
            data = response.json()

            if data['status'] == 'OK':
                location = data['results'][0]['geometry']['location']
                obj.location = f"{location['lat']},{location['lng']}"

        super().save_model(request, obj, form, change)
