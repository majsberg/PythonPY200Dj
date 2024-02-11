from django import forms

class TemplateForm(forms.Form):
    bb_name = forms.CharField()
    bb_phone = forms.CharField(min_length=5, max_length=10, )
    bb_time = forms.TimeField()
    bb_branch = forms.ChoiceField(choices=(
        ("Grünberger", "Grünberger"),
        ("Behrenstraße", "Behrenstraße"),
        ("Weinbergsweg", "Weinbergsweg"),
    ))
    bb_date = forms.DateField()
    bb_number = forms.IntegerField()
    bb_message = forms.CharField(widget=forms.Textarea)