# Hierarchical_Data

The goal of this assignment is to learn about this type of database and different ways of working with it. Build a simple Django server that uses MPTT models from django-mptt to create a Dropbox-esque web interface where you can create "folders" and "files" in an arbitrary structure and then display that structure. We won't actually be uploading anything, just making model instances and using them to represent real data.

Files are created and able to be displayed in tree form in the admin panel. They are also draggable to rearrange them. The trees are displayed on the homepage.

## Installation

You may need to delete the migrations and db.sqlite3 file before running the server. If so, after deleting those files, run the following before starting the server:

```python
python manage.py makemigrations hierarchichal_data_app

python manage.py migrate
```

## Usage

```python
python manage.py runserver     # to run locally and click localhost link
```

## Contributing

Please do not submit pull requests for this project to make changes. This is part of a series of projects submitted as coursework.

## License

[MIT](https://choosealicense.com/licenses/mit/)
