from django import forms
from .models import Post,Comment, ContactRequest, UserProfileInfo
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields =('author','title','text')

        widgets ={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
    }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields =('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = '__all__'
        widgets = {

            'name':forms.TextInput(attrs={'class':'textinputclass'}),
            'email':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})

        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('first_name','username','email','password','last_name')
        widgets = {

            'username':forms.TextInput(attrs={'class':'textinputclass'}),
            'email':forms.TextInput(attrs={'class':'textinputclass'}),
            'first_name':forms.TextInput(attrs={'class':'textinputclass'}),
            'password':forms.TextInput(attrs={'class':'textinputclass'}),
            'last_name':forms.TextInput(attrs={'class':'textinputclass'})

        }
