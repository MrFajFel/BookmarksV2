from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from images.form import ImageCreateForm


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.changed_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            return redirect(new_image.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request,'images/image/create.html',{'form':form,'section':'images'})
# Create your views here.
