import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from notes.models import Category, Note

@pytest.mark.django_db
def test_note_str_returns_title():
    user = User.objects.create_user(username='tester', password='Testpass12345')
    category = Category.objects.create(name='Test Category')
    note = Note.objects.create(
        user=user,
        title='My note',
        content='Hello',
        category=category
    )

    assert str(note) == 'My note'

@pytest.mark.django_db
def test_category_str_returns_name():
    category = Category.objects.create(name='Work')

    assert str(category) == 'Work'

@pytest.mark.django_db
def test_user_sees_only_own_notes(client):
    user1 = User.objects.create_user(username='user1', password='Testpass12345')
    user2 = User.objects.create_user(username='user2', password='Testpass12345')
    category = Category.objects.create(name='Work')

    Note.objects.create(
        user=user1,
        title='User 1 note',
        content='Hello from user1',
        category=category
    )

    Note.objects.create(
        user=user2,
        title='User 2 note',
        content='Hello from user2',
        category=category
    )

    client.login(username='user1', password='Testpass12345')

    response = client.get(reverse('note_list'))

    assert 'User 1 note' in response.content.decode()
    assert 'User 2 note' not in response.content.decode()

@pytest.mark.django_db
def test_note_list_requires_login(client):
    url = reverse('note_list')

    response = client.get(url)

    assert response.status_code == 302
    assert '/login/' in response.url

@pytest.mark.django_db
def test_create_note_sets_current_user(client):
    user = User.objects.create_user(username='creator', password='Testpass12345')
    category = Category.objects.create(user=user, name='Study')

    client.login(username='creator', password='Testpass12345')

    response = client.post(reverse('note_create'), {
        'title': 'New note',
        'content': 'New content',
        'category': category.id,
    })

    note = Note.objects.get(title='New note')

    assert response.status_code == 302
    assert note.user == user

@pytest.mark.django_db
def test_user_cannot_update_other_users_note(client):
    user1 = User.objects.create_user(username='owner', password='Testpass12345')
    user2 = User.objects.create_user(username='stranger', password='Testpass12345')
    category = Category.objects.create(name='Private')

    note = Note.objects.create(
        user=user1,
        title='Private note',
        content='Secret',
        category=category
    )

    client.login(username='stranger', password='Testpass12345')

    response = client.get(reverse('note_update', args=[note.id]))

    assert response.status_code == 404

@pytest.mark.django_db
def test_user_cannot_update_other_users_note(client):
    user1 = User.objects.create_user(username='owner', password='Testpass12345')
    user2 = User.objects.create_user(username='stranger', password='Testpass12345')
    category = Category.objects.create(name='Private')

    note = Note.objects.create(
        user=user1,
        title='Private note',
        content='Secret',
        category=category
    )

    client.login(username='stranger', password='Testpass12345')

    response = client.get(reverse('note_update', args=[note.id]))

    assert response.status_code == 404

@pytest.mark.django_db
def test_user_cannot_delete_other_users_note(client):
    user1 = User.objects.create_user(username='delete_owner', password='Testpass12345')
    user2 = User.objects.create_user(username='delete_stranger', password='Testpass12345')
    category = Category.objects.create(name='Private')

    note = Note.objects.create(
        user=user1,
        title='Private delete note',
        content='Secret',
        category=category
    )

    client.login(username='delete_stranger', password='Testpass12345')

    response = client.get(reverse('note_delete', args=[note.id]))

    assert response.status_code == 404