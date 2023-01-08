from pageObjectModel.domFunctions import DomHelper
from pageObjectModel.locators.loginLacators import loginLocator


class loginPage_Pom():
    def __init__(self,driver):
        self.driver=driver

    def Uygulama_Url_Ac(self,Url):
        url=DomHelper(self.driver)
        url.open_Page(Url)

    def KulaniciAdi_Giris(self,Usename):
        kullaniciAdi=DomHelper(self.driver)
        kullaniciAdi.send_keys_ID(loginLocator.UserName_ID,Usename)

    def KullaniciSifre_Giris(self,Password):
        kullaniciSifre=DomHelper(self.driver)
        kullaniciSifre.send_keys_ID(loginLocator.Password_ID,Password)

    def Login_Click_Btn(self):
        loginBtn_ID = "submit"
        loginBtn=DomHelper(self.driver)
        loginBtn.click_button_ID(loginBtn_ID)

