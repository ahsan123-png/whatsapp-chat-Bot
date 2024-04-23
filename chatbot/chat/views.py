
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# Create your views here.
from .models import *

def home(request):
    return render(request,'home.html')

def saveContacts(request):
    if request.method=="POST":
        name= request.POST.get('name')
        phone= request.POST.get('phone')
        user=Contact.objects.create(
            userName=name,
            phoneNumber= phone
        )
        user.save()
    return redirect('home')
# ======== View Contacts ========
def viewContacts(request):
    if request.method =="GET":
        contacts=Contact.objects.all()
        context={
            "contacts" : contacts,
        }
    return render(request,'contacts.html' , context=context)


def sendMessage(request):
    return render(request , 'send_message.html')


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

def messages(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)
        try:
            service = Service('E:\\chromedriver\\chromedriver-win64\\chromedriver.exe')
            options = Options()
            options.add_argument('--headless')
            options.add_argument('window-size=1200x600')  # Set window size for headless mode
            driver = webdriver.Chrome(service=service, options=options)
            driver.get('https://web.whatsapp.com/')
            
            # Wait for the element to be present
            wait = WebDriverWait(driver, 10)
            contacts = Contact.objects.all()
            for contact in contacts:
                search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
                search_box.send_keys(contact.userName, Keys.ENTER)
                time.sleep(2)  # Wait for the chat window to load
                message_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')))
                message_box.send_keys(message, Keys.ENTER)
                time.sleep(1)  # Wait for the message to be sent
            driver.quit()
            return HttpResponse('Message sent to all contacts successfully!')
        except Exception as e:
            return HttpResponse(f'An error occurred: {str(e)}')
    else:
        return render(request, 'send_message.html')


