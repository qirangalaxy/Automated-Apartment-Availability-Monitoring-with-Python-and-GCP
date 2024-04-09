# :mailbox_with_mail:Automated Apartment Availability Monitoring with Python and Google Cloud Platform (GCP) 

A short description about the project and/or client.

## Extended Applications

Some ways you can generalize the automated monitoring system to:

* You need this
* And you need this
* Oh, and don't forget this

## Getting Started

The code itself is quite straightforward, consisting of only three simple functions. However, its complexity can vary significantly based on the intricacies of the web framework and your validation process. Meanwhile, the framework, highlighted details, and subsequent steps and solutions related to Google Cloud Platform (GCP) are where the true value lies. Hopefully, these aspects will provide valuable insights and guidance for your reference.

### Step1: Check Availability of Your Desired Room Type
```
def check_availability(url):
    import requests
    # implementation of common web scrapping e.g beautifulsoup
    response = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
```

Again, the code at this step is highly customized and should be adjusted accordingly, depending on the complexity of the web framework and the validation process. Also, different web scrapping techniques are available online, so I will not illustrate it in detail but focus more on how I explore and make use of the HTML structure.

```
    # find all room types and information related
    room_elements = soup.find_all('div', class_='suite__column')
    group_size = 7  # size for each group
    found_desired_room = False  # Boolean var used later
```

In this particular example, since my target url (https://www.drewloholdings.com/apartments-for-rent/rosecliffe-gardens-ii) has certain HTML structure where information about all room types contained in the class of "suite__column". Each room type consists of 7 elements separated by "suite__column" (refer the graph below), including a hyperlink of floorplan picture and the suite name, an optional link to a virtual tour, a string of "Bedrooms" and number of bedrooms the suite has, a string of "Baths" and number of baths it has, a string of "Sq.Ft." and value indicating the area, a string of "Rent" and the range, a string of "Availability" and a string of "not available".


```
    for i in range(0, len(room_elements), group_size):

        # make every group contains all information for one room type
        group = room_elements[i:i+group_size]

        # find room name by searching 
        link_element = group[1].find('a', class_='hyperlink-default floorplan-link')
        room_name = link_element.text.strip()

        # this is the name of my desired 1b room; you can add more names or modify the if statement for your own intention
        if room_name == 'Agnes':
            # get text underneath Availability: availability appears in the last element 
            availability_span = group[-1].find('span', class_='suite__field-title', string='Availability').find_next('span')
            availability_text = availability_span.text.strip()
            if availability_text == 'not available':
                return False
            else:
                found_desired_room = True  # find the desired room so that the boolean var turned to be True
                break  # once any desired room found just end the loop

    return found_desired_room

```

A for loop is used for checking every room, and if the name of the room equals to the name of your desired room, it will check for the text under the field "Availability" indicating whether it is "not available" or "inquiry today" (or any other changes). 

<img src = "https://github.com/qirangalaxy/Automated-Apartment-Availability-Monitoring-with-Python-and-GCP/assets/166411227/2d3aa2ff-1154-4fdc-a94f-4c21a076322c" width=30% height=30%>
<img src = "https://github.com/qirangalaxy/Automated-Apartment-Availability-Monitoring-with-Python-and-GCP/assets/166411227/2dbdb241-e2b2-48a5-926b-ba603301566c" width=25% height=30%>

### Step2: SMTP email sending settings
```
def send_email(sender_email, recipient_email, subject):
    import smtplib
    from email.mime.text import MIMEText

    # A clear subject is enough for my use so I don't need any body content; so just leave message inside MIMEText() as blank
    msg = MIMEText('')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # send email by connecting to server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_app_username', 'your_app_password')
        server.sendmail(sender_email, recipient_email, msg.as_string())
```

The second step performs the action of sending an automatic notification email with certain subject from a specified sender towards a specified recipient. The content of email is highly personalised; the number parameter inside smtplib.SMTP() is a common used submission port. More information regarding SMTP can be referred at https://docs.python.org/3/library/smtplib.html. 

If you don't know the app username and password for your email, a detailed instruction is provided below in "Potential Obstacles And Solutions".

### Step3: combine 1st and 2nd step and test if you can recieve an email!
```
def main():
    if check_availability("https://www.drewloholdings.com/apartments-for-rent/rosecliffe-gardens-ii"):
        send_email("qiran@gmail.com","qiran@gmail.com","Available 1b $14xx at Rosecliffe Gardens II")
```

The example code provided a webpage displaying the availability information for different types of rooms at a specific London apartment complex. Here, the sender and recipient email addresses are assigned to be both my email addresses for personal reminder (not my real email), which can be modified if you want to notify your friends or family about the update of rooms. 

## Workflows On GCP
1. After having the code, create google cloud scheduler first, including creation of a trigger (I used Pub/Sub).
2. Create a google cloud function
   2.1 Select the same trigger used for scheduler.
   2.2 Since this example used python for coding, select "Python" for Runtime.
   2.3 Copy and paste the main.py to main.py and requirements.txt (code provided below) to requirements.txt.
   2.4 Type "main" to Entry point because it is the first function the program starts with.
3. You can repeat the previous step to generate several functions and assign them to the same trigger; in this case, since webpages of all apartments from this real estate have similar web structures, a little revision to the main.py is needed to have different functions, allowing you to monitor desired rooms from several apartments at the same time.

## :clipboard:Suggestions Along the Way
* Most importantly, always check if scrapping certain websites is allowed; you can check either from robots.txt or using API instead.
* Before writing the python code, think fully the logic and break down the task into several key phases.
* Konwing the HTML structure well is the key to extract desired information.
* When you don't know how to set up parameters at GCP, just take time to read through necessary documents it provided, which are all pretty clear, just set besides each field.
* If you want to check if the code can be run successfully, you can search for the available room first and see if you get an email.
* Similarly, if you want to verify if you set up successful the scheduler with linked functions, perform checking availability for available rooms first and see if you get an email at scheduled time.
* Import libraries right before using it (as demostrated in the python code); this is a suggestion that I saw from a reddit comment.

## :construction:Potential Obstacles And Solutions
Here is a list of problems I faced and you might face during coding under local python and during Cloud Functions & Cloud Scheduler construction under GCP and actions I took to solve them.

### main.py: Can't find your gmail app username and password?
*Work under gmail settings, other email providers may have different steps to get username and password
```
#Take gmail as example
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
# requirements.txt
functions-framework==3.*
requests == 2.31.0
beautifulsoup4
```

## Additional Documentation and Acknowledgments
This GitHub post aims to share the process of combining Google Cloud Functions and Google Cloud Scheduler to automate Python code execution since during the development process, limited supporting materials or tutorials were available online. Therefore, the purpose of this post is to provide guidance on implementing Python automation with GCP, to inspire other creative and helpful solutions and to encourage its proper and ethical use only.
