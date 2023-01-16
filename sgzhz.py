from sklearn import svm
import os
import cv2
import numpy as np
import pyautogui
import time


path = 'data'
dict = [[143, 494], [286, 653], [1116, 502], [1172, 698], [1331, 454]]
#dict = [[115, 404], [226, 520], [882, 407], [928, 564], [1050, 367]]


imgs = []
labels = []
i = 0
for filepath in os.listdir(path):
    for picture in os.listdir(path + '/' + filepath):
        img = cv2.imread(path + '/' + filepath + '/' + picture, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (100, 100))
        imgs.append(img.flatten().tolist())
        labels.append(i)
    i = i+1


imgs = np.array(imgs)
labels = np.array(labels)


lsvc = svm.SVC()
lsvc.fit(imgs, labels)


pr = 0
while 1:
    ans = []
    img = pyautogui.screenshot(region=(473,192,472,540))
    '''473,192,472,540        370,162,398,417'''
    img = np.array(img)
    img = cv2.resize(img, (100, 100))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img.reshape(1, -1)
    state = lsvc.predict(img)[0]
    if state==0:
        continue
    while 1:
        if state == 0:
            pr = 0
            break
        elif state!=pr:
            pr = state
            ans.append(state)
        img = pyautogui.screenshot(region=(473,192,472,540))
        img = np.array(img)
        img = cv2.resize(img, (100, 100))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img.reshape(1, -1)
        state = lsvc.predict(img)[0]
    print(ans)
    I = ans
    for i in ans:
        pyautogui.moveTo(dict[i-1][0], dict[i-1][1],duration=0.1)
        pyautogui.click()
