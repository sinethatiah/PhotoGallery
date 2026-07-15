# Photo Gallery

A Django web app for browsing, tagging, and reacting to photos. Users can register an account, manage a personal profile, browse the gallery, filter photos by tag, and like or dislike individual photos.


## Features

- User registration and login (Django's built-in authentication system)
- Profile page with editable bio and profile picture
- In-app password change
- Photo gallery homepage with tag-based filtering
- Photo detail view with like/dislike interactions
- Responsive UI built with Bootstrap 5

## Tech Stack

- **Backend:** Python 3, Django
- **Database:** PostgreSQL
- **Image storage:** Cloudinary
- **Frontend:** HTML, Bootstrap

## Project Structure

```
PhotoGallery/
├── galleryProject/        # Project settings, root URLs
├── galleryApp/             # Main app: models, views, forms, templates
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── photo_detail.html
│   │   └── registration/
│   │       ├── register.html
│   │       ├── login.html
│   │       ├── profile.html
│   │       └── password_change.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

## Models

- **Tag** — a reusable label attached to photos, used for filtering
- **Photo** — title, description, image, tags, upload timestamp
- **PhotoInteraction** — tracks a user's like/dislike on a given photo
- **Profile** — extends the built-in User model with a bio and profile picture

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sinethatiah/PhotoGallery.git
cd PhotoGallery
```

### 2. Create and activate a virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
SECRET_KEY=your_django_secret_key
DEBUG=True

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 5. Set up the database

Make sure PostgreSQL is running and the database in your `.env` exists, then:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

