## Kodland Level-3 için geliştirilen Discord Botuna Hoş Geldiniz!

![Kodland Logo](https://github.com/user-attachments/assets/fe273402-4a55-4bd3-b998-54d0af8964ef)

### Bot ayaklandırma komutları:

- ``` pip install -r requirements.txt ``` komutunu kullanarak gereksinimler indirilmelidir.
- bot.py dosyası içerisindeki Token kısmına kendi bot tokeninizi giriniz.
- Proje dosyasını indirdikten sonra dosyayı terminalde açaral ```python bot.py ``` komutu çalıştırılarak bot aktif edilir.
- Botun içerisindeki komutların çalıştığından emin olmak için yazılan unit testleri çalıştırmak için ```python run_tests.py ``` yazarak botu test edebilirsiniz.

### Discord içerisinde kullanımı

- ``` !add_task <description> ``` Yeni bir görev eklemek için kullanılır. komut yazıldıktan sonra boş bırakılarak içerisine eklenmek istenen görev yazılır.
![add_task](https://github.com/user-attachments/assets/3144f71b-698e-4dad-8647-52441da7e1dc)
- ``` !show_tasks <empty,0,1> ``` Eklenen görevleri görebilmek için kullanılır. eğer parametre verilmeden girilirse tüm görevleri listeler. 0 parametresi tamamlanmayan, 1 parametresi ise sadece tamamlanan görevleri gösterir.
![show_tasks parametresiz versiyonu](https://github.com/user-attachments/assets/e3a10a6a-c3ba-469e-9363-24a61e2112ad)
![show_tasks 0 parametresi](https://github.com/user-attachments/assets/23244d11-7947-4912-abb1-71db13d7eb25)
![show_tasks 1 parametresi](https://github.com/user-attachments/assets/38496423-0fe4-4c9c-8160-aed2fd88054c)
- ``` !complete_task <id> ``` Girilen id değerini tamamlanmış olarak işaretlemeyi sağlar.

![complete_task](https://github.com/user-attachments/assets/325ef725-a725-4657-92ce-538bd0d53c6f)
-  ``` !delete_task <id> ``` Girilen id değerini silmeyi sağlar.
  
![delete_task](https://github.com/user-attachments/assets/325ef725-a725-4657-92ce-538bd0d53c6f)

## Unit test sonuçları:

![Test Sonuçları](https://github.com/user-attachments/assets/c5b09d57-96cf-45b0-8344-756c043b5041)
