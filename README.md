# QRCodeGenerator
A simple app in django which you can use to generate QR codes for your data

to use the app simply visit here and enter your data - http://qcodesn.herokuapp.com/

To download the project right on your computer Download the zip file

Create a virtualenv using 
<pre>virtualenv -p python3 venv</pre>

From Home Directory run command

<pre>pip install -r requirements.txt</pre>
then run
<pre>
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
python manage.py runserver</pre>

