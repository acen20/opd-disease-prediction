from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import pickle
from django.views.decorators.csrf import csrf_exempt
from .models import Features
import numpy as np

# Create your views here

@csrf_exempt
def home(request):
    all_symptoms = Features.objects.all()
    prediction = None;
    if request.POST:
        model = pickle.load(open('RBF.sav', 'rb'))
        pca = pickle.load(open('PCA.sav', 'rb'))
        le = pickle.load(open('Encoder.sav', 'rb'))
        active_symptoms = []
        for i, value in request.POST.items():
            if int(value):
                active_symptoms.append(int(i))
        print(active_symptoms)
        print([all_symptoms[i].txt for i in active_symptoms])
        zero_array = [i*0 for i in range(0, 132)]
        for symptom in active_symptoms:
            zero_array[symptom] = 1
        zero_array = np.array(zero_array).reshape(1,-1)
        zero_array = pca.transform(zero_array)
        prediction = model.predict(zero_array)
        prediction = le.inverse_transform(prediction)[0]
        print(prediction)
    context = {
        'symptoms': all_symptoms,
        'prediction': prediction
        }
    return render(request, "main/home.html", context)
