from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

@csrf_exempt
@require_POST
def handle_form_submission(request):
    try:
        data = json.loads(request.body)

        form_type = data.get("formType")
        name = data.get("name")
        email = data.get("email")
        contact = data.get("contact")
        linkedin = data.get("linkedin", "")
        dev_worked_with = data.get("dev", "")
        experience = data.get("experience", "")

        if not (name and email and contact):
            return JsonResponse({'success': False, 'message': 'Missing required fields'}, status=400)

        subject = f"New Submission: {form_type}"
        body = f"Name: {name}\nEmail: {email}\nContact: {contact}\nLinkedIn: {linkedin}"

        if form_type == "endorsement":
            body += f"\nBLV Dev: {dev_worked_with}\nExperience: {experience}"

        send_mail(
            subject=subject,
            message=body,
            from_email="development@blvdevelopers.org",
            recipient_list=["pranavchinthala75@gmail.com"],
            fail_silently=False,
        )
        return JsonResponse({'success': True, 'message': 'Response saved successfully'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)}, status=500)