import logging

from apps.core import models as core_models
from django.urls import reverse
from django.shortcuts import redirect
from apps.web import forms
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import authenticate, login
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView, TemplateView
from apps.web.models import Lead

# Create your views here.

logger = logging.getLogger(__name__)


class RedirectToAppMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.company:
            return redirect(reverse("webapp"))
        return super().dispatch(request, *args, **kwargs)


class SoonTemplateView(RedirectToAppMixin, TemplateView):
    template_name = "pages/soon.html"


class CheckCompanyView(TemplateView):
    template_name = "auth/check_company.html"


class LoginView(FormView):
    form_class = forms.LoginForm
    template_name = "auth/login.html"
    success_url = "/app/"

    def dispatch(self, request, *args, **kwargs):
        if not self.request.company:
            return redirect(reverse("web:check-company"))

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]

        user = authenticate(self.request, email=email, password=password,)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)

        form.add_error("password", _("Invalid user or password"))
        return super().form_invalid(form)


class RegistrationView(TemplateView):
    template_name = "auth/signup.html"


class GetObjectByUUIDMixin:
    def get_object(self):
        return Lead.objects.get(secret=self.kwargs["pk"])


class SignUpStep1(FormView):
    template_name = "auth/signup/step1.html"
    form_class = forms.SignUpStep1Form
    success_url = reverse_lazy("web:signup-step-2")

    def form_valid(self, form):
        lead = Lead.objects.filter(
            email=form.cleaned_data.get("email")
        ).first()

        if not lead:
            form.save()
        else:
            form = self.form_class(instance=lead)

        form.send_email(self.request)
        return super().form_valid(form)


class SignUpStep2(TemplateView):
    template_name = "auth/signup/step2.html"


class SignUpStep3(GetObjectByUUIDMixin, UpdateView):
    template_name = "auth/signup/step3.html"
    model = Lead
    fields = ["company_name", "company_code"]

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            "web:signup-step-4", kwargs={"pk": self.kwargs["pk"]}
        )


class SignUpStep4(GetObjectByUUIDMixin, UpdateView):
    template_name = "auth/signup/step4.html"
    model = Lead
    fields = ["name", "position", "avatar"]
    success_url = reverse_lazy("web:signup-step-5")

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            "web:signup-step-5", kwargs={"pk": self.kwargs["pk"]}
        )


class SignUpStep5(GetObjectByUUIDMixin, UpdateView):
    template_name = "auth/signup/step5.html"
    model = Lead
    fields = ["invitations"]
    success_url = reverse_lazy("webapp")
