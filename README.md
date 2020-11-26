# Adidas API Script :ok_hand:
Perfoms user auto subcription to perticular trainings if there are vacancies.

## How to use
Script is written in python so first of all you need to install the latest verison of python ***(python 3.9.0)***.
When you are done with installing python you need to run the script with arguments:
```
python3 training_url adidas_login adidas_password notify_email
```
* **training_url** - the link to training in adidas runners (e.g. [this](https://www.adidas.ru/adidasrunners/community/moscow/event/womens-run-189?cm_sp=RUNNING_HUB-_-LOGGEDIN-_-WOMENS-RUN-189))
* **adidas_login** - login of your account in adidas site
* **adidas_password** - password to your account
* **notify_email** - email where script will send the information about signing to event

The email will consist of status message and link to training in adidas runners which you provide in **training_url**.

## Cron for scheduling
If you would like to use cron for script scheduling the start command above does not change, but in crontab you need to add this line:
```
* * * * * python3 ~/path/to/script/main.py training_url adidas_login adidas_password notify_email >> ~/log/path/logs.log
```
Where ```>> ~/log/path/logs.log``` stands for logging which looking in log file similar to this:
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
But it is not necessary for run.

About ```* * * * *``` you can read in cron docs. (e.g. [here](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804-ru))