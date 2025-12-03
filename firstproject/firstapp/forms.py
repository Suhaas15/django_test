from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        # Or u can use: fields = ['first_name', 'last_name', 'guest_count', 'reservation_time', 'comments']