from django import forms
from datetime import date
import os
import json
import ee

# Read credentials from environment variable
credentials_str = os.environ['EE_CREDENTIALS']
credentials = json.loads(credentials_str)

# Save to a temp file (needed for ee.ServiceAccountCredentials)
with open("earthengine-credentials.json", "w") as f:
    json.dump(credentials, f)

# Authenticate
ee.Initialize(ee.ServiceAccountCredentials('', 'earthengine-credentials.json'))

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
