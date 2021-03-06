Award
#### Author: [Rubyroy12](https://github.com/Rubyroy12) : 
## Description

As a user of the web application you will be able to:
1. Sign in with the application to start using.
2. Set up a profile about me and a general location and my neighborhood name.
3. Find a list of different businesses in my neighborhood.
4. Find Contact Information for the health department and Police authorities near my neighborhood.
5. Create Posts that will be visible to everyone in my neighborhood.
6. Change My neighborhood when I decide to move out.
7. Only view details of a single neighborhood.

## Setup and installations
* Clone Project to your machine
* Create a virtual environment uising `python3 -m venv venv`
* Activate a virtual environment on terminal: `source venv/bin/activate`
* Install all the requirements found in requirements file.
* On your terminal run `python3 manage.py runserver`
* Access the live site using the local host provided
  


### Prerequisites
* python3
* virtual environment
* pip
#### Clone the Repo and rename it to suit your needs.
bash
git clone https://github.com/Rubyroy12/neighbourinfo.git


#### Install dependancies
Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`
#### Make and run migrations
bash
- python3 manage.py check
- python3 manage.py makemigrations award 
- python3 manage.py migrate

#### Run the app
bash
python3 manage.py runserver

Open [localhost:5000](http://127.0.0.1:5000)
## Testing the Application
`python3.9 manager.py test`
## Built With
* [Python3.9](https://docs.python.org/3/)
* Django
* Boostrap
* HTML
* CSS
* git

## Live site 
- View [live]()

### Licence
This project is under the  [MIT](LICENSE.md) licence