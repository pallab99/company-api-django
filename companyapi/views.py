

from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("This is the home page")
    fruits = ["mango", "apple", "orange"]

    return JsonResponse(dict(fruits=fruits), safe=False)
