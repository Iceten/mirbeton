from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.core.mail import send_mail
from django.conf import settings
# , SubscriberNewsletterForm, SubscriberNewsletterForm2, LeadContactForm
from .forms import LeadConsultForm


def indexAntony(request):
    newLead = LeadConsultForm()
    context = {
        'lead_form': newLead,
    }

    if request.method == 'POST':
        print('in request POST')
        if 'lead_consult_form' in request.POST:
            print('in lead_consult_form')
            # We populate the form with previous index page entry
            form = LeadConsultForm(request.POST)

            if form.is_valid():
                print('in form.is_valid')
                print('first sending notification e-mail')
                send_email_lead_consult(form, request.META)
                print('Saving now in DB...')
                myform = form.save(commit=True)
                # sending notification to admin
                print(myform)
                print(form.cleaned_data)
                # return render(request, 'siteMain/index_thank_you.html', context=context)
                return redirect('/antony/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'antony/index-antony.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/index-antony.html', context=context)


def isolationAntony(request):
    newLead = LeadConsultForm()
    context = {
        'lead_form': newLead,
    }

    if request.method == 'POST':
        print('in request POST')
        if 'lead_consult_form' in request.POST:
            print('in lead_consult_form')
            # We populate the form with previous index page entry
            form = LeadConsultForm(request.POST)

            if form.is_valid():
                print('in form.is_valid')
                print('first sending notification e-mail')
                send_email_lead_consult(form, request.META)
                print('Saving now in DB...')
                myform = form.save(commit=True)
                # sending notification to admin
                print(myform)
                print(form.cleaned_data)
                # return render(request, 'siteMain/index_thank_you.html', context=context)
                return redirect('/antony/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'antony/isolation-thermique-antony.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/isolation-thermique-antony.html', context=context)


def mentions_lega(request):
    return render(request, 'antony/mentions-legales.html')


def politique_conf(request):
    return render(request, 'antony/politique-de-confidentialite.html')


def politique_cook(request):
    return render(request, 'antony/politique-de-cookies.html')


# --------------------------  Thank You Pages -------------
def thankYouAntony(request):
    return render(request, 'antony/thank-you-antony.html')


#------------------------------ Send E-mail Functions  ----------------------------------#
def send_email_lead_consult(form, http_header):
    try:
        if http_header.get('HTTP_X_REAL_IP'):
            remote_ip = http_header.get('HTTP_X_REAL_IP')
        elif http_header.get('X-FORWARDED-FOR'):
            http_header.get('X-FORWARDED-FOR')
        else:
            remote_ip = 'We were not able to fetch IP Address of client'
    except:
        pass

    first_name = form.cleaned_data['first_name']
    last_name = form.cleaned_data['last_name']
    phone = form.cleaned_data['phone']
    zipcode = form.cleaned_data['zipcode']

    try:
        email = form.cleaned_data['email']
    except:
        email = 'INVALID EMAIL'

    sentence = 'Here is your new lead for MIR Couverture - Antony\n' + 'First Name: ' + first_name + '\n' + 'Last Name: ' + last_name + '\n' + \
        'Email: ' + email + '\n' + 'Phone: ' + phone + '\n' + \
        'Zip Code: ' + zipcode + '\n' + 'IP Address: ' + remote_ip

    send_mail('New Consult Lead From MIR Couverture Antony!', sentence, from_email=settings.EMAIL_HOST_USER,
              recipient_list=[settings.ADMIN_EMAIL], fail_silently=False)
