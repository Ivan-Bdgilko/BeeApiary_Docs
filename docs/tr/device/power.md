# Güç ve Şarj

Cihaz bir veya iki 18650 hücreden çalışır ve USB Type-C üzerinden şarj olur. Güç kaynağı bir şarj cihazı, bir güç bankası veya isteğe bağlı bir güneş paneli olabilir.

!!! note "Şarj cihazı ve kablo seçimi"
    Cihaz, USB Güç Dağıtımı (PD) dahil olmak üzere hızlı şarjı desteklemez. USB Type-A bağlantı noktası ve USB Type-A–USB Type-C kablosuyla standart bir güç kaynağı kullanın. Şarj için USB Type-C–USB Type-C kablosunun kullanılması önerilmez.

![USB Type-C güç bağlantı noktasını açın](../../assets/common/device/power/open-usb-type-c-port.jpeg){ .doc-photo }

Şarj ettikten sonra koruyucu bağlantı noktası kapağını kapatın:

![Güç bağlantı noktasının üzerinde kapalı koruyucu kapak](../../assets/common/device/power/closed-usb-type-c-cover.jpeg){ .doc-photo }

- pil tamamen şarj olduğunda ve harici güç hala bağlı olduğunda mavi gösterge yanık kalır;
- şarj seviyesi SMS mesajlarında ve web arayüzünün genel ayarlarında gösterilir;

  ![Web arayüzünde pil şarjı](../../assets/en/device/power/battery-charge-status.png){ .doc-screenshot }

- %20'nin altında cihaz güç tasarrufu moduna girer, düzenli ölçümleri ve SMS mesajlarını durdurur ve şarj seviyesini periyodik olarak kontrol eder;
- Kritik bir deşarjın ardından akü bağlantısı otomatik olarak kesilir ve [zaman senkronizasyonu](../system/time-synchronization.md) şarj edildikten sonra gerekebilir.

!!! warning "Uzun süreli depolamadan sonra"
    Akü voltajı aşağıdaysa `3,5 В`aygıtı yalnızca USB bağlantı noktasını kullanarak geri yüklemeye çalışmayın. Takip et [uzun süreli depolamadan sonra kurtarma prosedürü](../troubleshooting/recovery-after-storage.md).

!!! danger
    Cihazı 18650 hücresi takılı olmadan kullanmayın. Değiştirirken polariteye kesinlikle dikkat edin: yanlış polarite cihaza zarar verecektir.
