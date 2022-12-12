from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk

def sender():
    global window
    contact = entry1.get()
    text=entry2.get()
    num = entry3.get()
    #/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span
    driver = webdriver.Firefox(r"geckodriver address")
    driver.get("https://web.whatsapp.com")
    inp_xpath_search = "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]"
    input_box_search = WebDriverWait(driver,500).until(lambda driver: driver.find_element(By.XPATH,inp_xpath_search))
    input_box_search.click()
    time.sleep(1)
    input_box_search.send_keys(contact)
    time.sleep(1)
    selected_contact = driver.find_element(By.XPATH,"//span[@title='"+contact+"']")
    selected_contact.click()
    inp_xpath = '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
    input_box = driver.find_element(By.XPATH,inp_xpath)
    time.sleep(1)
    for i in range(int(num)):
        for t in text:
            input_box.send_keys(t)
        send = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]")
        send.click()
        #time.sleep(0.5)
    #driver.quit()

window = tk.Tk()
window.title("WP BOT")
window.geometry("700x400")
lblC = tk.Label(window,text ="Write the contact:",font = 15).place(x=50,y=30)
lblT = tk.Label(window,text ="Write your message:",font = 15).place(x=50,y=60)
lblA = tk.Label(window,text ="Enter number of message to be sent:",font = 15).place(x=50,y=90)
entry1 = tk.Entry(window)
entry1.place(x=330,y=30,width=150) 
entry2 = tk.Entry(window)
entry2.place(x=330,y=60,width=150) 
entry3 = tk.Entry(window)
entry3.place(x=330,y=90,width=150) 
btn1 = tk.Button(window,text="Send the message",command = sender,width=20,bg="red").place(x=250,y=150)
tk.mainloop()