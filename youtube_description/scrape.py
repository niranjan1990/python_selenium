from selenium import webdriver 
import pandas as pd 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import csv

def getUrls(targeturl):
    driver = webdriver.Chrome() 
    driver.get(targeturl)
    driver.implicitly_wait(900000)
    user_data = driver.find_element_by_xpath('//*[@id="description"]/yt-formatted-string').get_attribute('innerHTML')
    print('user_data',user_data)
    Table_dict={ 'url': targeturl,'Description':user_data}    
    templist.append(Table_dict) 
    df = pd.DataFrame(templist)
    df.to_csv('table.csv',encoding='utf-8') 
    driver.quit()

templist = []
webPage = ['https://www.youtube.com/watch?v=jcd3_NgeDjI&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=1'
,'https://www.youtube.com/watch?v=thc5MYcZwzc&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=2'
,'https://www.youtube.com/watch?v=WjKtdzQ_w8E&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=3'
,'https://www.youtube.com/watch?v=XnbWSfSYcHw&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=4'
,'https://www.youtube.com/watch?v=5b7Z4vpgtLU&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=5'
,'https://www.youtube.com/watch?v=rUauIbqpxd4&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=6'
,'https://www.youtube.com/watch?v=vk2LlFRB-Og&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=7'
,'https://www.youtube.com/watch?v=aHZYFlPaHf8&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=8'
,'https://www.youtube.com/watch?v=-_HcHkXIbHA&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=9'
,'https://www.youtube.com/watch?v=XL-yrimto1k&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=10'
,'https://www.youtube.com/watch?v=1Z9UxYDcSFg&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=11'
,'https://www.youtube.com/watch?v=stiFPDBjavM&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=12'
,'https://www.youtube.com/watch?v=6Ygd2fUkrfE&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=13'
,'https://www.youtube.com/watch?v=wwRkz5DPxNA&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=14'
,'https://www.youtube.com/watch?v=zo8Hdwgop6A&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=15'
,'https://www.youtube.com/watch?v=TqI8VCjgawY&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=16'
,'https://www.youtube.com/watch?v=1A7MhCz6_Yw&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=17'
,'https://www.youtube.com/watch?v=rUXrb80VlDc&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=18'
,'https://www.youtube.com/watch?v=_2RhtSJyqBs&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=19'
,'https://www.youtube.com/watch?v=6k9ZBHZLTlA&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=20'
,'https://www.youtube.com/watch?v=VYdpypPG-io&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=21'
,'https://www.youtube.com/watch?v=3fupGMUk7-w&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=22'
,'https://www.youtube.com/watch?v=_ZgrQXJQ8WI&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=23'
,'https://www.youtube.com/watch?v=GZccmbVLNIU&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=24'
,'https://www.youtube.com/watch?v=vVdzwO7J1Yc&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=25'
,'https://www.youtube.com/watch?v=0V772hTxAQA&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=26'
,'https://www.youtube.com/watch?v=nUC6vmVNAT0&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=27'
,'https://www.youtube.com/watch?v=NZMoWa46Fh8&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=28'
,'https://www.youtube.com/watch?v=qGv589JafGo&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=29'
,'https://www.youtube.com/watch?v=ZhCO7opyLFk&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=30'
,'https://www.youtube.com/watch?v=YyYHVGn8IvA&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=31'
,'https://www.youtube.com/watch?v=UbBveHK5Ueg&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=32'
,'https://www.youtube.com/watch?v=bET6ya8VgCk&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=33'
,'https://www.youtube.com/watch?v=brzpq4UtyVc&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=34'
,'https://www.youtube.com/watch?v=ITsJM0pKeVs&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=35'
,'https://www.youtube.com/watch?v=Jx8Qlvs4FxE&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=36'
,'https://www.youtube.com/watch?v=C2DueVzzZy8&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=37'
,'https://www.youtube.com/watch?v=QqvPBafXfZo&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=38'
,'https://www.youtube.com/watch?v=-u60U73SN70&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=39'
,'https://www.youtube.com/watch?v=ZdUqQwR58VM&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=40'
,'https://www.youtube.com/watch?v=gykr2c53ktM&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=41'
,'https://www.youtube.com/watch?v=AtetGe0dB8U&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=42'
,'https://www.youtube.com/watch?v=D3SasX5ZsTU&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=43'
,'https://www.youtube.com/watch?v=Xx7SaqhN1ro&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=44'
,'https://www.youtube.com/watch?v=6y8d9PJfuLg&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=45'
,'https://www.youtube.com/watch?v=gr94g_mmMnE&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=46'
,'https://www.youtube.com/watch?v=dgT9ZM1yNrE&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=47'
,'https://www.youtube.com/watch?v=RuhCM0myQZU&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=48'
,'https://www.youtube.com/watch?v=-sdB60vJTvk&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=49'
,'https://www.youtube.com/watch?v=aYNp2_RQwfw&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=50'
,'https://www.youtube.com/watch?v=IWqVsDNFDks&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=51'
,'https://www.youtube.com/watch?v=5OBknWmwoIw&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=52'
,'https://www.youtube.com/watch?v=wP7f__SzYH0&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=53'
,'https://www.youtube.com/watch?v=xnLY5JcOo9s&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=54'
,'https://www.youtube.com/watch?v=t8_bdO4Mg4c&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=55'
,'https://www.youtube.com/watch?v=O2LbEcEFSj8&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=56'
,'https://www.youtube.com/watch?v=E-uaaJz-imI&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=57'
,'https://www.youtube.com/watch?v=4dZBhNN4fFA&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=58'
,'https://www.youtube.com/watch?v=XPBrDN4rk1k&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=59'
,'https://www.youtube.com/watch?v=D3wI1NWurl0&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=60'
,'https://www.youtube.com/watch?v=WVxJlbFpM0s&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=61'
,'https://www.youtube.com/watch?v=eiiHnS4DAFw&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=62'
,'https://www.youtube.com/watch?v=64SNpxgFhiQ&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=63'
,'https://www.youtube.com/watch?v=W8SGKDGbjCc&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=64'
,'https://www.youtube.com/watch?v=l1kMfmFNQ28&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=65'
,'https://www.youtube.com/watch?v=We60WS3NBB4&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=66'
,'https://www.youtube.com/watch?v=IXJboD1QBEY&list=PLW1XlJ-Yzv-Pkj0dmED889u-3pyclMjmL&index=67'
,'https://www.youtube.com/watch?v=MQffBLluJ4A&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=1'
,'https://www.youtube.com/watch?v=OcXsv4O-uog&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=2'
,'https://www.youtube.com/watch?v=f6SKHfJnLj8&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=3'
,'https://www.youtube.com/watch?v=_8Nf6web7X8&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=4'
,'https://www.youtube.com/watch?v=NGd1V3gjGyo&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=5'
,'https://www.youtube.com/watch?v=82V0O4WTPQ8&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=6'
,'https://www.youtube.com/watch?v=dhjo8vCx3c0&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=7'
,'https://www.youtube.com/watch?v=YmtM1mjokTU&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=8'
,'https://www.youtube.com/watch?v=kMfRiR4p2Uw&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=9'
,'https://www.youtube.com/watch?v=Il1gMQkWI44&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=10'
,'https://www.youtube.com/watch?v=esj5XNnSE4Y&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=11'
,'https://www.youtube.com/watch?v=Yk6VkHK2Ld0&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=12'
,'https://www.youtube.com/watch?v=O0K6A4cr0Rc&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=13'
,'https://www.youtube.com/watch?v=dq6fHaf4df4&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=14'
,'https://www.youtube.com/watch?v=XSja_fYbLZ8&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=15'
,'https://www.youtube.com/watch?v=Auw-MiPbaZw&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=16'
,'https://www.youtube.com/watch?v=IdHxQaaTGIA&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=17'
,'https://www.youtube.com/watch?v=tq9zLBH6toM&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=18'
,'https://www.youtube.com/watch?v=V_ERLFKbNww&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=19'
,'https://www.youtube.com/watch?v=T13G1oQdNWg&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=20'
,'https://www.youtube.com/watch?v=K1ay8uGEpik&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=23'
,'https://www.youtube.com/watch?v=gNwfRp8Q258&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=24'
,'https://www.youtube.com/watch?v=1r6l3BuMPPY&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=25'
,'https://www.youtube.com/watch?v=oClFPbjiT5Q&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=26'
,'https://www.youtube.com/watch?v=pMnx0gnakQM&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=27'
,'https://www.youtube.com/watch?v=4G01jh4mkJ0&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=28'
,'https://www.youtube.com/watch?v=tr2E_RiJOb8&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=29'
,'https://www.youtube.com/watch?v=GaQ_Lq9yvqA&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=30'
,'https://www.youtube.com/watch?v=zFiwAs5lXOE&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=48'
,'https://www.youtube.com/watch?v=qH3puZaqPs0&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=32'
,'https://www.youtube.com/watch?v=NDmnyDt79Ow&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=33'
,'https://www.youtube.com/watch?v=fJWss6jLjo4&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=45'
,'https://www.youtube.com/watch?v=6NFiGZEsWTY&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=44'
,'https://www.youtube.com/watch?v=13TXUSmy2xc&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=34'
,'https://www.youtube.com/watch?v=pA23Tr1nZbg&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=35'
,'https://www.youtube.com/watch?v=kmWHGf7FEP8&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=36'
,'https://www.youtube.com/watch?v=DdGxuRtZzoc&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=38'
,'https://www.youtube.com/watch?v=lAIJegomCXk&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=46'
,'https://www.youtube.com/watch?v=mXigjC1fCRM&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=39'
,'https://www.youtube.com/watch?v=PK-69F8Ito8&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=47'
,'https://www.youtube.com/watch?v=a98YkaC0zp0&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=40'
,'https://www.youtube.com/watch?v=jeeJUrNAtso&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=41'
,'https://www.youtube.com/watch?v=x9umggQmmIQ&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=42'
,'https://www.youtube.com/watch?v=PWnJTYRqGGE&list=PLW1XlJ-Yzv-PY5jUqbsb32bSiKeF4s0Xd&index=43'
,'https://www.youtube.com/watch?v=BKy2MmEwL1E&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI'
,'https://www.youtube.com/watch?v=uD2612rmlZA&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=2'
,'https://www.youtube.com/watch?v=1qTRdX5lveA&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=3'
,'https://www.youtube.com/watch?v=6ehiSkNdlqc&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=4'
,'https://www.youtube.com/watch?v=-Og-1RtouQ4&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=5'
,'https://www.youtube.com/watch?v=ial8VutYC1E&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=6'
,'https://www.youtube.com/watch?v=2Myx2NRW5kc&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=7'
,'https://www.youtube.com/watch?v=5AalFhSfg6Q&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=8'
,'https://www.youtube.com/watch?v=Nj2CqDZoNm8&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=9'
,'https://www.youtube.com/watch?v=YevziSwWEWc&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=10'
,'https://www.youtube.com/watch?v=vN3Ql1sjT8g&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=11'
,'https://www.youtube.com/watch?v=2IlJdrVtnIE&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=12'
,'https://www.youtube.com/watch?v=Nkq2V2AY-Aw&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=13'
,'https://www.youtube.com/watch?v=Ir55kHftPM4&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=14'
,'https://www.youtube.com/watch?v=as9GivKoTx4&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=15'
,'https://www.youtube.com/watch?v=HgzfSyXRqdU&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=16'
,'https://www.youtube.com/watch?v=cx80ciqUZoI&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=17'
,'https://www.youtube.com/watch?v=cbITHZ6CpLo&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=18'
,'https://www.youtube.com/watch?v=CDGV27Rn4HI&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=22'
,'https://www.youtube.com/watch?v=dW5grBs1bvE&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=21'
,'https://www.youtube.com/watch?v=QPOeTlk-Wjk&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=19'
,'https://www.youtube.com/watch?v=czaiBB_8vQo&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=23'
,'https://www.youtube.com/watch?v=DQW3nRmtDLM&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=24'
,'https://www.youtube.com/watch?v=AzqCLOUZGoQ&list=PLW1XlJ-Yzv-NrO1NK7JaiJdqKQAbU0BTI&index=20'
,'https://www.youtube.com/watch?v=jxdoMGW3eQk&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc'
,'https://www.youtube.com/watch?v=8DArbkT8kHo&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=2'
,'https://www.youtube.com/watch?v=XNTtF2HxBRs&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=3'
,'https://www.youtube.com/watch?v=FzQN8-uZvpA&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=4'
,'https://www.youtube.com/watch?v=RrC698DNt3k&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=5'
,'https://www.youtube.com/watch?v=W1i0WnK8Qak&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=6'
,'https://www.youtube.com/watch?v=NbvgqkEsX90&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=7'
,'https://www.youtube.com/watch?v=vm52_jhrIBg&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=8'
,'https://www.youtube.com/watch?v=Id4W7AqeCkE&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=9'
,'https://www.youtube.com/watch?v=K1GXKzxjjtc&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=10'
,'https://www.youtube.com/watch?v=IkH6SMsKY7o&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=11'
,'https://www.youtube.com/watch?v=X9GZmTP_7gk&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=12'
,'https://www.youtube.com/watch?v=KTEYi9LRiVU&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=13'
,'https://www.youtube.com/watch?v=CDFn9Ii9q-A&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=14'
,'https://www.youtube.com/watch?v=KHtESTSr_x8&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=15'
,'https://www.youtube.com/watch?v=74SYjIJPvIg&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=21'
,'https://www.youtube.com/watch?v=WwxRoEYkVzc&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=21'
,'https://www.youtube.com/watch?v=mI1r9rlBI0c&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=16'
,'https://www.youtube.com/watch?v=JVMzrqHcqDc&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=17'
,'https://www.youtube.com/watch?v=gXat_vVhe0k&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=22'
,'https://www.youtube.com/watch?v=Dl_FoNIikxc&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=19'
,'https://www.youtube.com/watch?v=ip7arFHNVKI&list=PLW1XlJ-Yzv-OBI4aqRj_yvQY1OXwP3Cqc&index=20'
,'https://www.youtube.com/watch?v=3kgPzxdeD7k'
,'https://www.youtube.com/watch?v=ewmjxKk_MRY'
,'https://www.youtube.com/watch?v=pWzcBI3Uc0E'
,'https://www.youtube.com/watch?v=7IK0-nCpSVA'
,'https://www.youtube.com/watch?v=o9HsRVJcxWc'
,'https://www.youtube.com/watch?v=1Gb4mhb1u3s'
,'https://www.youtube.com/watch?v=1LAceng7pzE'
,'https://www.youtube.com/watch?v=lZurhbQjrPk'
,'https://www.youtube.com/watch?v=p0tcPPIPSC0'
,'https://www.youtube.com/watch?v=zIlSj7FkV2Y&t=1s'
,'https://www.youtube.com/watch?v=x7mzb8f_6G0'
,'https://www.youtube.com/watch?v=Pz-tbvVAVbU'
,'https://www.youtube.com/watch?v=xwIp4xZzU98'
,'https://www.youtube.com/watch?v=H2jZkEe_5bg'
,'https://www.youtube.com/watch?v=9JF22ahvQxw'
,'https://www.youtube.com/watch?v=NfjyPMLN0QM'
,'https://www.youtube.com/watch?v=KY7_TKFR_Xs'
,'https://www.youtube.com/watch?v=2kd4dPvHFWE'
,'https://www.youtube.com/watch?v=Eh3MIXB90hg'
,'https://www.youtube.com/watch?v=OD2EBXxPUuE'
,'https://www.youtube.com/watch?v=vZGK-IODVsU'
,'https://www.youtube.com/watch?v=Ii-HR90Q6pA'
,'https://www.youtube.com/watch?v=ScJWAy2xRAY'
,'https://www.youtube.com/watch?v=KqIaULeOCGA'
,'https://www.youtube.com/watch?v=j3R-r9j4ONg'
,'https://www.youtube.com/watch?v=ppw6uGmltMQ'
,'https://www.youtube.com/watch?v=VIgOVUqzImo'
,'https://www.youtube.com/watch?v=UqD-9E0-X6I'
,'https://www.youtube.com/watch?v=DragdoQJ3no&t=1s'
,'https://www.youtube.com/watch?v=RzP_87Q-IMk'
,'https://www.youtube.com/watch?v=bOJTcvILJu4'
,'https://www.youtube.com/watch?v=nhLekbHlQ4w'
,'https://www.youtube.com/watch?v=_Zg-d2cfWQc'
,'https://www.youtube.com/watch?v=2i_yuVQOKBU'
,'https://www.youtube.com/watch?v=RKdHSTxHMwU'
,'https://www.youtube.com/watch?v=Bfk9IBtt69Q'
,'https://www.youtube.com/watch?v=b2i-B95v3Bs'
,'https://www.youtube.com/watch?v=GETu7K3jZUg'
,'https://www.youtube.com/watch?v=oRp6ClYxSzw'
,'https://www.youtube.com/watch?v=zE38-292YEQ'
,'https://www.youtube.com/watch?v=rZFI1uNQUGg'
,'https://www.youtube.com/watch?v=KSdVIxINtlg'
,'https://www.youtube.com/watch?v=z9O_3jE-ewY'
,'https://www.youtube.com/watch?v=MjiectMedrQ'
,'https://www.youtube.com/watch?v=gDmgCpTWA38'
,'https://www.youtube.com/watch?v=i9QcduIevNo'
,'https://www.youtube.com/watch?v=63XhwqNEy4I'
,'https://www.youtube.com/watch?v=DSq7fdP0Y5k'
,'https://www.youtube.com/watch?v=1E3WB3gEbko'
,'https://www.youtube.com/watch?v=Zu354RmNa08'
,'https://www.youtube.com/watch?v=2bmwBQVi8l8'
,'https://www.youtube.com/watch?v=HZLrsx1Em28'
,'https://www.youtube.com/watch?v=jgdiy_SwLkQ'
,'https://www.youtube.com/watch?v=nEDN1BVif9o'
,'https://www.youtube.com/watch?v=eovW21xmO4c'
,'https://www.youtube.com/watch?v=TJqNk-gqjXc'
,'https://www.youtube.com/watch?v=EYEGHBhhrcs'
,'https://www.youtube.com/watch?v=p-BQk2FIQTc'
,'https://www.youtube.com/watch?v=yHCi5diq5WM'
,'https://www.youtube.com/watch?v=cBVB1428b2Q'
,'https://www.youtube.com/watch?v=NJ_QxZ5srt4'
,'https://www.youtube.com/watch?v=u7g6guI68Qs'
,'https://www.youtube.com/watch?v=k1xIOdyGm3w'
,'https://www.youtube.com/watch?v=6mx8sQHcj5c'
,'https://www.youtube.com/watch?v=-PwAp6nnEvY'
,'https://www.youtube.com/watch?v=46jGIrDpXGY'
,'https://www.youtube.com/watch?v=mtw0kme4xW0'
,'https://www.youtube.com/watch?v=ztSDdPXEs3A'
,'https://www.youtube.com/watch?v=i-EbxluLI2o'
,'https://www.youtube.com/watch?v=dyNDgl7AJkk'
,'https://www.youtube.com/watch?v=G_GtESwo-Hc'
,'https://www.youtube.com/watch?v=TOGZhJ8N7DE'
,'https://www.youtube.com/watch?v=9rcC_2Ck4-M&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=13'
,'https://www.youtube.com/watch?v=p5mfqs23FzI&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=14'
,'https://www.youtube.com/watch?v=HUCB3eLro6Y&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=6'
,'https://www.youtube.com/watch?v=Jo3oCDLz1fE&list=PLW1XlJ-Yzv-OiPocUyn-I5CQXPMJqc6uC&index=24'
,'https://www.youtube.com/watch?v=GjvavEk4oOE&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=15'
,'https://www.youtube.com/watch?v=jmWjuuuemO8&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=16'
,'https://www.youtube.com/watch?v=skE2kdinfiU&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=17'
,'https://www.youtube.com/watch?v=W4-WujnYwlY&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=18'
,'https://www.youtube.com/watch?v=KMVWs3ZaBGo&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=19'
,'https://www.youtube.com/watch?v=bKB0xD_jAoI&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=20'
,'https://www.youtube.com/watch?v=LdITskk5OCY&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=21'
,'https://www.youtube.com/watch?v=IbVO-eGiP88&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=22'
,'https://www.youtube.com/watch?v=j86AgF_g48Y&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=23'
,'https://www.youtube.com/watch?v=JR1sJ0UP_J8&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=2'
,'https://www.youtube.com/watch?v=KIpnDB-u-i0&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=24'
,'https://www.youtube.com/watch?v=KtcGImtVCTo&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=25'
,'https://www.youtube.com/watch?v=Vnnc_QvAEVg&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=30'
,'https://www.youtube.com/watch?v=4gP9ksYzQN8&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=26'
,'https://www.youtube.com/watch?v=3qMHH010G2o&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=27'
,'https://www.youtube.com/watch?v=Q9bTHh7ztTY&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=10'
,'https://www.youtube.com/watch?v=EBAVxyB7zec&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=28'
,'https://www.youtube.com/watch?v=fcS9tr5nWyo&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=30'
,'https://www.youtube.com/watch?v=bmXDZUTifKE&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=9'
,'https://www.youtube.com/watch?v=vVxuC--ZWYE&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=1'
,'https://www.youtube.com/watch?v=GfEr7Nm64QY&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=29'
,'https://www.youtube.com/watch?v=p8oZ1jwCOgo&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=11'
,'https://www.youtube.com/watch?v=GUUA8f1idAY&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=3'
,'https://www.youtube.com/watch?v=sLv4I5eDfx8&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=12'
,'https://www.youtube.com/watch?v=Vb2yyoF2uxU&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=5'
,'https://www.youtube.com/watch?v=Bj4_BBDf2P4&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=4'
,'https://www.youtube.com/watch?v=38kiOJmY2e8&list=PLW1XlJ-Yzv-O29787rKqRAQGW8EcZzZw1&index=7'
,'https://www.youtube.com/watch?v=SJpJk_JEp6w&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=13'
,'https://www.youtube.com/watch?v=1ymWpJ5fyfg&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=14'
,'https://www.youtube.com/watch?v=Ra8nNPVIH7o&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=6'
,'https://www.youtube.com/watch?v=jCBW83mnIoc&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=1'
,'https://www.youtube.com/watch?v=wPjzWlmJ7XY&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=15'
,'https://www.youtube.com/watch?v=OE1oldasqIo&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=19'
,'https://www.youtube.com/watch?v=YAO5-6N8ZAw&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=16'
,'https://www.youtube.com/watch?v=h9ZNSs5Bpk8&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=17'
,'https://www.youtube.com/watch?v=IIvd4ZMShuQ&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=18'
,'https://www.youtube.com/watch?v=Y5PSoDFfIU0&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=20'
,'https://www.youtube.com/watch?v=tRrHlL13Dt0&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=21'
,'https://www.youtube.com/watch?v=4npODqvf-vM&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=22'
,'https://www.youtube.com/watch?v=2wmYbVYY5Jw&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=23'
,'https://www.youtube.com/watch?v=8GYHhWtoDv0&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=8'
,'https://www.youtube.com/watch?v=yr4lv-H_zBQ&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=24'
,'https://www.youtube.com/watch?v=p_oR9MhXKCg&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=25'
,'https://www.youtube.com/watch?v=7ISGhVY7PB4&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=26'
,'https://www.youtube.com/watch?v=FbL2wSnemQs&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=7'
,'https://www.youtube.com/watch?v=CyFnMATthAk&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=27'
,'https://www.youtube.com/watch?v=l3xcKK-Wf98&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=10'
,'https://www.youtube.com/watch?v=4OBiRe6LXdw&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=28'
,'https://www.youtube.com/watch?v=H3gPrw319Ug&feature=youtu.be'
,'https://www.youtube.com/watch?v=lsoFVAbRWgQ&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=9'
,'https://www.youtube.com/watch?v=0tYHvo2fnow&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=29'
,'https://www.youtube.com/watch?v=m5Nu2OCT6Qw&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=30'
,'https://www.youtube.com/watch?v=QT9gOv0T1YM&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=12'
,'https://www.youtube.com/watch?v=Drvod5Q7kMc&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=5'
,'https://www.youtube.com/watch?v=7jOVTo_KSqo&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=11'
,'https://www.youtube.com/watch?v=bmrqmDazXDE&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=4'
,'https://www.youtube.com/watch?v=hZaG5Te4SZ4&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=3'
,'https://www.youtube.com/watch?v=-y0q9MrItyc&list=PLW1XlJ-Yzv-OexmU9VcolJRi4lkCQrXcl&index=2'
,'https://www.youtube.com/watch?v=fsdaCTHPMG4&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=32'
,'https://www.youtube.com/watch?v=t0Wgtt7vTzE&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq'
,'https://www.youtube.com/watch?v=gs2h9BvWWxE&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=34'
,'https://www.youtube.com/watch?v=wDh8pPXkR80&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=31'
,'https://www.youtube.com/watch?v=Bvcv5RWDePk&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=2'
,'https://www.youtube.com/watch?v=WuN0OJ1WP6s&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=3'
,'https://www.youtube.com/watch?v=X1VY-5TnHHc&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=4'
,'https://www.youtube.com/watch?v=88_NWvbvOp0&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=5'
,'https://www.youtube.com/watch?v=7ucmcPh5PA8&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=6'
,'https://www.youtube.com/watch?v=tLMHO2BbKlg&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=7'
,'https://www.youtube.com/watch?v=J1rqd-2I-Q4&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=8'
,'https://www.youtube.com/watch?v=qp04QjC-cts&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=23'
,'https://www.youtube.com/watch?v=u_cTmW5m6Hc&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=9'
,'https://www.youtube.com/watch?v=qOD4Q6Ia5Zk&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=10'
,'https://www.youtube.com/watch?v=nh_HU1Kaz2w&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=33'
,'https://www.youtube.com/watch?v=_iRRtB0hgAA&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=11'
,'https://www.youtube.com/watch?v=WJ866ur8r6g&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=12'
,'https://www.youtube.com/watch?v=vkDNE0CL4-c&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=13'
,'https://www.youtube.com/watch?v=kT8mMBRnE_I&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=14'
,'https://www.youtube.com/watch?v=17-3a8yC_j8&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=22'
,'https://www.youtube.com/watch?v=kN3BPBLlNg8&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=21'
,'https://www.youtube.com/watch?v=O7qcSCkh0cw&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=27'
,'https://www.youtube.com/watch?v=lj0_apqp4zs&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=15'
,'https://www.youtube.com/watch?v=arqkPE3Dxhc&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=16'
,'https://www.youtube.com/watch?v=J9zWKEhGX0c&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=17'
,'https://www.youtube.com/watch?v=4aC8Le5TFQo&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=26'
,'https://www.youtube.com/watch?v=KvbHD65cDqA&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=44'
,'https://www.youtube.com/watch?v=qQSQm2uq0B8&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=28'
,'https://www.youtube.com/watch?v=4Z6JwFZdu-w&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=24'
,'https://www.youtube.com/watch?v=xbHQ9T5WjlQ&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=29'
,'https://www.youtube.com/watch?v=07nVNo14uJY&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=45'
,'https://www.youtube.com/watch?v=43VXDjFbLVM&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=46'
,'https://www.youtube.com/watch?v=lR91dT6nTTw&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=18'
,'https://www.youtube.com/watch?v=JHb_EzQlYCk&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=25'
,'https://www.youtube.com/watch?v=CM37aNcgDak&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=19'
,'https://www.youtube.com/watch?v=TQdWHhtOhO0&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=20'
,'https://www.youtube.com/watch?v=TP_fNb0MCCc&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=40'
,'https://www.youtube.com/watch?v=TjxkVq3uGcQ&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=43'
,'https://www.youtube.com/watch?v=LqlU8XN_xmc&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=35'
,'https://www.youtube.com/watch?v=ubkW-6yXh9o&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=42'
,'https://www.youtube.com/watch?v=ncMi-cJqJo8&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=36'
,'https://www.youtube.com/watch?v=DTpXdTLxj6c&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=37'
,'https://www.youtube.com/watch?v=ZD5E2QMYwEg&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=38'
,'https://www.youtube.com/watch?v=amsiRxFH6c4&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=41'
,'https://www.youtube.com/watch?v=VUCvBZ532Y8&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=39'
,'https://www.youtube.com/watch?v=A2Nn-M-tIN8&list=PLW1XlJ-Yzv-OwN65cGdHDE4LTIUlgleQq&index=30'
,'https://www.youtube.com/watch?v=pWBTwxsmTAE&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=1'
,'https://www.youtube.com/watch?v=V9whDAc_Ayc&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=2'
,'https://www.youtube.com/watch?v=PwRyUzINEhA&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=3'
,'https://www.youtube.com/watch?v=jZ1qjkftxLE&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=4'
,'https://www.youtube.com/watch?v=_DyTaYNw0i8&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=5'
,'https://www.youtube.com/watch?v=0nPBtA4jA18&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=6'
,'https://www.youtube.com/watch?v=MeSS0eVuUt4&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=7'
,'https://www.youtube.com/watch?v=m7cXbuueZgg&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=8'
,'https://www.youtube.com/watch?v=45DdMW88jdg&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=9'
,'https://www.youtube.com/watch?v=n4ojECl70Kw&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=10'
,'https://www.youtube.com/watch?v=DfW03XK7lME&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=11'
,'https://www.youtube.com/watch?v=4tqCU3wLkh4&list=PLW1XlJ-Yzv-P3-gDyxdo7gpQiD_zgwoqQ&index=12']
for link in webPage:
    print(link)
    getUrls(link)
