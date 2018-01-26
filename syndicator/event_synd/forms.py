from django import forms

class AddProductForm(forms.Form):

    name = forms.CharField(
        max_length=140,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'name'
        })
    )

    description = forms.CharField(
        max_length=1000,
        widget=forms.TextInput(attrs={
            'placeholder': 'description'
        })
    )

    price = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'price'
        })
    )




    