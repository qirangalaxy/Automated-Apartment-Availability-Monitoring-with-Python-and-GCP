def check_availability(url):
    import requests
    response = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    # 找到所有房型信息的父元素
    room_elements = soup.find_all('div', class_='suite__column')
    group_size = 8  # 每个组的大小
    found_desired_room = False  # 标志变量，表示是否找到符合条件的房间
    for i in range(0, len(room_elements), group_size):
        group = room_elements[i:i+group_size]
        link_element = group[1].find('a', class_='hyperlink-default floorplan-link')
        room_name = link_element.text.strip()
        if room_name == 'Crossing':
            # 查找包含“Availability”标题的span标签
            availability_span = group[-1].find('span', class_='suite__field-title', string='Availability').find_next('span')
            availability_text = availability_span.text.strip()
            if availability_text == 'not available':
                return False
            else:
                found_desired_room = True  # 找到符合条件的房间，将标志变量设置为True
                break  # 找到满足条件的房间后停止循环

    return found_desired_room



def send_email(sender_email, recipient_email, subject):
    # 创建邮件内容
    import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText('')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    # 连接到邮件服务器并发送邮件
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('lala.zqrno1@gmail.com', 'wwjj iiyk woou ucbc')
        server.sendmail(sender_email, recipient_email, msg.as_string())

def main():
    if check_availability("https://www.drewloholdings.com/apartments-for-rent/rio"):
        send_email("lala.zqrno1@gmail.com","lala.zqrno1@gmail.com","Available Studio $13xx at SOUTH CARRIAGE PLACE")

main()
