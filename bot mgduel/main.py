from log import user,hasl
from waiting import wait
from selenium import webdriver
import time
import math
import random
import sys

from selenium.webdriver.remote.webelement import WebElement
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
dri = webdriver.Chrome(options=options)
#dri= webdriver.Chrome()
dri.get("http://mgduel.pl/")
i=0
def main():
    def logowanie():
        lem=dri.find_element_by_id("lemail")
        lpa=dri.find_element_by_id("lpass")
        lem.send_keys(user)
        lpa.send_keys(hasl)
        but=dri.find_elements_by_xpath('//button[text()="Logowanie"]')[0]
#print(but)
        but.click()
        time.sleep(1)
        
    logowanie()
    
    speed=[]
    lop=0

    for x in range(60):
        o=""
        for j in range(random.randint(1,10)):
            o+=str(random.randint(0,9))

        speed.append(float(str(random.randint(2,5))+'.'+str(o)  ))
    
    
    
    def logout():
        dri.find_element_by_class_name("b5").click()
        time.sleep(60*random.randint(3,7))
        #time.sleep(5)
        main()


    def sell():
        global i
        sklep=dri.find_element_by_id("zone_shop")
        time.sleep(random.choice(speed))
        sklep.click()
        dri.find_elements_by_xpath('//button[text()="Sprzedaj wszystkie śmieci"]')[0].click()
        dri.find_elements_by_xpath('//button[text()="Wyjdź ze sklepu"]')[0].click()
        time.sleep(random.choice(speed))
        i+=1


    def level():
            global i
            lvl=int(dri.find_element_by_id("lvl").text)
            lvlper=math.ceil(lvl/5)
            zone=dri.find_element_by_id("zone_dungeon"+str(lvlper))
            zone.click()
            i=0
            if lvl<=5:
                time.sleep(2)
                dri.find_element_by_css_selector("div[onclick^='enterDungeon("+str(lvl) +")']").click()
                time.sleep(2)
                #dri.find_element_by_css_selector("button[onclick^='$('#dungeon').fadeOut()']").click()
                dri.find_elements_by_class_name("exit")[2].click()
                #$('#dungeon').fadeOut()
                #dri.implicitly_wait(10)
                #dri.find_elements_by_link_text("exit")
                #print(dri.find_elements_by_link_text("exit"))
                #print(b)
                #print("rteret")
                #b.click()
                #print("hg")
                time.sleep(random.choice(speed))
            else:
                if lvl==6:
                    time.sleep(2)
                    dri.find_elements_by_css_selector("div[onclick^='enterDungeon("+str(1) +")']")[1].click()
                   # dri.implicitly_wait(10)
                    time.sleep(2)
                    dri.find_elements_by_class_name("exit")[2].click()
                    
                    time.sleep(random.choice(speed))
                elif lvl>11:
                    time.sleep(2)
                    dri.find_elements_by_css_selector("div[onclick^='enterDungeon("+str(5) +")']")[1].click()
                    time.sleep(2)
                    dri.find_elements_by_class_name("exit")[2].click()
                    time.sleep(random.choice(speed))
                else:
                    time.sleep(2)
                    dri.find_elements_by_css_selector("div[onclick^='enterDungeon("+str(int(lvl)-5) +")']")[1].click()
                    #dri.implicitly_wait(10)
                    time.sleep(2)
                    dri.find_elements_by_class_name("exit")[2].click()
                    time.sleep(random.choice(speed))
    def buyap():
        sklep=dri.find_element_by_id("zone_shop")
        time.sleep(random.choice(speed))
        sklep.click()
        dri.find_elements_by_xpath('//button[text()="Kup 10 PA za "]')[0].click()
        dri.find_elements_by_xpath('//button[text()="Wyjdź ze sklepu"]')[0].click()
        time.sleep(random.choice(speed))
    
    def pier():
        global i
        apb=dri.find_element_by_id("ap")
        ap=int(apb.text)
        while ap !=-1:
            print("chuj")
        

            bag=dri.find_elements_by_class_name("item")
            if i==3:
                break
                sys.exit()
            if len(bag)==15 or len(bag)==18:
                sell()
        
        
        
            apb=dri.find_element_by_id("ap")
            ap=int(apb.text)
        #print(ap)
            try:
                dri.find_elements_by_xpath('//div[img/@src="/img/items/1.p1.gif"]')[0].click()
            except:
                #print("img zjebalo")
            #print(dri.find_elements_by_xpath('//div[img/@src="/img/items/1.p1.gif"]'))
                0
        
            if ap==0:
                logout()
            else:
                level()
            if int(dri.find_element_by_id("gold").text)>int(dri.find_element_by_id("lvl").text)*20:
                buyap()

    pier()
main()