# Adidas Runners Events AutoSubcript :runner:
Perfoms user auto subcription to particular trainings if there are vacancies.

## How to use
Firstly, clone the repo in you machine.
> Script is written in python so first of all you need to install the latest verison of python ***(python 3.9.0)***.
```
git clone https://github.com/Vladislav504/adidas-api.git adidas_api
cd adidas_api
pip install -r requirements.txt
cd adidas_api
```
Secondly, you need to run the [main.py](/adidas_api/main.py) with arguments:
```
python3 main.py training_url adidas_login adidas_password notify_email
```
* **training_url** - the link to training in adidas runners (e.g. [this](https://www.adidas.ru/adidasrunners/community/moscow/event/womens-run-189?cm_sp=RUNNING_HUB-_-LOGGEDIN-_-WOMENS-RUN-189))
* **adidas_login** - login of your account in adidas site
* **adidas_password** - password to your account
* **notify_email** - email where script will send the information about signing to event

The email will consist of status message and link to training in adidas runners which you provide in **training_url**.

The script will response what has just happend. Where you get to know if the user was subscripted to event.
```
================================
The script is called with arguments: 
Event url: ---
Email: ---
Password: ---
Notify email: ---
User is signed up to event: False/True
================================
```

## Email settings
On order to use email notifications you should specify this parameters in [setting.py](/adidas_api/settings.py) file:
```python
# creds for emailling
sender_address = ''
sender_password = ''
smtp_host = ''
smtp_port = 465

```

## Cron for scheduling
If you would like to use cron for script scheduling for automation the run command above does not change, but in crontab you need to add this line:
```
* * * * * python3 ~/path/to/script/main.py training_url adidas_login adidas_password notify_email >> ~/log/path/logs.log
```
Where ```>> ~/log/path/logs.log``` stands for logging, but it is optional.

About ```* * * * *``` you can read in cron docs. (e.g. [here](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804-ru))