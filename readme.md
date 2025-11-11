# This project is for ISDN3000C Lab9

## Package Requirement
* `pip install -r requirement.txt` for download relative package.
* python 3.13, and all the package version is satisfied the python version.
 
## Folder introduction
ISDN3000C_LAB09_TEMPLATE.       # The father folder of all files 
├── FlaskApp/                   # Flask application folder
│   ├── app.py                  Coding 3 task(python code version)
│   ├── templates/
│   │   └── index.html          # Coding 3 task(javascript code version),Coding 4 task
│   │   └── movies.html         # Coding 2 task
│   └── database.db             # database
│   └── static/                 # Challenge task 
│   |   └──1.css                # test file
│   |   └──Profile.jpg          # test file
│   ├── schema.sql
|   |__ init_db.py
├── Dockerfile                  # Builds the  container, Coding 5 task
├── requirements.txt            
├── docker-compose.yml          # Orchestrates the containers
└── nginx/
│   └── nginx.conf              # Nginx configuration
├── questions.md
|__ readme.md
|__ .gitignore