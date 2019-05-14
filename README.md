# An online bookstore “AlcoBookStore”.
An online bookstore “AlcoBookStore” is created with Python/Flask, Bootstrap, PostgreSQL, Flask-SQLAlchemy.
The website provides the next options for users:
1. To select a book from the entire list; 
2. To select a book from different category;
3. View a detail description for each book; 
4. View a description for each author; 
5. To comment books and authors; 
6. To order books; 
7. To register on the website; 
8. To create a profile, correct personal information and upload an avatar or photo in the account; 
9. To view personal order history. 
There are usual users and administrators on the website. For administrators the website provides options to add new books and authors, to manage orders and users.

# How to run project locally.
- Copy the project from Github.
- Create a virtual environment.
- Install software from requirements.txt: 
 pip install –r requirements.txt
- Install PostgreSQL and create a new data base.
- Add file "config.py" in the folder "webapp" of the project.
- add SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/db_name', SECRET_KEY='your_key', SQLALCHEMY_TRACK_MODIFICATIONS = False, REMEMBER_COOKIE_DURATION = timedelta(days=5), ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']), MAX_CONTENT_LENGTH = 16 * 1024 * 1024 in config.py.
- Open cmd and go to root of the project.
- Execute “python create_db”.
- Execute “python filling_bd”.
- Execute “chmod +x run.sh”
- Run command “./run.sh”

# Main page
![ScreenShot](https://github.com/DmPolikarpov/book_store/raw/master/screenshots/main_page.png)

# Category
![ScreenShot](https://github.com/DmPolikarpov/book_store/raw/master/screenshots/category.png)

# Books
![ScreenShot](https://github.com/DmPolikarpov/book_store/raw/master/screenshots/books.png)

# Cart
![ScreenShot](https://github.com/DmPolikarpov/book_store/raw/master/screenshots/cart.png)

# Profile
![ScreenShot](https://github.com/DmPolikarpov/book_store/raw/master/screenshots/profile.png)

