# EGME

# DJANGO SHOPPING WEBSITE


A complete shopping website , using django , html , css , made under Codebinary Initiative , where you can buy Tshirts .

Download/clone the code

Go to the directory of the code, and open the folder EGME-master

Follow the steps:-

$ cd EGME

$ pip3 install -r requirements.txt  
(or do a sudo , if above doesn't work)

$ source venv/bin/activate

$ cd shop

$ python3 manage.py runserver

Then open http://127.0.0.1:8000/  ( You might face some email SMTP error, that's because the email login details in the setttings.py is outdated, you can change the email and password for your own use. )

First of all create an account , *then login* ( YOU HAVE TO BE LOGGED IN TO VIEW SHOP PAGE ), then you will be redirected to add address page. 
 
 Or go to http://127.0.0.1:8000/nav/
 
Add address to continue to the Tshirts section ,then select sizes to view Tshirts.

You can add Tshirts by going http://127.0.0.1:8000/additem , but you will need admin rights to do it , so first create a superuser .
Then you can view cart, and order by cod .
