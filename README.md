# Project Overview

This project was created by synthesizing the MATLAB code from the study at [this link](https://dergipark.org.tr/tr/download/article-file/810165) with ChatGPT. The code primarily uses the "Inter-City Distance Chart" table from the General Directorate of Highways. This table has been converted to a CSV file to be used in Python. Subsequently, the names of the cities on the map of Turkey were edited in SVG format.

## Code Operation

**TPORT Route Calculator**: When the TPORT route calculator file is executed, it requests input from the cities in the city distance file. The city name should be in all uppercase letters and include Turkish characters (example: DİYARBAKIR). After the input, the TPORT algorithm runs, calculates the required cost, and prints it on the screen. The corresponding route is listed in the `rota.txt` file as a sequence of city names.

**Draw SVG**: When the draw svg file is executed, dots are added to Turkey.svg based on the city names in the rota.txt file, starting from the first city and chaining to the next. It is then saved as Turkey_route.svg. This allows the route to be visually tracked.

## Additional Information

The project was developed using Python and relevant libraries. City distances have been edited in the CSV file and integrated into the project. For the visualization process, an SVG format map is used to present the route more clearly.

**Dependencies**: To ensure the code runs correctly, install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

////////////////////////////////////////////////////////////////////////////////

# Proje Özeti

Bu proje, [bu bağlantıdaki](https://dergipark.org.tr/tr/download/article-file/810165) çalışmadaki MATLAB kodunun ChatGPT ile sentezlenerek kullanılması ile oluşturulmuştur. Kod, temel olarak Karayolları Genel Müdürlüğünün "İller Arası Mesafe Cetveli" isimli tablosunu kullanır. Bu tablo, CSV dosyasına dönüştürülerek Python'da kullanılabilir hale getirilmiştir. Ardından Türkiye haritası SVG formatında il isimleri düzenlenmiştir.

## Kodun Çalışması

**TPORT Route Calculator**: TPORT route calculator dosyası çalıştırılınca, ilmesafe dosyasındaki illerden bir girdi ister. İl ismi tamamen büyük harf ve Türkçe karakter içermelidir (örnek: DİYARBAKIR). Girdiden sonra TPORT algoritması çalıştırılarak gerekli maliyet hesabı yapılır ve ekrana yazdırılır. İlgili rota, `rota.txt` dosyasına il isimleri sıralaması şeklinde listelenir.

**Draw SVG**: Draw svg dosyası çalıştırıldığında, rota.txt dosyasındaki il isimleri ilk ilden sonraki ile, ondan sonraki ile zincirleme şekilde Türkiye.svg dosyası üzerine noktalar eklenir ve Türkiye_rota.svg dosyası olarak kaydedilir. Bu sayede, rota görsel olarak da takip edilebilir.

## Ekstra Bilgiler

Proje, Python ve ilgili kütüphaneler kullanılarak geliştirilmiştir. İl mesafeleri CSV dosyasında düzenlenmiş ve projeye entegre edilmiştir. Görselleştirme işlemi için SVG formatında harita kullanılarak, rotanın daha anlaşılır bir şekilde sunulması sağlanmıştır.

**Bağımlılıklar**: Kodun doğru çalışması için gerekli bağlılıkları şu komut ile yükleyiniz:

```bash
pip install -r requirements.txt
```


