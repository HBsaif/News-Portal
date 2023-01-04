#News-Portal

1. Two different layouts for normal viewers and managers.
2. Managers can add, delete or edit news. But normal users can only view the news.
3. The news is arranged using diffetent types of categories.
4. The forntend is designed using HTML, CSS, Bootstrap and Javascript.
5. The backend is developed with Django framework of Python.



RUN PROJECT:
	1. Keep the folder named "myNews" on "Desktop" 
	2. Go to command prompt and run (3) and (4)
	3. cd Desktop/myNews
	4. python manage.py runserver
	5. go to URL : http://127.0.0.1:8000/



Admin Page URL:
	http://127.0.0.1:8000/panel/



Superuser:
	username : Admin
	password : Admin#12345

Normal Manager:
	username : Clay
	password : Mypass#123



If any MODEL changes :
	1. python manage.py makemigrations
	2. python manage.py migrate
