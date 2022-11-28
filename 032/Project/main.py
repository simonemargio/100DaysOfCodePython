import smtplib
import random
import pandas
import datetime as dt

email = "your_email_here"
password = "your_password_email_here"


def random_quote():
    with open("quotes.txt", mode="r") as file:
        data = file.read().splitlines()
        quote = random.choice(data)
    return quote


def random_letter(receiver):
    n_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{n_letter}.txt") as file:
        standard_letter = file.read()
        letter = standard_letter.replace('[NAME]', str(receiver))
        quote = random_quote()
        letter += "\n\n" + quote
        return letter


def send_email(receiver, letter):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=receiver,
            msg=f"Subject:Hey :)\n\n{letter}")


current_date_time = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")

for (index, row) in data.iterrows():
    if current_date_time.month == row.month and current_date_time.day == row.day:
        name_receiver = row.receiver
        email_receiver = row.email
        letter = random_letter(name_receiver)
        print(f"Send email:{letter}\n\nto: {email_receiver}")
        send_email(email_receiver, letter)
