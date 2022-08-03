from django.shortcuts import render
from rest_framework import viewsets
from .serializers import VocabSerializer
from .models import Vocab
from .form import VocabForm
from django.contrib import messages
# Create your views here.
class VocabViewSet(viewsets.ModelViewSet):
    queryset = Vocab.objects.all()
    serializer_class = VocabSerializer

def vocabtest(request):
    obj = Vocab.objects.all()
#    for vocab in obj:
#        if request.method == 'POST':
#            form = VocabForm(request.POST)
            # create an instance of our form, and fill it with the POST data
#           urans = request.POST.get('youranswer')
#            if urans != vocab.ans:
#                messages.error(request, 'Wrong Answer.')
#            else:
#                messages.success(request, 'Correct.')



 #       else:
            # this must be a GET request, so create an empty form
#            form = VocabForm()
    return render(request, "formpractice.html", {'obj': obj})


