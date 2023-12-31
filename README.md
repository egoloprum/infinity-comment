# Infinite Nested Comments with Django

This Django code snippet implements a feature similar to Facebook's nested comments, allowing users to create an infinite hierarchy of comments in a threaded discussion style.

## Setup

The first thing to do is to clone the repository:

```
$ git clone https://github.com/egoloprum/infinity-comment.git
$ cd infinity-comment
```

Make sure you have Django installed. If not, install it using pip install django:

```python
pip install django
```

Apply Migrations:

```python
python manage.py makemigrations
python manage.py migrate
```

Once migration has finished, run the server:

```python
python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.

Visit the main page and use the comment form to create new comments.
You can reply to existing comments by clicking the "Reply" button associated with each comment.

## Note

- Customization: Adapt the code to fit your specific Django project structure and requirements. Customize the model, views, and templates as needed.

- Styling: Ensure that your HTML templates include proper styling to visually represent the nested comments. CSS styles for indentation or other visual cues can enhance the user experience.

- Testing: Thoroughly test the functionality to ensure that it behaves as expected, especially in scenarios with multiple levels of nested comments.

- Security: Implement proper user authentication and authorization mechanisms based on your application's requirements.

## Disclaimer
This code is provided as an example and may need modifications based on your specific project structure and requirements. Ensure that the code aligns with best practices and security considerations for your Django application.
