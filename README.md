# PROJECT
## GALERY

# AUTHOR
## By MURATHE


## USER STORIES
View my photos as posted.
Click on a single photo to expand it and also view the details of that specific photo. The photo details must appear on a modal within the same route as the main page.
Search for different categories of photos. (ie. HIking, code)
Copy a link to the photo to share with your friends.

# SetUp / Installation Requirements
0. Clone the repo by running:

`git clone https://github.com/Murathe/Galery.git`

0. Navigate to the project directory;

1. cd Gallery

1. Create a virtual environment and activate it
`python3 -m venv virtual`
`. virtual/bin/activate`

2. Create a database using postgress, type the following commands;
`$psql`

3. Then run the command to create a new database
`create database gallery`

4. Install dependencies
`pip install -r requirements.txt`

5. Create database migrations
`python3 manage.py makemigrations photoz`
`python3 manage.py migrate`

6. Run the app
`python3 manage.py runserver`

## TECHNOLOGIES USED
1. Django
4. Bootstrap
3. Postgres


## LICENCE
### MIT ©2019 Faith Gakori