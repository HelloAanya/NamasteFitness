from django.shortcuts import render

def yoga(request):
    context = {
        # You can add more context variables here if needed
    }
    return render(request, 'yoga.html')