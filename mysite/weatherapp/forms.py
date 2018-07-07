from django.forms import ModelForm, TextInput
from .models import City

# The form is basically the same ad the model!
class CityForm(ModelForm):
	class Meta:
		model = City
		fields = ['name']
		# TextInput!
		widgets =  {'name' : TextInput(attrs = {'class' : 'input', 'placeholder' : 'City Name'})}
