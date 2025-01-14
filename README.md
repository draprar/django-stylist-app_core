# Hair Stylist Webpage Django Application

![Screenshot](media/Screenshot_1.png)
![Screenshot](media/Screenshot_2.png)
![Screenshot](media/Screenshot_3.png)
![Screenshot](media/Screenshot_4.png)

This is a Django-based application for a hair stylist service. The app allows clients to book appointments, view testimonials, and browse a gallery of images.

## Setup Instructions

1. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies:
   ```
   pip install django
   ```

3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

5. Access the application at `http://127.0.0.1:8000/`.