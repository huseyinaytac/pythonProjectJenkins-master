Feature: Moderator Kullanici Uygulamaya giris yapabilmelidir.
  Birim Kullanicisi Uygulamaya Giris Yapabilmelidir.
  Birim Yoneticisi Uygulamaya Giris Yapabilmelidir.



  Scenario: Moderator Uygulamaya Giris Yapabiliyor mu?
    Given Kullanici Tarayiciyi açar
    When Kullanici Uygulamanin Url "https://practicetestautomation.com/practice-test-login/" Adresine gider
    And Moderator Kullanici Kullanici Adi "student" ve Sifresini "Password123" girer
    And Login Sayfasinda submit Butonuna tiklar


