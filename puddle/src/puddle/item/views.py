from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from .models import Category, Item

#view for detail page
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })



#view for Browse page
def items(request):
	query = request.GET.get('query', '')
	category_id = request.GET.get('category', 0)
	categories = Category.objects.all()
	items = Item.objects.filter(is_sold=False)

	if category_id:
	    items = items.filter(category_id=category_id)

	if query:
		items = items.filter(Q(name__icontains=query)| Q(description__icontains=query))

	return render(request, 'item/items.html', {
		'items': items,
		'query': query,
		'categories': categories,
		'category_id': int(category_id)
	})


# Create your views here.
# def detail(request, pk):
# 	item = get_object_or_404(Item, pk=pk) #if the items is not found in the db, 'get_object_or_404()' an error
# 	related_items = Item.objects.filter(category=item.Category, is_sold=False).exclude(pk=pk)[0:3] 

# 	return render(request, 'item/detail.html', {
#         'item': item,
#         'related_items': related_items
#     })



@login_required
def new_item(request):
	if request.method == 'POST':
    	#request,files get the files uploaded by the user
		form = NewItemForm(request.POST, request.FILES)
		if form.is_valid():
    #when i put commit= false it will the not save the object to the database for now
			item = form.save(commit=False)
			item.created_by = request.user
			item.save()
    #redirecting the user to the product which he created
			return redirect('item:detail', pk=item.id)
	else:
		form = NewItemForm()
	 
	return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

# @login_required
# def edit_item(request,pk):
# 	item = get_object_or_404(Item, pk=pk, created_by=request.user)
# 	if request.method == 'POST':
# 		form = EditItemForm(request.POST, request.FILES, instance=item)
# 		if form.is_valid():
# 			item = form.save(commit=False)
# 			item.created_by = request.user
# 			item.save()
# 			return redirect('item:detail', pk=item.id)
# 	else:
# 		form = EditItemForm()
	 
# 	return render(request, 'item/form.html',{
# 		'form': form
# 	})

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })


@login_required
def delete(request, pk):
	item = get_object_or_404(Item, pk=pk, created_by=request.user)
	item.delete()

	return redirect('dashboard:index')
