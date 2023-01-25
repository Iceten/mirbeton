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
                return render(request, 'antony/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/index.html', context=context)


def pageServices(request):
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
                return render(request, 'antony/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/all-services.html', context=context)


def pageArticles(request):
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
                return render(request, 'antony/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/all-articles.html', context=context)

# --------------------------  GDPR Pages -------------


def mentions_lega(request):
    return render(request, 'antony/mentions-legales.html')


def politique_conf(request):
    return render(request, 'antony/politique-de-confidentialite.html')


def politique_cook(request):
    return render(request, 'antony/politique-de-cookies.html')

# --------------------------  Services Pages -------------


def pageService_1(request):
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
                return render(request, 'antony/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-1.html', context=context)


def pageServiceBordureBeton(request):
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
                return render(request, 'antony/service-beton-bordure.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-beton-bordure.html', context=context)


def pageServiceBetonCire(request):
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
                return render(request, 'antony/service-beton-cire.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-beton-cire.html', context=context)


def pageServiceDalleBeton(request):
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
                return render(request, 'antony/service-beton-dalle.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-beton-dalle.html', context=context)


def pageServiceBetonDecoratif(request):
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
                return render(request, 'antony/service-beton-decoratif.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-beton-decoratif.html', context=context)


def pageServiceBetonDesactive(request):
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
                return render(request, 'antony/service-beton-desactive.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-beton-desactive.html', context=context)


def pageServiceBetonImprime(request):
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
                return render(request, 'antony/service-beton-imprime.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-beton-imprime.html', context=context)


def pageServiceBitumeEnrobe(request):
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
                return render(request, 'antony/service-bitume.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-bitume.html', context=context)


def pageServiceCoulageFondation(request):
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
                return render(request, 'antony/service-fondation.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-fondation.html', context=context)


def pageServicePavageDallage(request):
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
                return render(request, 'antony/service-pavage.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-pavage.html', context=context)


def pageServiceResineEpoxy(request):
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
                return render(request, 'antony/service-resine-sol-epoxy.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-resine-sol-epoxy.html', context=context)


def pageServiceGresCerame(request):
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
                return render(request, 'antony/service-terrasse-gres-cerame.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-terrasse-gres-cerame.html', context=context)


def pageServicePierreNaturelle(request):
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
                return render(request, 'antony/service-terrasse-pierre-naturelle.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/service-terrasse-pierre-naturelle.html', context=context)


# -------------------------- Articles Pages -------------
def pageArticle_1(request):
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
                return render(request, 'antony/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'antony/article-1.html', context=context)
# --------------------------  Thank You Pages -------------


def thankYouAntony(request):
    return render(request, 'antony/index-thank-you.html')


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
    work_type = form.cleaned_data['work_type']
    surface = form.cleaned_data['surface']

    try:
        email = form.cleaned_data['email']
    except:
        email = 'INVALID EMAIL'

    sentence = 'Here is your new lead for MIR Béton - Antony\n' + 'First Name: ' + first_name + '\n' + 'Last Name: ' + last_name + '\n' + \
        'Email: ' + email + '\n' + 'Phone: ' + phone + '\n' + \
        'Zip Code: ' + zipcode + '\n' + 'Work Type: ' + work_type + '\n' + \
        'Surface: ' + surface + '\n' + 'IP Address: ' + remote_ip

    send_mail('New Consult Lead From MIR Couverture Antony!', sentence, from_email=settings.EMAIL_HOST_USER,
              recipient_list=[settings.ADMIN_EMAIL], fail_silently=False)
