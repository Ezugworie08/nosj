import os
import json

# from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView, TemplateView

from app.forms import JSONUploadForm
# Create your views here.

# Based on my research, Python has this ultimate file MIME checker called "Magic"
# As this app grows in complexity and function, we'd consider that module.
# Also, to make life easier with sending message to the templates,
# I will move validation to the view
# With "magic",
# file_type = magic.from_buffer(file.read(), mime=True)
# file.seek(0)
# if not "JSON" in file_type:
#     raise ValidationError("File is not JSON")
# return file


class ProcessJSONForm(FormView):
    # To make life easier, we could use django braces
    # For message passing and other things.

    form_class = JSONUploadForm
    template_name = 'index.html'
    success_url = reverse_lazy('success')
    valid = False
    status_message = False
    data = []

    def form_valid(self, form):
        file = form.cleaned_data['file']
        extension = os.path.splitext(file.name)[1]
        if not extension == '.json':
            self.status_message = "This is not a JSON file, please upload a JSON file."
            return self.form_invalid(form)
        try:
            for chunk in file.chunks():
                self.data = json.loads(str(chunk, 'utf-8'))
        except (TypeError, ValueError) as e:
            print(e)
            self.status_message = "This file contains an invalid JSON string, please cross-check and re-upload!"
            return self.form_invalid(form)
        self.valid = True
        form.save(commit=True)
        return super(ProcessJSONForm, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProcessJSONForm, self).get_context_data(**kwargs)
        context['valid'] = self.valid
        context['status_message'] = self.status_message
        return context


class SuccessfulUpload(TemplateView):
    template_name = 'success.html'
