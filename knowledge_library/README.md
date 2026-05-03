# Knowledge Archive

Knowledge Archive is a Django web application for storing personal notes and study records.

## Features

- User registration, login and logout
- Create, read, update and delete notes
- Notes are private for each user
- Users cannot edit or delete other users' notes
- Search notes by title or content
- Filter notes by category
- Dark archive-style interface
- Pytest tests for core logic and permissions

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Pytest
- pytest-django

## Tests

The project includes tests for:

- Note string representation
- Category string representation
- User ownership
- Login required access
- Note creation owner assignment
- Update permission protection
- Delete permission protection

Run tests:

```bash
pytest