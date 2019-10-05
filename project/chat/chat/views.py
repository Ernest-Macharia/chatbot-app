import json

from django.views.generic.base import TemplateView

from django.views.generic import View

from django.http import JsonResponse

from chatterbot import ChatBot

from chatterbot.ext.django_chatterbot import settings

from django.shortcuts import render

from django.contrib.auth import login, authenticate

from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect

from.forms import SignUpForm,UserFeedbackForm


def index(request):

    return render(request,'bot.html')

def signup(request):

    if request.method == 'POST':

        form = SignUpForm(request.POST)

        if form.is_valid():

            form.save()

            username = form.cleaned_data.get('username')

            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)

            login(request, user)

            return redirect('main')
    else:
        
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


class ChatterBotAppView(TemplateView):

    template_name = 'app.html'


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.body.decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = self.chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })


def feedback_form(request):

    if request.method == 'POST':

        form = UserFeedbackForm(request.POST)
 
        if form.is_valid():

            form.save()

            return render(request, 'thanks.html')
    else:

        form = UserFeedbackForm()

    return render(request, 'feedbackform.html', {'form': form})
