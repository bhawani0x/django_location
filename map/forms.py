from django import forms
from .models import BaseAddress
import requests


class AddressAdminForm(forms.ModelForm):
    class Meta:
        model = BaseAddress
        fields = '__all__'

    def clean_address(self):
        address = self.cleaned_data['address']
        api_key = ''  # Replace with your actual API key

        # Make a request to the Google Geocoding API
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            self.cleaned_data['location'] = f"POINT({location['lng']} {location['lat']})"
            return address
        else:
            raise forms.ValidationError(f"Geocoding failed: {data['status']}")
