from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def get_message(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        return JsonResponse({'message': message})
    return JsonResponse({'message': 'Hello, World!'})