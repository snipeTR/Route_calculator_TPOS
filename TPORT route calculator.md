# Python Koduyla GSP Çözümü

Bu Python kodu, iki şehir arasındaki mesafeleri içeren bir CSV dosyasını okuyarak Gezgin Satıcı Problemi (GSP) için bir çözüm sunmaktadır. Kod, başlangıç şehri olarak kullanıcıdan bir şehir alır, şehirler arasındaki mesafe matrisini oluşturur ve ardından GSP için başlangıç rotasını ve maliyetini hesaplar. Daha sonra, 2-Opt iyileştirme algoritması kullanarak rotayı optimize eder ve yeni maliyeti hesaplar.

### Detaylı Açıklama:

1. **Veri Yükleme ve Dönüştürme:**
   - CSV dosyasını (`ilmesafe.csv`) `iso-8859-9` karakter kodlamasıyla yükler.
   - Mesafeleri bir sözlük yapısına dönüştürür.

2. **Mesafe Matrisi Oluşturma:**
   - Şehirler arasında mesafe matrisini (`D`) oluşturur.

3. **Başlangıç Şehrinin Alınması:**
   - Kullanıcıdan başlangıç şehrini alır ve doğrular.

4. **Rota Hesaplama:**
   - İlk başta basit bir yöntemle rota hesaplanır.
   - Ardından, 2-Opt algoritması kullanılarak rota optimize edilir.

5. **Sonuçların Kaydedilmesi ve Gösterilmesi:**
   - Optimizasyon sonucunda elde edilen rota `rota.txt` dosyasına şehir isimleriyle birlikte virgülle ayrılmış şekilde kaydedilir.
   - Hesaplanan maliyetler ve geliştirilen rota konsola yazdırılır.

### Kodun Etkileştiği Dosyalar:
1. **Girdi Dosyası:**
   - `ilmesafe.csv`: Şehirler arasındaki mesafeleri içeren CSV dosyası.
   
2. **Çıktı Dosyası:**
   - `rota.txt`: Optimizasyon sonucunda elde edilen rota şehirlerinin isimlerini içeren metin dosyası.

Bu kod, temel olarak GSP için başlangıç rotası ve optimize edilmiş rotayı hesaplar ve bu rotaları dosyaya kaydeder.
