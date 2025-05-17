# Django Blog Application

Simple blog application built using Django. It allows users to sign up, log in, create, edit, view, and delete articles. The platform supports tagging, publishing status, and searching for articles by title, content, or tags.

## Features

- User authentication (sign up, log in, log out)
- Create, read, update, and delete (CRUD) articles
- Article tags
- Article publishing (published/unpublished status)
- Author display on articles
- Responsive navigation with user greeting
- Search functionality to filter articles by title, content, or tags
- RESTful API for article access and management

## Technologies Used

- Python 3.13
- Django 5.2.1
- Django REST Framework
- HTML/CSS (Bootstrap for styling)
- SQLite

## Getting Started

### Prerequisites

- Python 3.10+
- pip
- Virtual environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/0then0/BlogDjango
   cd BlogDjango
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (admin):

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

Visit `http://127.0.0.1:8000/` in your browser to access the application.

## API Documentation

The project includes a basic RESTful API using Django REST Framework.

### Base URL

```
http://127.0.0.1:8000/api/
```

### Endpoints

| Method | Endpoint          | Description                 |
| ------ | ----------------- | --------------------------- |
| GET    | `/articles/`      | Retrieve a list of articles |
| GET    | `/articles/<id>/` | Retrieve a single article   |
| POST   | `/articles/`      | Create a new article        |
| PUT    | `/articles/<id>/` | Update an existing article  |
| DELETE | `/articles/<id>/` | Delete an article           |

### Example JSON Object

```json
{
	"title": "Example Article",
	"content": "This is an example article body.",
	"published": true,
	"tags": "news, updates"
}
```

### Authentication

Currently, the API is open or protected depending on how the project is configured. You can update permissions in `views.py` or add token-based authentication as needed.

## Notes

- Only authenticated users can create and edit articles.
- Users can only edit/delete their own articles unless they are staff.
- Search functionality is case-insensitive and supports partial matches.
