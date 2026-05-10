from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import WordForm
from .models import Word


@login_required
def user_dashboard(request):
    words = Word.objects.filter(created_by=request.user).order_by('-created_at')

    return render(request, 'dashboard/user_dashboard.html', {
        'words': words
    })


@login_required
def add_word(request):
    if request.method == 'POST':
        form = WordForm(request.POST)

        if form.is_valid():
            word = form.save(commit=False)
            word.created_by = request.user
            word.is_approved = False
            word.save()

            messages.success(
                request,
                'Word submitted successfully. It is waiting for admin approval.'
            )
            return redirect('user_dashboard')
    else:
        form = WordForm()

    return render(request, 'dashboard/add_word.html', {
        'form': form
    })