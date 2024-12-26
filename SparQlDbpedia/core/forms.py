from django import forms

class SPARQLQueryForm(forms.Form):
    query = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 10, "cols": 80}),
        label="Votre requête SPARQL",
        required=True
    )