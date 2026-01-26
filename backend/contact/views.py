import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
from django.http import HttpResponse


@csrf_exempt

def contact_api(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Message.objects.create(
            name=name,
            email=email,
            message=message
        )

        return HttpResponse("Saved successfully")

    return HttpResponse("Only POST allowed", status=405)
