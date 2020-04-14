## Internship Web Crawler: User Guide

Team Name: Team Nougat

Team Members: Emma Rivera, Neal Goyal, and Sydney Pun 

__Dependencies:__ 
- BeautifulSoup (bs4)
- Requests   
- urlparse

__How to Run the Web Application:__
- Enter the project folder: 
```python
cd web_app
```
- Enter the Virtual Environment by running: 
```python
env/Scripts/Activate.ps1
```
- Install the requirements.txt file by running: 
```python
pip install -r requirements.txt
```
- Run the next few commands into your terminal to run the project files: 
```python
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
- Finally, to view this project visit: 
```python
  http://127.0.0.1:8000/
```
__Possible VSCODE Errors:__

If you are running this project on VSCODE, here are some tips to overcome the errors that may arise. 

- If you receive a "running scripts is disabled on this system error", after typing in "env/Scripts/Activate.ps1", resolve this issue by typing in: 
```python
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
env/Scripts/Activate/ps1
``` 
- If you receive a "Django class has no objects error", to resolve this issue, type in:
```python
 pip install pylint-django
 ```
