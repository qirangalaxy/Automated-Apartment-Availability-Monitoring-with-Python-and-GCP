# :mailbox_with_mail:Automated Apartment Availability Monitoring with Python and GCP 

A short description about the project and/or client.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

The things you need before installing the software.

* You need this
* And you need this
* Oh, and don't forget this

### Installation

A step by step guide that will tell you how to get the development environment up and running.

```
$ First step
$ Another step
$ Final step
```

### Usage

A few examples of useful commands and/or tasks.

```
$ First example
$ Second example
$ And keep this in mind
```

### 3rd Step: combine 1st and 2nd step and perform 
```
def main():
    # The website address only used for illustration
    if check_availability("https://www.drewloholdings.com/apartments-for-rent/rosecliffe-gardens-ii"):
        send_email("qiran@gmail.com","qiran@gmail.com","Available Studio $13xx at LondonApartment")
```

## :clipboard:Suggestions Along the Way
1. Most importantly, always check if scrapping certain websites is allowed; you can check either from robots.txt or using API instead.
2. Before writing the python code, think fully the logic and break down the task into several key phases.
3. If you want to check if the code can be run successfully, you can search for the available room first and see if you get an email.
4. After having the code, create google cloud scheduler first, including creation of trigger (I used Pub/Sub), then generate google cloud functions where you select the consistent trigger used for scheduler.
5. When you don't know how to set up parameters at GCP, just take time to read through necessary documents it provided, which are all pretty clear, just set besides each field.
6. If you want to verify if you set up successful the scheduler with linked function, use the python code in suggestion[4] first and see if you get an email at scheduled time.
7. Import libraries right before using it (as demostrated in the python code); this is a suggestion that I saw from a reddit comment.

## :construction:Potential Obstacles And Solutions
Here is a list of problems I faced and you might face during coding under local python and during Cloud Functions & Cloud Scheduler construction under GCP and actions I took to solve them.

### main.py: Can't find your gmail app username and password?
*Work under gmail settings, other email providers may have different steps to get username and password
```
$Take gmail as example
with smtplib.SMTP('smtp.gmail.com', 587) as server:
  server.starttls()
  server.login('your_app_username', 'your_app_password')
  server.sendmail(sender_email, recipient_email, msg.as_string())
```
In default, gmail account does not have an app username or password ready to use; you can follow the steps to get your own set of username and auto-generated password:
1. Go to "Manage your Google Account";
2. On the top of the page, search "App Passwords";
3. Add a name for it and click create;
4. Copy and past the password into the code where "your_app_password" located;
5. The username I got is just the gmail name;

As listed on the site, Notice: App passwords are less secure than using up-to-date apps and services that use modern security standards.

### Google Cloud Functions: Fail to pass the test run?
* First thing first, always make sure codes in main.py works well under local environment and nothing wrong with the code; any subtle error will lead to failure
* Check if the "Entry point" is the first function/step your whole coding starts with; for example, here, you defined three functions, you should not just leave them there but add another code of main() to perform the whole task thus "Entry point" = main
* Check if all extra libraries and their versions are written under requirements.txt; Specifically under this apartment case, the version of beautifulsoup4 does not need to be specified as it works well when just leave it there thus it looks like:
```
functions-framework==3.*
requests == 2.31.0
beautifulsoup4
```

## Additional Documentation and Acknowledgments
This GitHub post aims to share the process of combining Google Cloud Functions and Google Cloud Scheduler to automate Python code execution since during the development process, limited supporting materials or tutorials were available online. Therefore, the purpose of this post is to provide guidance on implementing Python automation with GCP, to inspire other creative and helpful solutions and to encourage its proper and ethical use only.
