import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage
# import PyAudio

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def get_info():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('akonasif579@gmail.com', 'hfglbffrphtzhvjs') #need to login my gmail account so go to gmail and on the access account
    email = EmailMessage()
    email['From'] = 'akonasif579@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject 
    email.set_content(message)
    server.send_message(email)
    
email_list = {
    'mother': 'tarinsulta733@gmail.com',
    'brother': 'akonasif321@gmail.com',  
}    

    
def get_email_info():
    talk("To Whom you want send email")
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What is the subject of Your email?")
    subject = get_info()
    talk("tell me the text in your email")
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey lazy Men. Your email is sent')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()
    elif 'no' in send_more:
        talk("Ok Boss, thank you for using me")

get_email_info()     
    
