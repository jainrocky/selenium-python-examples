from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import termios, fcntl, sys, os




if __name__=='__main__':

    fd = sys.stdin.fileno()
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    print('Loading...', end='\r')
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome('/usr/bin/chromedriver', options=option)

    url='https://www.worldometers.info/world-population/'
    class_name='rts-counter'
    driver.get(url)
    wait=WebDriverWait(driver, 100)

    try:
        element = driver.find_element_by_class_name(class_name)
    except:
        print('ElementNotFound: Inspect {} weppage and find the element class-name in which population text is displaying and update the class_name variable'.format(url))
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        driver.quit()
        exit(1)

    try:
        while True:
            try:
                c = sys.stdin.read(1)
                if c=='q' or c=='Q':
                    break
                else:
                    print('\r'+'(press q for exit) Current World Population: [ {} ]'.format(element.text), end='')
            except IOError: pass
    finally:
        print()
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        driver.quit()
