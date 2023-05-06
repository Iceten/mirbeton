from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.core.mail import send_mail
from django.conf import settings
# , SubscriberNewsletterForm, SubscriberNewsletterForm2, LeadContactForm
from .forms import LeadConsultForm


def indexPoitiers(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/index.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/all-services.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/all-articles.html', context=context)

# --------------------------  GDPR Pages -------------


def mentions_lega(request):
    return render(request, 'poitiers/mentions_legales.html')


def politique_conf(request):
    return render(request, 'poitiers/politique_de_confidentialite.html')


def politique_cook(request):
    return render(request, 'poitiers/politique_de_cookies.html')

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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-1.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-beton-bordure.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-beton-bordure.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-beton-cire.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-beton-cire.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-beton-dalle.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-beton-dalle.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-beton-decoratif.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-beton-decoratif.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-beton-desactive.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-beton-desactive.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-beton-imprime.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-beton-imprime.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-bitume.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-bitume.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-fondation.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-fondation.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-pavage.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-pavage.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-resine-sol-epoxy.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-resine-sol-epoxy.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-terrasse-gres-cerame.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-terrasse-gres-cerame.html', context=context)


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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-terrasse-pierre-naturelle.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-terrasse-pierre-naturelle.html', context=context)


def pageServicePierreNaturelleGresCerame(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-terrasse-pierre-naturelle-gres-cerame.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-terrasse-pierre-naturelle-gres-cerame.html', context=context)


def pageServiceAmenagementExterieur(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-amenagement-exterieur.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-amenagement-exterieur.html', context=context)


def pageServiceTerrasseBois(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-terrasse-bois.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-terrasse-bois.html', context=context)


def pageServiceTravauxSecondOeuvre(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-travaux-second-oeuvre.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-travaux-second-oeuvre.html', context=context)


def pageServiceTravauxGrosOeuvre(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-travaux-gros-oeuvre.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-travaux-gros-oeuvre.html', context=context)


def pageServiceTerrasseCarrelage(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-terrasse-carrelage.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-terrasse-carrelage.html', context=context)


def pageServiceTerrasseAlleePavee(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-terrasse-allee-pavee.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-terrasse-allee-pavee.html', context=context)


def pageServiceTerrasseBetonPierre(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-terrasse-beton-pierre.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-terrasse-beton-pierre.html', context=context)


def pageServiceEntreeGarage(request):
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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/service-entree-garage.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/service-entree-garage.html', context=context)

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
                return redirect('/poitiers/thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/index.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/article-1.html', context=context)
# --------------------------  Thank You Pages -------------


def thankYouPoitiers(request):
    return render(request, 'poitiers/index-thank-you.html')


def thankYouPoitiersPromotionDuPrintemps(request):
    return render(request, 'poitiers/promotion-du-printemps-thank-you.html')

# --------------------------  Promotion Pages -------------


def pagePoitiersPromotionDuPrintemps(request):
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
                return redirect('/poitiers/promotion-du-printemps-thank-you/')

            else:
                print('ERROR FORM INVALID')
                print('Form is not saved in db')
                print(form)
                print('\n')
                print(form.cleaned_data)
                return render(request, 'poitiers/promotion-du-printemps.html', context=context)
    else:
        print('NOT in request POST')
        return render(request, 'poitiers/promotion-du-printemps.html', context=context)

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

    sentence = 'Here is your new lead for MIR Béton - Poitiers\n' + 'First Name: ' + first_name + '\n' + 'Last Name: ' + last_name + '\n' + \
        'Email: ' + email + '\n' + 'Phone: ' + phone + '\n' + \
        'Zip Code: ' + zipcode + '\n' + 'Work Type: ' + work_type + '\n' + \
        'Surface: ' + surface + '\n' + 'IP Address: ' + remote_ip

    send_mail('New Consult Lead From MIR Beton Poitiers!', sentence, from_email=settings.EMAIL_HOST_USER,
              recipient_list=[settings.ADMIN_EMAIL], fail_silently=False)
