from django.shortcuts import render
from .models import Endorsement

def endorsement_list(request):
    endorsements = Endorsement.objects.all()
    return render(request, 'endorsements.html', {'endorsements': endorsements})
