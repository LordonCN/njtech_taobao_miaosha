from selenium import webdriver
import time
import datetime

driver = webdriver.Chrome(executable_path=r'D:\PyCharm\Code3.7.3\chromedriver.exe')
# 窗体最大化
driver.maximize_window()

def login(url):#选择一个购物车内的商品
    """登录模块,用于登录淘宝，并选中需要购买的商品按钮，结束"""
    # 获取网页源信息
    driver.get(url)
    # 等浏览器与Selenium完美契合之后再进行下一步动作
    driver.implicitly_wait(2)
    """账号密码登陆: 但是有验证框 需要拖拽"""
    #driver.find_element_by_name("TPL_username").send_keys("187")  # user_pwd
    #driver.find_element_by_name("TPL_password").send_keys("xld")  # user_pwd
    #time.sleep(4)
	#有滑块验证，没加
    #driver.find_element_by_id("J_SubmitStatic").click()  # 寻找id类型的确认
    """扫码登陆(自己扫码)："""
    time.sleep(1)
    driver.find_element_by_id("J_Static2Quick").click()  # 寻找id类型的确认,变换不过去 只能手动了== 哭
    time.sleep(7)
    # 查找购物车按钮的xpath并点击进入购物车
    driver.find_element_by_xpath('//*[@id="mc-menu-hd"]/span[2]').click()
    time.sleep(1)
    """(修改)勾选你需要购买的物品"""
    driver.find_element_by_xpath('//*[@id="J_Item_1294926048057（这里要修改）"]/ul/li[1]/div/div/label').click()#这里要提前修改好
    time.sleep(2)

def buy_good(buy_time):
    """一直循环读取当前的系统时间，如果到了开始秒抢的时间，立马提交订单"""
    while True:
        # 读取系统当前时间
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # 是否到可以购买的时间了
        if now_time <= buy_time:
            try:
                driver.find_element_by_id("J_Go").click()#提交
                time.sleep(0.05)
                # 点击提交订单按钮
                driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()
                # 然后这里你就可以输入密码进行支付了
                break
            except:
                time.sleep(1)
        print(now_time)
        time.sleep(1)

if __name__ == "__main__":
    url = 'https://login.taobao.com/member/login.jhtml'
    login(url=url)
    """（修改）定时购买，可以在每个框中输入支付宝密码"""
    #buy_good('2019-06-18 10:30:00')

    #购买调试测试
    driver.find_element_by_id("J_Go").click()  # 提交
    # 点击提交订单按钮
    driver.find_element_by_xpath('//*[@id="submitOrder_1"]/div/a[2]').click()
