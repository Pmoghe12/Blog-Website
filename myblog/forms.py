# forms.py 
from django import forms 
from .models import *

class MyblogForm(forms.ModelForm): 

	class Meta: 
		model = Myblog 
		fields = ['author','title','text', 'image'] 
