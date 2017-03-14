#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect, HttpResponse

from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
#from django.urls import reverse
from django.views import generic

from django.contrib.auth import authenticate, login, logout

from django.views.generic.edit import CreateView

from django.template import loader

from datetime import datetime

from django.conf import settings

#from django.utils.decorators import method_decorator
#from stronghold.decorators import public

from .models import User, Company, Job, JobApplication
from .forms import JobForm, UserForm, LoginForm

#def IndexView(ListView):
#    template_name = 'jobportal/index.html'


class IndexView(generic.ListView):
    template_name = 'jobportal/index.html'
    context_object_name = 'latest_job_list'

    #def get(self, request, *args, **kwargs):

    #@method_decorator(public)
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

class JobCreate(CreateView):
    model = Job
    #fields = ['name','cover_letter']
    fields = ['name']

class JobFormView(generic.View):
    form_class = JobForm
    template_name = 'jobportal/job_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # creates object from form but doesn't go into database
            job = form.save(commit=False)
            #job.pub_date = models.DateTimeField(default=datetime.now, blank=True)
            # cleaned (normalized) data
        #    pub_date =
            #job.pub
            job.save()

            return redirect('jobportal:index')

class UserFormView(generic.View):
    form_class = UserForm
    template_name = 'jobportal/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # creates object from form but doesn't go into database
            user = form.save(commit=False)
            #job.pub_date = models.DateTimeField(default=datetime.now, blank=True)
            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
        #    pub_date =
            #job.pub
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                # if user is not banned or made inactive
                if user.is_active:
                    login(request, user)

                    #to printout username do
                    #request.user.username

                    return redirect('jobportal:index')

        # if login failed
        return render(request, self.template_name, {'form':form})

class LoginFormView(generic.View):
    form_class = LoginForm
    template_name = 'jobportal/login_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        #if request.user.is_authenticated():
    #        return redirect('jobportal:index')
        #str("HELLO")
        #HttpResponse(str(var))

        #show_debug_toolbar(request)

        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        #form = self.form_class(request.POST)


        #str("HELLO")
        #if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            # if user is not banned or made inactive
            if user.is_active:
                login(request, user)
                return redirect('jobportal:index')
            #else:
                # return you are inactive

        # if login failed
        return render(request, self.template_name, {'form':form})

class LogoutView(generic.View):

    def get(self, request):
        logout(request)
        return redirect('jobportal:index')


def apply(request, jobseeker_id):
    job = get_object_or_404(Job, pk=job_id)

    return HttpResponseRedirect(reverse('jobportal:job', args=()))
