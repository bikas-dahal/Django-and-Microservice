from django import forms 

# from news.producer import send_email_task_message 
from .tasks import send_email_task

class SuggestionForm(forms.Form):

    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    Suggestion = forms.CharField(widget=forms.Textarea, label='Suggestion')
    
    def send_email(self):
        send_email_task.delay(
            self.cleaned_data['name'],
            self.cleaned_data['email'],
            self.cleaned_data['Suggestion']
        )
    
    
# class SuggestionForm(forms.Form):

#     name = forms.CharField(max_length=100, label='Name')
#     email = forms.EmailField(label='Email')
#     Suggestion = forms.CharField(widget=forms.Textarea, label='Suggestion')
    
#     def send_email(self):
#         task_message = {
#             'name': self.cleaned_data['name'],
#             'email': self.cleaned_data['email'],
#             'suggestion': self.cleaned_data['Suggestion']
#         }
#         send_email_task_message(task_message)