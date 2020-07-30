from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect

droplets = [
    {
        'title':'title1',
        'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas rhoncus neque nisl, ac bibendum justo faucibus ut. Suspendisse potenti.',
    },
    {
        'title': 'title2',
        'content': 'Integer congue eros metus, eget aliquam est tristique ac. Fusce eget viverra leo. Donec mollis leo at fringilla tempor. Donec ante lacus,',
    },
    {
        'title':'title3',
        'content':'maximus eu enim quis, rhoncus malesuada dolor. Sed venenatis est eget eleifend ultrices.',
    },
    {
        'title': 'title4',
        'content': 'Ut suscipit eget lacus vitae facilisis. Morbi nec semper nunc, vel varius lacus. Curabitur dui risus, convallis ut lacinia ut, congue ac nisi. Praesent sollicitudin in tellus id pharetra. Mauris ut bibendum massa.',
    },
    {
        'title':'title5',
        'content':' Etiam eros ipsum, pretium quis tincidunt non, congue a nisl. Quisque aliquet sed purus nec euismod. Vivamus malesuada sapien sit amet cursus eleifend.',
    },

]

class Objective(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    description = forms.CharField(label='Description', max_length=500)


def home(request):
    context = {
        'droplets':droplets,
    }
    return render(request, 'bucketlist/bucketlist_display.html', context)

def get_input(request):
    if request.method == 'POST':
        form = Objective(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('')
    else:
        form = Objective()
    return render(request, 'bucketlist/bucketlist_get_input.html', {'form':form})




