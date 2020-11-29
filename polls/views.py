from django.shortcuts import render, redirect
from django.core import serializers
from .models import Candidates
import pusher
import json


pusher_client = pusher.Pusher(
  app_id='1114552',
  key='0a546ba40b49dfb81ecd',
  secret='c169e358abf2c273cb10',
  cluster='ap2',
  ssl=True
)


def mainpage(request):
    candidates = Candidates.objects.all()
    return render(request, 'index.html', {'candidates':candidates})


import json
def voting(request):
    if request.method == 'POST':
        print(request.POST)
        candidate_id = request.POST.get('candidate')
        candidate = Candidates.objects.get(id=candidate_id)
        candidate.counts += 1
        candidate.save()
        candidates = Candidates.objects.all()
        candidates_data = serializers.serialize('json', candidates)
        pusher_client.trigger('voting-channel', 'voting', {'candidates':candidates_data})

    return redirect('mainpage')




