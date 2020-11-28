from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time, sys, argparse
from selenium.webdriver.common.action_chains import ActionChains
from tqdm import tqdm




def send_automated_whatsapp_msgs(*, target, message, file=None, count=10):
    driver = webdriver.Chrome('/usr/bin/chromedriver') 
    driver.get("https://web.whatsapp.com/") 
    wait = WebDriverWait(driver, 1000) 
    # time.sleep(3)
    # chat_list_arg="//div[@arial-label='Chat list. Press right arrow key on a chat to open chat context menu.'][@class='-GlrD _2xoTX'][@role='region']"
    x_arg = "//span[@dir='auto'][@title='{}']".format(target)
    # target_user = wait.until(EC.presence_of_element_located((By.XPATH, x_arg))) 
    target_user = wait.until(EC.element_to_be_clickable((By.XPATH, x_arg))) 
    if not target_user:
        print('User not traced!')
        return
    target_user.click()

    inp_xpath = "//div[@contenteditable='true'][@data-tab='6'][@dir='ltr'][@spellcheck='true']"
    
    print("If not started yet, Click anywhere on the console to start")
    
    input_box = wait.until(EC.presence_of_element_located(( By.XPATH, inp_xpath)))
    input_box.click()
    if file:
        with open(file) as f:
            content=f.read().splitlines()
            for i in tqdm(range(len(content))):
#                print("#{}".format(i+1))
                if i==len(content)-1:
                    input_box.send_keys(content[i]+Keys.ENTER)
                    ActionChains(driver).send_keys(Keys.ENTER)
                else:
                    input_box.send_keys(content[i])
                
                    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()
                    # input_box.click()
                time.sleep(0.1)
    else:
        for i in tqdm(range(count)): 
#            print("#{}".format(i+1))
            input_box.send_keys(message+Keys.ENTER) 
#            time.sleep(0.05) 
        # driver.quit()

if __name__=='__main__':
    parser=argparse.ArgumentParser(
        description='''Whatsapp automated messaging. ''',)
    parser.add_argument('-t', type=str, help='target user or group')
    parser.add_argument('-f', type=str, help='message file name')
    parser.add_argument('-m', type=str, help='message')
    parser.add_argument('-n', type=int, default=10, help='Count of messages to be sent! by default 10')
    args=parser.parse_args()
    if (args.m or args.f) and args.t:
        send_automated_whatsapp_msgs(target=args.t, message=args.m, count=args.n, file=args.f)
    else:
        print('Required target and message/message-file')
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
