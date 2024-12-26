from django.shortcuts import render
from SPARQLWrapper import SPARQLWrapper, JSON
from .forms import SPARQLQueryForm

def query_dbpedia(request):
    form = SPARQLQueryForm()

    if request.method == "POST":
        form = SPARQLQueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            endpoint = "https://dbpedia.org/sparql"
            sparql = SPARQLWrapper(endpoint)
            sparql.setQuery(query)
            sparql.setReturnFormat(JSON)

            try:
                # Exécution de la requête SPARQL
                results = sparql.query().convert()
                bindings = results.get("results", {}).get("bindings", [])

                # Si des résultats sont trouvés
                if bindings:
                    results_list = [
                        {variable: value["value"] for variable, value in result.items()}
                        for result in bindings
                    ]
                    return render(request, "index.html", {"results": results_list, "form": form})
                else:
                    return render(request, "index.html", {"error": "Aucun résultat trouvé.", "form": form})

            except Exception as e:
                # Gestion des erreurs
                return render(request, "index.html", {"error": f"Erreur lors de l'exécution de la requête : {str(e)}", "form": form})

    return render(request, "index.html", {"form": form})
