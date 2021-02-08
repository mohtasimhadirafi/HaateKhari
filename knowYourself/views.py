import cv2
import base64
import os.path
from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .bodyPartsDetection import bodyPartDetection

# Create your views here.

def test(request):
    from .testFile import load_images_from_folder
    return render(request, 'test.html', {'image' : load_images_from_folder})


def add_image_know_you(request):
    if request.method == 'POST':
        form = KnowYourSelfForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Your photo updated successfully.")
            return redirect('add_image_know_you')
    else:
        form = KnowYourSelfForm()
    return render(request, 'add_image_know_you.html', {'form' : form})


def know_you_learn(request):
    action = 'Nose'
    imagePath = 'media/knowYourself/imageDB/0.jpg'
    resultPath = 'media/knowYourself/temp/result.jpg'
    image = bodyPartDetection(cv2.resize(cv2.imread(imagePath), None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA), action)
    cv2.imwrite(resultPath, image)
    return render(request, 'know_you_learn.html', {'image' : resultPath, 'element' : action})


def know_you_identity(request):
    actions = ['eye', 'nose', 'frontalFace', 'mouth']
    for i in range(4):
        context = "media/knowYourself/"+actions[i]+".jpg"
        action = actions[i]
        if os.path.exists(context):
            break
        else:
            context = None
            action = None
    return render(request, 'know_you_identity.html', {'context' : context, 'action' : action})