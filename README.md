# Adidas Runners Events AutoSubcript :runner:
Perfoms user auto subcription to particular trainings if there are vacancies.

## How to use
Firstly, clone the repo in you machine.
> Script is written in python so first of all you need to install the latest verison of python ***(python 3.6.9)***.
```
git clone https://github.com/Vladislav504/adidas-api.git adidas_api
cd adidas_api
python3 -m pip install -r requirements.txt
cd adidas_api
```
Secondly, make the json file for every user:
```
touch user1.json
```
edit it like this:
```json
{
    "email": "",
    "password": "",
    "notification email": ""
}
```
* **email** - login of your account in adidas site
* **password** - password to your account
* **notification email** - email where script will send the information about signing to

and run the [main.py](/adidas_api/main.py) with arguments:
```bash
python3 main.py training_url the_path_to_config_file
```
* **training_url** - the link to training in adidas runners (e.g. [this](https://www.adidas.ru/adidasrunners/community/moscow/event/womens-run-189?cm_sp=RUNNING_HUB-_-LOGGEDIN-_-WOMENS-RUN-189))
* **the_path_to_config_file** - path to your user1.json

The email will consist of status message and link to training in adidas runners which you provide in **training_url**.

The script will response what has just happend. Where you get to know if the user was subscripted to event.
```bash
================================
The script is called with arguments: 
Event url: --
Cred_path: --
User is signed up to event: False/True
================================
```
>## Warning!!
>If script managed to get response from api there will such message in command line about user subscription status like above, but if there is some issue with this the script will stuck in this position:
```bash
================================
The script is called with arguments: 
Event url: --
Cred_path: --
```
>It means that you are not able to get information from API. Such problem can appear when you use script at server. However from PC script should work.
## Email settings
On order to use email notifications you could install your own smtp server on machine or use external (e.g. gmail) and specify essential settings in [setting.py](/adidas_api/settings.py) file:
```python
# creds for emailling
sender_address = None
sender_password = None
smtp_host = ""
smtp_port = 25
ssl = False
tls = False
auth_required = False
```
Please use the free SMTP server (e.g. GMail) in place of your own. 
## Cron for scheduling
If you would like to use cron for script scheduling for automation the run command above does not change, but in crontab you need to add this line:
```bash
* * * * * python3 ~/path/to/script/main.py training_url the_path_to_config_file >> ~/log/path/logs.log
```
Where ```>> ~/log/path/logs.log``` stands for logging, but it is optional.
>If you use virtualenv then you should replace python3 with path to python3 file within you local environment.

About ```* * * * *``` you can read in cron docs. (e.g. [here](https://www.digitalocean.com/community/tutorials/how-to-use-cron-to-automate-tasks-ubuntu-1804-ru))