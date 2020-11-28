from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
import argparse, re, json
from tabulate import tabulate



def overall(driver, wait, paths, *args, **kwargs):
    overall_tab_path=paths['overall']['overall_tab_path']
    overall_btn = wait.until(EC.presence_of_element_located(( By.XPATH, overall_tab_path)))
    overall_btn.click()

    table1_path=paths['overall']['table1_path']
    table1=driver.find_elements( By.XPATH, table1_path)

    data=[]
    for row in table1:
        for e in row.find_elements_by_tag_name('td'):
            h, d = e.text.split(':')
            data.append([h.strip(), d.strip()])
    
    print(tabulate(data,))

    table2_head_path=paths['overall']['table2_head_path']
    table2_head=driver.find_elements( By.XPATH, table2_head_path)

    headers=[head.text for head in table2_head]
    
    table2_path=paths['overall']['table2_path']
    table2=driver.find_elements( By.XPATH, table2_path)

    data=[]
        
    for row in table2:
        data.append([e.text for e in row.find_elements_by_tag_name('td')])

    print()    
    print(tabulate(data, headers=headers, ))


def sem(driver, wait, paths, n, *args, **kwargs):
    sem_btn_path=paths['semester']['sem_btn_path'].format(n)
    sem_btn=wait.until(EC.presence_of_element_located(( By.XPATH, sem_btn_path)))
    sem_btn.click()

    table1_path=paths['semester']['table1_path']
    table1=driver.find_elements( By.XPATH, table1_path)

    data=[]
    for row in table1:
        for e in row.find_elements_by_tag_name('td'):
            h, d = e.text.split(':')
            data.append([h.strip(), d.strip()])
    
    print(tabulate(data,))

    table2_head_path=paths['semester']['table2_head_path']
    table2_head=driver.find_elements( By.XPATH, table2_head_path)
    headers=[head.text for head in table2_head]

    table2_path=paths['semester']['table2_path']
    table2=driver.find_elements( By.XPATH, table2_path)

    data=[]
        
    for row in table2:
        data.append([e.text for e in row.find_elements_by_tag_name('td')])

    print()    
    print(tabulate(data, headers=headers, ))


def find_student(driver, wait, paths, id, *args, **kwargs):
    try:
        input_path=paths['input_path']
        input_box = wait.until(EC.presence_of_element_located(( By.XPATH, input_path)))
        input_box.click()
        input_box.send_keys(id+Keys.ENTER)
        name_path=paths['name_path']
        name=wait.until(EC.presence_of_element_located(( By.XPATH, name_path)))
        print('\r'+name.text+'\n', end='\r')
    except:
        raise Exception()
    return True


def validate_enroll(id):
    return True if re.match(r'^\d{11}$', id) else False


def main(args, **kwargs):
    print('Fetching...!', end='\r')

    with open('result_path.json') as f:
        paths = json.load(f)

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(paths['chromedriver'], options=option)

    driver.get(paths['url'])
    wait=WebDriverWait(driver, 5)
    try: 
        
        if find_student(driver, wait, paths, args.id,):
            if args.o:
                overall(driver, wait, paths)
            elif args.s:
                sem(driver, wait, paths, args.s, )
    except:
        print('Not found!')
        exit(1)


if __name__=='__main__':
    description='''
        IPU Ranklist CLI
    '''
    parser=argparse.ArgumentParser(description=description, )
    parser.add_argument('-id', type=str, help='Student\'s enrollment id')
    parser.add_argument('-o', action='store_true', help='Student\'s Overall Result')
    parser.add_argument('-s', type=int, help='Semester number')
    args=parser.parse_args()

    if args.id and validate_enroll(args.id) and (args.o or args.s):
        main(args)
    else:
        print('Required Student enrollment id and atleast one argument')