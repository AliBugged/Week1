from .forms import NoteForm
from django.shortcuts import redirect, render#импортируем функцию render для отображения шаблонов 
from .models import Note, Category  #импортируем модели из текущего приложения
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def note_list(request):
    category_id = request.GET.get('category')
    query = request.GET.get('q')

    notes = Note.objects.filter(user=request.user)
    categories = Category.objects.all()

    if category_id:
        notes = notes.filter(category_id=category_id)

    if query:
        notes = notes.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    return render(request, 'notes/note_list.html', {
        'notes': notes,
        'categories': categories,
        'query': query,
    })

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_update(request, note_id):#функция для обновление 
    note = get_object_or_404(Note, id=note_id, user=request.user)#получаем заметку по id если заметка не найдется то будет ошибка 404

    if request.method == 'POST':# если запрос был отправлен методом POST то мы обрабатываем данные формы 
        form = NoteForm(request.POST, instance=note)#создаю form и внутри него будут дааные которые были отправлены после того как он добавил форму также чтобы можно было обновлять существующие заметки нужен instance=note при помощи которого ты можем обновлять существующие заметки а не создавать новые 
        if form.is_valid():#если все ок то сохраняем изменения в базе данных
            note = form.save(commit=False)
            note.user = request.user
            form.save()#сохраняем изменения в базе данных
            return redirect('note_list')#после закидываем пользывателья на главную страницу со списком заметок 
    else:#если сразу в начале он зашел но не отправил или не сохранил что одно и тоже то мы просто отображаем форму с уже существующими данными заметки которую он хочет обновить
        form = NoteForm(instance=note)#тут уже не пустая форма а форма с данными которые уже есть в базе данных и которые он может изменить и сохранить 

    return render(request, 'notes/note_form.html', {'form': form})#тут как обычно от ображение шаблона note_form.html который нужен для отображения формы в главной странице и в зависимости от пустоты или заполненности формы он будет отображать пустую форму для создания новой заметки или заполненную форму для обновления существующей заметки

@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)

    if request.method == 'POST':
        note.delete()
        return redirect('note_list')

    return render(request, 'notes/note_confirm_delete.html', {'note': note})