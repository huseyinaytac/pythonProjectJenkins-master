import time
from behave import *
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from pageObjectModel.pages.LoginPage import loginPage_Pom
from selenium.webdriver.common.by import By
from pageObjectModel.locators.loginLacators import loginLocator
from pageObjectModel.domFunctions import DomHelper
use_step_matcher("re")

@given('Kullanici Tarayiciyi açar')
def step_impl(context):


    #
    # context.driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
    # context.driver.implicitly_wait(5)



    context.driver=webdriver.Chrome(executable_path="driver/chromedriver.exe")
    context.driver.implicitly_wait(10)




@when('Kullanici Uygulamanin Url "(.*)" Adresine gider')
def step_impl(context,url):
    Url=loginPage_Pom(context.driver)
    Url.Uygulama_Url_Ac(url)



@step('Moderator Kullanici Kullanici Adi "(.*)" ve Sifresini "(.*)" girer')
def step_impl(context,UserName,Password):
    ##Moderator_Kullanici_Adi##
    KullaniciAdi_Sifre = loginPage_Pom(context.driver)
    KullaniciAdi_Sifre.KulaniciAdi_Giris(UserName)
    userName=context.driver.find_element(By.ID,loginLocator.UserName_ID)
    assert "student" == userName.get_attribute('value')
    print(userName.get_attribute('value'))
    ##Kullanici_Sifre##
    KullaniciAdi_Sifre.KullaniciSifre_Giris(Password)
    password=context.driver.find_element(By.ID,loginLocator.Password_ID)
    assert "Password123" == password.get_attribute('value')
    print(password.get_attribute('value'))
    time.sleep(3)



@step("Login Sayfasinda submit Butonuna tiklar")
def step_impl(context):
    LogiBtn = loginPage_Pom(context.driver)
    LogiBtn.Login_Click_Btn()
    time.sleep(5)


