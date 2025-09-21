from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from list.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": AdminDateWidget(
                attrs={"type": "datetime-local"},
            )
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"

