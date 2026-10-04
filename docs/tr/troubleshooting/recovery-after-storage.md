# Uzun Süreli Saklamanın Ardından Cihazı Kurtarma

Uzun süreli saklamanın ardından pil tamamen boşalabilir ve cihaz normal güç bağlantısına yanıt vermeyebilir. 18650 hücresinin voltajı aşağıdaysa `3,5 В`, cihazı aşağıdaki sırayla kurtarın.

!!! danger "Pil polaritesi"
    Pili çıkarmadan önce, `+` ve `-` hücre ve tutucu üzerindeki işaretler. Doğru yönü hatırlayın veya fotoğraflayın. Pili ters kutupla takmak cihaza kalıcı hasar verebilir.

1. Pili cihazdan çıkarın.
2. 18650 hücre için tasarlanmış ayrı bir şarj cihazında şarj edin.
3. Şarj ettikten sonra akü voltajını kontrol edin. Cihaza yalnızca voltaj düşük olduğunda takın. `4,0 В` veya daha yüksek.
4. Pili, işaretli kutuplara dikkat ederek takın.
5. Standart bir harici güç kaynağını, Güç Dağıtımı (PD) hızlı şarjı olmayan cihazın USB Type-C bağlantı noktasına bağlayın. USB Tip A bağlantı noktasına ve USB Tip A'dan USB Tip C'ye kabloya sahip bir şarj cihazı kullanın; USB Type-C'den USB Type-C'ye kablo kullanılması önerilmez.
6. Pil takılı ve harici güç bağlıyken, [cihazı manyetik anahtarla etkinleştirin](../device/installation.md#activation-reset).
7. Saati şu yollardan biriyle senkronize edin:

    - [Wi-Fi üzerinden cihazın erişim noktasına bağlanın](../guides/configure-local-wifi.md) ve ana sayfasını açın; bu yöntem varsayılan olarak mevcuttur;
    - [Bluetooth senkronizasyonunu ayarla](../guides/configure-bluetooth-sync.md), aç BeeApiary uygulamasını kullanın ve telefonu cihazın yakınında bırakın; bu yöntem yalnızca ilgili ayarlar hem cihazda hem de uygulamada etkinleştirildiğinde çalışır.

8. Tarih ve saatin doğru olduğundan ve son senkronizasyon zaman damgasının güncellendiğinden emin olun.

Güç ve zaman geri geldikten sonra cihaz normal çalışmaya hazırdır.

Ayrıca bakınız [Güç ve Şarj](../device/power.md) ve [Zaman Senkronizasyonu](../system/time-synchronization.md).
