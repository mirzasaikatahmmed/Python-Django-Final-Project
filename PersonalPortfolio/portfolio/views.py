from django.shortcuts import render
from .models import WorkExperience, Skill, Project, Education, About
from .models import Contact
from django.contrib import messages
from django.shortcuts import redirect


def index(request):
    experiences = WorkExperience.objects.all()
    skills = Skill.objects.all()
    projects = Project.objects.all()
    educations = Education.objects.all()
    about_content = About.objects.first() #Gets the first (and only) About object
    return render(request, 'portfolio/index.html', {
        'experiences': experiences,
        'skills': skills,
        'projects': projects,
        'educations': educations,
        'about_content': about_content,
    })
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # ✅ Save the contact form data
        Contact.objects.create(name=name, email=email, message=message)

        # ✅ Show a success message
        messages.success(request, "Your message has been submitted successfully!")
        return redirect('index')

    return render(request, 'portfolio/index.html')