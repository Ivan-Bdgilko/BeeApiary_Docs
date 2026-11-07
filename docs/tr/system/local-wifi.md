---
title: "Wi-Fi özellikli kovan tartıları — doğrudan bağlantı ve ağ bağlantısı"
description: "Bağlan BeeApiary Wi-Fi üzerinden arı kovanı tartım terazileri: telefonunuz için doğrudan erişim noktası ve arı kovanı ağı üzerinden uzaktan aktarım."
---

# Wi-Fi özellikli kovan tartıları — doğrudan bağlantı ve ağ bağlantısı { #wi-fi- }

BeeApiary Wi-Fi özellikli arı kovanı tartım terazileri, veri almanın iki yolunu destekler: cihazın erişim noktasına (AP) doğrudan telefon bağlantısı ve arı kovanı Wi-Fi ağı (STA) üzerinden iletim. İlk yöntem tartı terazisinin yakınında çalışır; ikincisi, İnternet bağlantısı mevcut olduğunda uzaktan veri erişimi sağlar.

## Cihaza Doğrudan Bağlantı { #direct-access-point }

Manyetik anahtarla etkinleştirildikten sonra cihaz geçici olarak yerel bir erişim noktası oluşturur. Genellikle yaklaşık bir dakika boyunca kullanılabilir, ancak bu aralık ayarlardan değiştirilebilir.

Varsayılan ayarlar:

```text
SSID: apiary_net
Şifre: apiary_wifi
Web arayüzü: http://192.168.4.1
```

Yerel bağlantı aracılığıyla şunları yapabilirsiniz:

- uygulamanın ölçüm arşivini almasına izin verin;
- web arayüzünü açın;
- sahibinin telefon numarasını ve programını yapılandırın;
- şarj seviyesini ve donanım yazılımı sürümünü görüntüleyin;
- microSD karttaki dosyalara erişmek için FTP'yi kullanın.

Telefon bağlandıktan sonra `apiary_net`, uygulama cihazı bulur ve istemi görüntüler **"Cihaz yakında. Arşiv alınsın mı?"**. Veriler yalnızca kullanıcı isteği onayladıktan sonra indirilir.

!!! warning "Şifreyi değiştir"
    Varsayılan şifre herkesçe bilinmektedir. İlk kontrolden sonra 32 karaktere kadar kendi şifrenizi belirleyin.

Ayrıntılı prosedürler:

- [Cihaz Erişim Noktasına Bağlan](../guides/configure-local-wifi.md);
- [arşivi uygulamaya indirin](../guides/download-archive.md);
- [ek cihaz ayarlarını görüntüle](../device/additional-settings.md).

## Arı Kovanı Wi-Fi Ağı Üzerinden Yönlendirme { #apiary-wifi-routing }

Cihaz, arı kovanındaki mevcut Wi-Fi ağına bağlanabiliyor ve verileri İnternet üzerinden sahibinin uygulamasına otomatik olarak gönderebiliyor. Telefon internet erişimi olan her yerde olabilir.

Bu yöntem, her cihazda ayrı bir SIM kart gerektirmez, ancak cihazın yakınında İnternet erişimi olan yapılandırılmış bir Wi-Fi ağının bulunması gerekir.

### Kurulum Nasıl Çalışır?

Uygulamada zaten bilinen cihazı kaydedin: servis kimlikleri ve anahtarları oluşturur. Ardından arılık ağı ayarlarını telefondan cihazın `apiary_net` erişim noktası üzerinden aktarın.

Manyetik anahtarla yeniden başlatmanın ardından veya bir sonraki programlanmış saatlik döngü sırasında cihaz, otomatik iletim için yapılandırılmış ağı kullanır. Artık telefonun yakında olmasına gerek yok.

### Gereksinimler

- cihaz uygulamaya önceden eklenmiş olmalıdır;
- uygulamanın verilerini SMS veya doğrudan arşiv indirme yoluyla en az bir kez aldığı;
- telefonun kayıt sırasında İnternet erişimi vardır;
- cihazın yakınında İnternet erişimi olan bir Wi-Fi ağı mevcut;
- kullanıcı o ağın adını ve şifresini bilir.

Çevrim içi aktarma hizmeti kalıcı depolama değildir: veriler tartıda ve telefonda kalır. Hizmet kararsızlaşabilir veya ücretli olabilir; cihaz uyumluluğu ve diğer koşullar kılavuzda açıklanır.

Adım adım prosedür için bkz. [Arı Kovanı Wi-Fi Ağı Aracılığıyla Senkronizasyonu Ayarlama](../guides/configure-wifi-sync.md).
