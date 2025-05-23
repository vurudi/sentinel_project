from django import forms
from datetime import date
import os
import json
import ee

# Load EE credentials
ee_json = os.getenv('EE_CREDENTIALS')
with open('ee-key.json', 'w') as f:
    f.write(ee_json)

# Initialize EE with service account
ee.Initialize(ee.ServiceAccountCredentials(
    'sentinel-36@brainbox-448715.iam.gserviceaccount.com',
    'ee-key.json'
))

class SentinelForm(forms.Form):
    geojson_file = forms.FileField(label="GeoJSON File")
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')
        if start and end:
            if end < start:
                raise forms.ValidationError("End date must be after start date.")
            if start > date.today():
                raise forms.ValidationError("Start date cannot be in the future.")
        return cleaned_data
