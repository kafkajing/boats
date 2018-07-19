import pyautogui as pag
import time,pyperclip,random
pag.FAILSAFE = True
print('程序会在三秒后开始运行，现在快去打开微信并把它全屏。')
time.sleep(3)
qun_num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#在这里改班的序号
qunlist = []
for z in range(len(qun_num)):
    qunlist.append('摄影入门【42期'+str(qun_num[z])+'班】')
    #在这里，改群的名字和期数
for x in qunlist:
    pyperclip.copy(x)
    pag.moveTo(200,40)
    pag.click()
    pag.hotkey('ctrl','a')
    pag.hotkey('ctrl','v')
    time.sleep(1.5)
    pag.moveTo(200,100)
    pag.click()
    time.sleep(1)
    # pag.moveTo(1420,40)
    # pag.click()

    for x in range(14):
        #在这修改班级人数上限。除以6就对啦！
        time.sleep(1)    
        pag.moveTo(1420,40)
        pag.click()
        time.sleep(0.5)
        
        pag.moveTo(1280,140)
        time.sleep(0.5)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(680,320)
        pag.click()      
        pag.moveTo(680,400)
        pag.click()
        pag.moveTo(680,460)
        pag.click()
        pag.moveTo(680,520)
        pag.click()
        pag.moveTo(680,580)
        pag.click()
        pag.moveTo(680,640)
        pag.click()
        time.sleep(0.5)
        pag.moveTo(880,640)
        pag.click()
        time.sleep(0.8)
        pag.moveTo(750,500)

        pag.click()
        time.sleep(1)