import pyautogui as pag
import time,pyperclip,random
pag.FAILSAFE = True
print('程序会在三秒后开始运行，现在快去打开微信并把它全屏。')
time.sleep(3)
qun_num=[16]
qunlist = ['冷笑话']
# for z in range(len(qun_num)):
#     qunlist.append('摄影入门【38期'+str(qun_num[z])+'班】')
for x in qunlist:
    pyperclip.copy(x)
    pag.moveTo(300,60)
    pag.click()
    pag.hotkey('ctrl','a')
    pag.hotkey('ctrl','v')
    time.sleep(1.5)
    pag.moveTo(300,150)
    pag.click()
    time.sleep(1)
    pag.moveTo(1875,65)
    pag.click()
    for x in range(2):
        time.sleep(2)    
        pag.moveTo(1875,65)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(1875,65)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(1680,220)
        time.sleep(0.5)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(680,400)
        pag.click()        
        pag.moveTo(680,490)
        pag.click()
        pag.moveTo(680,580)
        pag.click()
        pag.moveTo(680,670)
        pag.click()
        pag.moveTo(680,760)
        pag.click()
        pag.moveTo(680,850)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(1200,850)
        pag.click()
        time.sleep(0.8)
        pag.moveTo(1000,650)
        pag.click()