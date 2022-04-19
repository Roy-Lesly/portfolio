from django.shortcuts import render


def WelcomeView(request):
    context = {
        # "title": 'Medical Radiology Department',
        "title": 'RADIOLOGY INFORMATION SYSTEM',
        "page_title": "RADIOLOGY",
        "sub_title": "Home Page",
    }
    return render(request, 'resume/resume_welcome.html', context)