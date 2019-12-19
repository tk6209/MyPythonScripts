import time, selenium, sys
from selenium import webdriver as wb


orig_stdout = sys.stdout

f = open('worklogs.txt', 'w')
sys.stdout = f

wb = wb.Firefox()
xpath = wb.find_element_by_xpath

i=0
while i < 10:

    url = ('https://clientsupport.worldlinesweden.com/browse/PAYPAL-59'+str(i))
    print(url)
    wb.get(url)
    time.sleep(20)
    ikey = wb.title
    #ikey = wb.current_url

    def left(ikey,amount):
              return s[:amount]

    ikey = ikey[:12]
    #ikey[49:]

    time.sleep(4)
    btn = wb.find_element_by_id('worklog-tabpanel')

       
    #wb.find_element_by_xpath('//*[@id="worklog-tabpanel"]')
    btn.click()

    time.sleep(4)
    txt = wb.find_element_by_class_name("worklog-comment").text
    if txt is not None:

        print(ikey," ", txt)

    else:
        i += 1

i += 1
sys.stdout = orig_stdout
f.close()


#RESULT: [
#PAYPAL-599]   Fernanda Yamazaki, from Rede, confirmed that Rede is sending the records as expected, multiple forecast and funding records due to multiple chargebacks in many installments;

