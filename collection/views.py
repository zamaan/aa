from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.core.mail import EmailMessage, mail_admins
from django.template import Context
from collection.forms import ThingForm, ContactForm, ThingUploadForm
from collection.models import Thing, Upload




def index(request):
    things = Thing.objects.all()
    return render(request, 'index.html', {
        'things': things,
    })

    mail_admins("Our subject line","Our content")

def about(request):
    things=Thing.objects.all()
    social_accounts=thing.social_accounts.all()
    return render(request,'about.html',{
        'social_accounts':social_accounts,
        })


def contact(request):
	form_class=ContactForm
	if request.method == 'POST':
		form=form_class(data=request.POST)
		if form.is_valid():
				contact_name=form.cleaned_data['contact_name']
				contact_email=form.cleaned_data['contact_email']
				form_content=form.cleaned_data['content']
				template=get_template('contact_template.txt')

				context=Context({
					'contact_name':contact_name,
					'contact_email':contact_email,
					'form_content':form_content,
					})
				context=template.render(context)
				email=EmailMessage('New contact form submission',content, 'Your website <hi@rental.com>',['zamaan06@gmail.com'],
					headers= {'Reply-To':contact_email })
				email.send()
				return redirect('contact')
	return render(request,'contact.html',{'form':form_class})


def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    social_accounts = thing.social_accounts.all()

    uploads=thing.uploads.all()
    # and pass to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
        'uploads':uploads,
    })



@login_required

def edit_thing_uploads(request, slug):
	thing=Thing.objects.get(slug=slug)
	#if thing.user != request.user:
	#	raise Http404
	form_class = ThingUploadForm
	if request.method == 'POST':
		form=form_class(data=request.POST, files=request.FILES, instance=thing)
			
	#if form.is_valid():
		#Upload.objects.create(image=form.cleaned_data['image'],thing=thing,)
#return redirect('edit_thing_uploads', slug=thing.slug)
	#else:

	form=form_class(instance=thing)
	uploads=thing.uploads.all()

	return render(request, 'things/edit_thing_uploads.html',{
					'thing':thing,
					'form':form,
					'uploads':uploads,
	}
	)

def delete_upload(request,id):
    upload=Upload.objects.get(id=id)

    #if upload.thing.user != request.user:
     #   raise Http404

    upload.delete()

    return redirect('edit_thing_uploads',slug=upload.thing.slug)

def edit_thing(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    # grab the current logged in user and make sure they're the owner of the thing
    if thing.user != request.user:
        raise Http404

    # set the form we're using...
    form_class = ThingForm

    # if we're coming to this view from a submitted form,  
    if request.method == 'POST':
        # grab the data from the submitted form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)

    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    # and render the template
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })


def create_thing(request):
    form_class = ThingForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and apply to the form
        form = form_class(request.POST)

        if form.is_valid():
            # create an instance but do not save yet
            thing = form.save(commit=False)

            # set the additional details
            thing.user = request.user
            thing.slug = slugify(thing.name)

            # save the object
            thing.save()

            # redirect to our newly created thing
            return redirect('thing_detail', slug=thing.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'things/create_thing.html', {
        'form': form,
    })
