# Newspaper Agency

Newspaper agency is a Django application for managing news, editors, and topics.

### **Features**

- View news (available to all users).
- Edit news (available only to editors and the superuser).
- Categorization by topics.
- Manage editors.

### **Getting started**

1. Clone the repository
```python
git clone https://github.com/yelizaveta-zh/newspaper-agency/
cd newspaper-agency
```

2. Create and activate a virtual environment

```python
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies
```python
pip install -r requirements.txt
```

4. Make and apply migrations
```python
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (to manage the admin panel)
```python
python manage.py createsuperuser
```

6. Run the server
```python
python manage.py runserver
```
7. Open in your browser

- Homepage: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/


### 📌 **Notes**

- Editors can create, edit, and delete news.
- Users can view news without logging in.
- Only the superuser has access to the admin panel.

![img.png](static/images/img.png)
