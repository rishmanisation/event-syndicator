from django import forms

class AddEventForm(forms.Form):

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

    currency = forms.CharField(
        max_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': 'CUR'
        })
    )

    price = forms.DecimalField(
        min_value=0.0,
        widget=forms.NumberInput()
    )

    start_date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs = {
                'type': 'date'
            }
        )
    )

    start_time = forms.TimeField(
        widget=forms.widgets.TimeInput(
            attrs = {
                'type': 'time'
            }
        )
    )

    end_date = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs = {
                'type': 'date'
            }
        )
    )

    end_time = forms.TimeField(
        widget=forms.widgets.TimeInput(
            attrs = {
                'type': 'time'
            }
        )
    )

    timezone = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'timezone in Olson'
            }
        )
    )




    