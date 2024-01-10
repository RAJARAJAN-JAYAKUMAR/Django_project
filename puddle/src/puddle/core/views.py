# from django.shortcuts import render, redirect

# from item.models import Category,Item

# from .forms import SignupForm

# from django.contrib.auth.decorators import login_required

# # Create your views here.
# @login_required
# def index(request):
#     # items = Item.objects.all() you can use this too unless you need any filtered objects
#     items = Item.objects.filter(is_sold=False)[0:6]
#     categories = Category.objects.all()
#     # print(f"Number of items: {len(items)}")
#     # print(f"Number of categories: {len(categories)}")
#     context = {
#         "categories":categories,
#         "items":items,
#     }
#     return render(request, 'core/index.html',context)

# def contact(request):
#     return render(request, 'core/contact.html')

# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/login/')
#     else:
#         form = SignupForm()
#     return render(request, 'core/signup.html', {
#         'form': form
#     })

from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

# def front(request):
#     return render(request,'core/front.html',{})

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):  
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })
    
def logout(request):
    return render(request, 'core/logout.html')
    