from django.shortcuts import render
from companies.models import Company
from skills.models import Skill


# Create your views here.
def index(request):
    skills = Skill.objects.all()
    companies_with_experiences = Company.objects.prefetch_related('experience_set').order_by('-arrangement_id')
    context = {
        'companies_with_experiences':companies_with_experiences,
        'skills': skills
    }
    return render(request, 'pages/index.html', context)
