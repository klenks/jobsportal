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

from django.contrib.auth.models import User
#user = User.objects.get(id=user_id)

from .models import Company, Job, JobApplication, Resume, Person
from .forms import JobForm, UserForm, LoginForm, ResumeForm

#from django.contrib.auth.models import User

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

            # TODO i dont know if this should go here or after user.is_active, IDK what that code is doing there. how can save work if let's say it was a duplicate account
            Person.objects.create(user=user, name=username)

            user = authenticate(username=username, password=password)

            if user is not None:
                # if user is not banned or made inactive
                if user.is_active:

                    login(request, user)

                    #to printout username do
                    #request.user.username

                    return redirect('jobportal:control-panel')

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

        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(username=username, password=password)
        #print("ASASH"+user)
        if user is not None:
            # if user is not banned or made inactive
            if user.is_active:
                login(request, user)

                #to printout username do
                #request.user.username

                return redirect('jobportal:control-panel')

        # if login failed
        return render(request, self.template_name, {'form':form})

class MyResumesView(generic.ListView):
    #def __init__(self, *args, **kwargs):
        # you take the user out of kwargs and store it as a class attribute
    #    self.user = kwargs.pop('user', None)
    #    super(MyResumesView, self).__init__(*args, **kwargs)

    #form_class = ResumeForm

    context_object_name = 'my-resumes-list'
    template_name = 'jobportal/my_resumes.html'

    #def get_context_data(self, **kwargs):
    #    context = super(MyResumesView, self).get_context_data(**kwargs)
    #    context["userr"] = self.request.user
    #    return context

    def get_queryset(self):
        print(type(self.request.user))
        print(self.request.user)
        #print(Resume.objects.filter(user=self.request.user))
        print("s")
        return Resume.objects.filter(owner=Person.objects.get(user=self.request.user))
        #return Resume.objects.filter(user=User.objects.filter(name=self.request.user))

class ResumeFormView(generic.CreateView):
    form_class = ResumeForm
    template_name = 'jobportal/resume_upload_form.html'

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
        form = self.form_class(request.POST)


        if form.is_valid():
            # creates object from form but doesn't go into database
            resume = form.save(commit=False)
            #job.pub_date = models.DateTimeField(default=datetime.now, blank=True)
            # cleaned (normalized) data
            #username = form.cleaned_data['username']
            #password = form.cleaned_data['password']
            #user.set_password(password)
            resume.resume_file = form.cleaned_data['resume_file']
        #    pub_date =
            #job.pub
            resume.save()

            return redirect('jobportal:my-resumes')
            #else:
                # return you are inactive

        # if login failed
        return render(request, self.template_name, {'form':form})

class LogoutView(generic.View):

    def get(self, request):
        logout(request)
        return redirect('jobportal:index')

class ControlPanelView(generic.View):
    #model = User
    template_name = 'jobportal/control_panel.html'

    def get(self, request):
        #form = self.form_class(None)
        return render(request, self.template_name)



def apply(request, jobseeker_id):
    job = get_object_or_404(Job, pk=job_id)

    return HttpResponseRedirect(reverse('jobportal:job', args=()))
