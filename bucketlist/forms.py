from django import forms


class ObjectiveForm(forms.Form):
    title = forms.CharField(label='Title', max_length=50)
    content = forms.CharField(label='Content', max_length=500)

    def clean(self):
        title = self.cleaned_data['title']
        content = self.cleaned_data['content']
        return {title: content}