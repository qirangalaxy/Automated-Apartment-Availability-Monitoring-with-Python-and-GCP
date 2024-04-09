def check_availability(url):
    import requests
    response = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # find all room types and information related
    room_elements = soup.find_all('div', class_='suite__column')
    group_size = 8  # size for each group
    found_desired_room = False  # Boolean var used later
    for i in range(0, len(room_elements), group_size):
        group = room_elements[i:i+group_size]
        link_element = group[1].find('a', class_='hyperlink-default floorplan-link')
        room_name = link_element.text.strip()
        # this is the name of my desired 1b room
        if room_name == 'Agnes':
            # check text after "Availability" is "not available" or "inquire today"/other
            availability_span = group[-1].find('span', class_='suite__field-title', string='Availability').find_next('span')
            availability_text = availability_span.text.strip()
            if availability_text == 'not available':
                return False
            else:
                found_desired_room = True  # find the desired room so that the boolean var turned to be True
                break  # once any desired room found just end the loop

    return found_desired_room



def send_email(sender_email, recipient_email, subject):
    # Create email content
    import smtplib
    from email.mime.text import MIMEText
    # The 
    msg = MIMEText('')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    # Connect with gmail (can be any email) server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_app_username', 'your_app_password')
        server.sendmail(sender_email, recipient_email, msg.as_string())

def main():
    # The website address only used for illustration
    if check_availability("https://www.drewloholdings.com/apartments-for-rent/rosecliffe-gardens-ii"):
        send_email("qiran@gmail.com","qiran@gmail.com","Available Studio $13xx at LondonApartment")

main()
