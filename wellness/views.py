from django.shortcuts import render
from .models import WellnessProgram

def wellness_programs(request):
    programs = WellnessProgram.objects.all()
    return render(request, 'wellness/programs.html', {'programs': programs})

import openai
from django.conf import settings
from django.http import JsonResponse

def generate_ai_module(request):
    if request.method == 'POST':
        topic = request.POST.get('topic', '')

        # Set the OpenAI API key from settings
        openai.api_key = settings.OPENAI_API_KEY

        try:
            # Call the OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use GPT-3.5 or GPT-4
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that generates training modules."},
                    {"role": "user", "content": f"Create a training module about {topic}."}
                ]
            )

            # Extract the generated content
            ai_content = response.choices[0].message.content

            # Return the AI-generated content as JSON
            return JsonResponse({"content": ai_content})

        except Exception as e:
            # Handle errors
            return JsonResponse({"error": str(e)}, status=500)

    # Return an error if the request method is not POST
    return JsonResponse({"error": "Invalid request method"}, status=400)
