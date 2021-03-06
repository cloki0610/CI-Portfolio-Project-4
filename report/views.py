"""
REPORT APPLICATION VIEWS
"""
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from theme.forms import CommentForm
from theme.models import Theme
from .forms import ReportForm


class ReportView(LoginRequiredMixin, View):
    """ Return a form model to display report form """

    def get(self, request, slug):
        """ get method """
        # get the required form model and data
        report_form = ReportForm()
        theme = get_object_or_404(Theme, slug=slug)
        # return data with template
        return render(
            request,
            "report/report.html", {
                "theme": theme,
                "report_form": report_form
            }
        )

    def post(self, request, slug):
        """ post method """
        # get required form model and data
        theme = get_object_or_404(Theme, slug=slug)
        comments = theme.theme_comments.order_by('created_on')
        report_form = ReportForm(request.POST)
        # form validation
        if report_form.is_valid():
            report = report_form.save(commit=False)
            report.user = request.user
            report.theme = theme
            report.save()
            messages.success(request,
                             'Form submited, Thank you your report.')
        else:
            # if form object is invald
            # show error message and redirect to overview page
            messages.error(request,
                           'Submit failed, Please check and Try Again!')
            return HttpResponseRedirect(reverse('theme_overview',
                                        args=[theme.slug]))
        # return data with template
        return render(
            request,
            "theme/theme_overview.html",
            {
                "theme": theme,
                "comments": comments,
                "comment_form": CommentForm()
            },
        )
