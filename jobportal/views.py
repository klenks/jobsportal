#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect, HttpResponse

from django.http import Http404
from django.shortcuts import render, get_object_or_404
#from django.urls import reverse
from django.views import generic

from django.template import loader

from .models import JobSeeker, Employer, Job, JobApplication

#def IndexView(ListView):
#    template_name = 'jobportal/index.html'

class IndexView(generic.ListView):
    template_name = 'jobportal/index.html'
    context_object_name = 'latest_job_list'

    def get_queryset(self):
        return Job.objects.order_by('-pub_date')[:5]



#def index(request):
#    latest_job_list = Job.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.name for q in latest_jobs_list])
    #return HttpResponse(output)
    #return HttpResponse("hello")
    #template = loader.get_template('jobportal/index.html')
#    context = {
#        'latest_job_list': latest_job_list
#    }
    #return HttpResponse(template.render(context, request))
#    return render(request, 'jobportal/index.html', context)

class JobView(generic.DetailView):
    model = Job
    template_name = 'jobportal/job.html'
    #context_object_name = 'latest_job_list'

    #def get_queryset(self):
        #return Job.objects.order_by('-pub_date')[:5]


def employer(request, employer_id):
    #try:
    #    employer = Employer.objects.get(pk=employer_id)
    #except Employer.DoesNotExist:
    #    raise Http404("Employer does not exist")

    return render(request, 'jobportal/employer.html', {'employer':employer})

#def job(request, job_id):
    #try:
    #    job = Job.objects.get(pk=job_id)
    #except Job.DoesNotExist:
    #    raise Http404("Job does not exist")
#    job = get_object_or_404(Job, pk=job_id)
#    return render(request, 'jobportal/job.html', {'job':job})


#def apply(request, jobseeker_id):
#    jobseeker = get_object_or_404(Job, pk=jobseeker_id)

#    return HttpResponseRedirect(reverse('jobportal:job', args=()))
