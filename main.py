import pandas
import smtplib
import datetime as dt

my_email = "subhojittest2@gmail.com"
password = "qtrwquzfbtnkqtpt"
receiver_email = "subhojit.test@yahoo.com"
msg = "Subject: Hello\n\nGood morning! How are you."

now = dt.datetime.now()
today = (now.day, now.month)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row["day"], row["month"]): row for (index, row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    print()
    with open("letter.txt", mode="r") as birthday_letter:
        message = birthday_letter.read()
    message_to_send = f"Subject: Happy birthday to you!\n\n{message.replace('[Name]', birthday_person['name'])}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=message_to_send)

#
# if now.weekday() == 4:
#     with open("quotes.txt", mode="r", encoding="utf8") as file:
#         all_quotes = file.readlines()
#         quote = random.choice(all_quotes)
#     with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs=reciever_email,
#                             msg=f"Subject: Monday Motivation\n\n{quote}".encode("utf8"))
