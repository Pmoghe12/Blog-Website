from django.views.generic import ListView,DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from .models import Myblog
from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import render, redirect 
from django.http import HttpResponse 



class Homepage(ListView):
    model = Myblog
    template_name ="home.html"

class ViewDetail(DetailView):
    model = Myblog
    template_name ="DetailView.html"
    context_object_name = 'batman'

class AddPost(CreateView):
    model = Myblog
    template_name ="addnew.html"
    fields = ['author','title' ,'text','image']

class EditPost(UpdateView):
    model = Myblog
    template_name ="blog_edit.html"
    context_object_name = 'superman'
    fields = ['text']

class DeletePost(DeleteView):
    model = Myblog
    template_name ="blog_delete.html"
    context_object_name = 'batman'
    fields = ['title' ,'text']
    success_url = reverse_lazy('home')

class Aboutus(ListView):
    model = Myblog
    template_name ="aboutus.html"

class Abt(ListView):
    model = Myblog
    template_name = "about.html"

class Join(ListView):
    model = Myblog
    template_name = "join.html"

def hotel_image_view(request): 

	if request.method == 'POST': 
		form = MyblogForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			#return redirect('success') 
	else: 
		form = MyblogForm() 
	return render(request, 'addnew.html', {'form' : form}) 


# def success(request): 
	#return HttpResponse('successfully uploaded') 

    