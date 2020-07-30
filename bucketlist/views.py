from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

droplets = [

]

class Objective(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    description = forms.CharField(label='Description', max_length=500)

    def droplets_append(self, title, description):
        droplet ={
            'title': title,
            'content': description
        }
        droplets.append(droplet)



def home(request):
    context = {
        'droplets':droplets,
    }
    return render(request, 'bucketlist/bucketlist_display.html', context)

def get_input(request):
    if request.method == 'POST':
        form = Objective(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            form.droplets_append(title, description)
            return HttpResponseRedirect('../')
    else:
        form = Objective()
    return render(request, 'bucketlist/bucketlist_get_input.html', {'form': form})




