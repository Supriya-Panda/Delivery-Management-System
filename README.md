# Delivery-Management-System

# Run the applications
cd Delivery-Management-System 

1. Set Up Virtual Environment
python3 -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows

3. Install Dependencies
pip install django djangorestframework 

4.  Inside Application folder ;already  Migrations done
cd delivery_system 

5. Superuser credentials
  id :- admin
  password:- supriya@123

6. Run the Development Server
python manage.py runserver
Now visit: http://127.0.0.1:8000/admin/ to log in to the Django admin.
For agents:
http://127.0.0.1:8000/agents/check-in/1/
For dispatch Compliance report:
http://127.0.0.1:8000/dispatch/compliance-report/