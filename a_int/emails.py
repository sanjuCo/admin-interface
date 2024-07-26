from django.core.mail import send_mail

def credentials(username, password, email, login_url):
    subject = 'Credentials'
    from_email = 'samuelnjeri111@gmail.com'
    to_email = [email]
    message= f'Use your username {username} and password {password} to login and finish your profile by visiting the url {login_url}'
    send_mail(subject, message, from_email, to_email)
