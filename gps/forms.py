from django.forms import ModelForm
from .models import WifiScan, Location


class WifiForm(ModelForm):
    class Meta:
        model = WifiScan    # specify for what model we would be working with
        fields = '__all__'    # specify all fields of the model
class LocationForm(ModelForm):
    class Meta:
        model = Location    # specify for what model we would be working with
        fields = ['location_name','latitude','longitude']    # specify all fields of the model
        