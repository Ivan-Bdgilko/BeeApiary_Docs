---
title: "GSM, Wi-Fi ve Bluetooth ile arılık izleme"
description: "Ölçümleri almak için GSM, doğrudan Wi-Fi, arı kovanı ağı ve Bluetooth'u karşılaştırın BeeApiary: bağlantı gereksinimleri ve kullanılabilir geçmiş."
---

# GSM, Wi-Fi ve Bluetooth ile arılık izleme { #_1 }

Arı kovanlarının izlenmesi için, veriler BeeApiary arı kovanı tartım terazileri uygulamaya dört yoldan erişebilir: GSM/SMS, doğrudan Wi-Fi bağlantısı, arı kovanı Wi-Fi ağı veya Bluetooth aracılığıyla. Yerel ve uzaktan izleme arasındaki seçim, telefonun konumuna ve tartı terazisinin yakınındaki mevcut bağlantıya bağlıdır.

| Kanal | Telefon konumu | Gereksinimler | Veriler uygulamaya nasıl ulaşır? |
|---|---|---|---|
| [GSM ve SMS](gsm-and-sms.md) | Mobil kapsama alanı olan her yerde | Cihazda temel SMS planına sahip bir SIM kart | Uygulama, SMS mesajlarını otomatik olarak işler; mobil internet gerekli değildir |
| [Cihaz erişim noktasına doğrudan bağlantı](local-wifi.md#direct-access-point) | Cihazın yakınında | Cihazı manyetik anahtarla etkinleştirin ve `apiary_net` mevcut aralık dahilinde, genellikle yaklaşık bir dakika | Uygulama cihazı bulur, arşivi almak için izin ister ve onaylandıktan sonra verileri içe aktarır |
| [Arı kovanı Wi-Fi ağı üzerinden yönlendirme](local-wifi.md#apiary-wifi-routing) | İnternet erişimi olan her yerde | Cihazın yakınında İnternet erişimi olan yapılandırılmış bir Wi-Fi ağı bulunmalıdır | Veriler uygulamaya otomatik olarak yönlendirilir; her cihaz için ayrı bir SIM karta gerek yoktur |
| [Bluetooth](bluetooth.md) | Yakınlarda, Bluetooth menzili dahilinde | **BLE info**, BLE taraması ve uygulama arka plan işlemi etkinleştirildi; zaman senkronize edilir; SIM kart veya İnternet gerekmez | Uygulama mevcut verileri otomatik olarak senkronize eder ve mevcut geçmişi geri yükleyebilir |

## GSM ve SMS

Cihaz, mobil İnternet olmadan düzenli veya kompakt SMS mesajları gönderir. Uygulama, kısa mesajları tanır ve ölçümleri otomatik olarak telefonun yerel belleğine ekler.

## Cihaza Doğrudan Bağlantı

Manyetik anahtarla etkinleştirildikten sonra cihaz geçici olarak `apiary_net` erişim noktası. Ona bağlı bir telefonun SIM karta veya İnternet erişimine ihtiyacı yoktur. Uygulama, cihazı otomatik olarak bulur ancak arşivi yalnızca kullanıcı isteği onayladıktan sonra indirir.

Ayrıntılı prosedür için bkz. [Arşivi İndir](../guides/download-archive.md).

## Arı Kovanı Wi-Fi Ağı Üzerinden Yönlendirme

Cihaz, arı kovanında İnternet erişimi olan mevcut bir Wi-Fi ağını kullanabilir. Cihaz sahibi, her cihaz için ayrı bir SIM karta ihtiyaç duymadan, verileri uygulama üzerinden uzaktan alır.

İlk kurulumdan önce uygulamanın cihazdan SMS veya doğrudan arşiv indirme yoluyla en az bir kez veri almış olması gerekir. Kayıt internet erişimi olan bir telefonda tamamlanır ve hazırlanan Wi-Fi ve bulut ayarları daha sonra cihaza aktarılır. `apiary_net` erişim noktası.

Çevrimiçi geçiş veri saklamaz. Kalıcı kopyalar arşivde kalır. BeeApiary arı kovanı tartı terazisinin hafızasında ve kullanıcının telefonunda.

Ayrıntılı prosedür için bkz. [Arı Kovanı Wi-Fi Ağı Aracılığıyla Senkronizasyonu Ayarlama](../guides/configure-wifi-sync.md).

## Bluetooth

Telefon Bluetooth menzilinde olduğunda uygulama mevcut verileri otomatik olarak senkronize eder. Bunun için SIM kart, mobil İnternet veya mobil cihazın etkinleştirilmesi gerekmez. `apiary_net` erişim noktası. Geçmişe erişim etkinleştirildiğinde, bir sonraki başarılı bağlantı sırasında geçici boşluklar doldurulabilir.

Bir açıklama için bkz. [Bluetooth Veri Senkronizasyonu](bluetooth.md). Pratik prosedür için bkz. [Bluetooth Senkronizasyonunu Ayarlama](../guides/configure-bluetooth-sync.md).

## Bağlantı Olmadan Çalıştırma

Herhangi bir iletişim kanalının geçici veya tamamen kaybolması ölçümleri durdurmaz: cihaz bunları microSD'ye kaydetmeye devam eder. Bağlantı yeniden kurulduğunda uygulama kaçırılan verileri alabilir ancak mevcut geçmiş derinliği seçilen kanala bağlıdır.

| Kanal | Bağlantı yeniden kurulduktan sonra mevcut olan geçmiş | Not |
|---|---|---|
| GSM ve SMS | 2 ila 12 saat | Yapılandırılmış SMS iletim planına bağlıdır |
| Cihaz erişim noktasına doğrudan bağlantı | 1 yıla kadar | İlgili kayıtların yerel arşivde mevcut olması durumunda veriler indirilebilir |
| Bluetooth | 1 gün ila 1 hafta | Geçmiş alma ayarına ve mevcut kayıtlara bağlıdır |
| Arı kovanı Wi-Fi ağı üzerinden yönlendirme | Geçmiş kullanılamıyor | Çevrimiçi geçiş mevcut verileri aktarır ancak sunucuda saklamaz |

Bu sınırlar yalnızca belirli bir kanal aracılığıyla geri yüklenebilecek kaçırılan veri miktarı için geçerlidir. Yerel [microSD arşivi](data-storage.md) bir yıllık depolama sınırı yoktur: derinliği yalnızca cihazın beklenen hizmet ömrü boyunca yeterli olan kart kapasitesiyle sınırlıdır. Gerekirse veriler doğrudan microSD karttan da okunabilir.
