# LibraryProject

This Django project demonstrates **Custom User Models, Groups, and Permissions**.

## Project Structure

- `LibraryProject/` → Django project folder
- `bookshelf/` → App containing models, views, and custom user logic
- `manage.py` → Django management script
- `db.sqlite3` → SQLite database

### Custom User Model

- Model: `bookshelf.CustomUser` (extends `AbstractUser`)
- Additional fields:
  - `date_of_birth` (DateField)
  - `profile_photo` (ImageField)
- Configured in `settings.py`:

```python
AUTH_USER_MODEL = 'bookshelf.CustomUser'
```
