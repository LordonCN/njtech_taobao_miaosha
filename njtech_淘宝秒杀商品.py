import unittest
from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome()
# 窗体最大化
driver.maximize_window()

def login(url):#选择一个购物车内的商品
    '''
    登录模块,用于登录淘宝，并选中需要购买的商品按钮，结束。
    '''
    # 获取网页源信息
    driver.get(url)
    # 等浏览器与Selenium完美契合之后再进行下一步动作
    driver.implicitly_wait(2)
    # 账号密码登陆
    # driver.find_element_by_id("J_Quick2Static").click()  # 寻找id类型的确认
    # driver.find_element_by_name("TPL_username").send_keys("18753015386")  # user_pwd
    # driver.find_element_by_name("TPL_password").send_keys("xlodng")  # user_pwd
    # time.sleep(4)
    # driver.find_element_by_id("J_SubmitStatic").click()  # 寻找id类型的确认
    # 扫码登陆：
    time.sleep(7)
    # 查找购物车按钮的xpath并点击进入购物车
    driver.find_element_by_xpath('//*[@id="mc-menu-hd"]/span[2]').click()
    # 等待4秒
    time.sleep(1)
    # 勾选你需要购买的物品
    #driver.find_element_by_xpath('//*[@id="J_Item_942414149785"]/ul/li[1]/div/div/label').click()
    # time.sleep(1)
    driver.find_element_by_xpath('//*[@id="J_Item_933919061379"]/ul/li[1]/div/div/label').click()
    # 等待5秒
    time.sleep(5)#

def buy_good(buy_time):
    '''
    一直循环读取当前的系统时间，如果到了开始秒抢的时间，立马启动程序开始提交订单
    '''
    while True:
        # 读取系统当前时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print(now_time)
        # 是否到可以购买的时间了
        if now_time == buy_time:
            try:
                # 这一句是判断，是否可以购买了
                driver.find_element_by_id("J_Go").click()#提交
                # 点击提交订单按钮
                #time.sleep()
                driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()
                # 然后你就可以输入密码进行支付了
                 # 结束循环
                break
            except:
                time.sleep(1)
        print(now_time)
        time.sleep(1)

if __name__ == "__main__":
    url = 'https://login.taobao.com/member/login.jhtml'
    login(url=url)
    #buy_good('2018-11-29 14:23:13')
    driver.find_element_by_id("J_Go").click()  # 提交
    # # 点击提交订单按钮
    # time.sleep(0.05)
    driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()