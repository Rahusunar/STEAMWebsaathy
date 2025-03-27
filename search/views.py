# views.py
from django.shortcuts import render
from Shoolkit.models import kit

def search(request):
    query = request.GET.get('query', '')  # Default to empty if no query provided

    if query:
        allkits = kit.objects.filter(name__icontains=query)  # Filters by kit name (or you can add more fields)
    else:
        allkits = kit.objects.all()  # Show all if no query is given

    context = {'kit': allkits, 'query': query}  # Pass the kits and the query to the template
    return render(request, 'search.html', context)
