import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message

@csrf_exempt
def contact_api(request):
    if request.method == "POST":
        data = json.loads(request.body)
        Contact.objects.create(
            name=data["name"],
            email=data["email"],
            message=data["message"]
        )
        return JsonResponse({"status": "saved"})
