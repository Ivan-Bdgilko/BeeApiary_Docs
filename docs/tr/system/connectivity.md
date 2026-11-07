---
title: "GSM, Wi-Fi ve Bluetooth ile arılık izleme"
description: "Ölçümleri almak için GSM, doğrudan Wi-Fi, arı kovanı ağı ve Bluetooth'u karşılaştırın BeeApiary: bağlantı gereksinimleri ve kullanılabilir geçmiş."
---

# GSM, Wi-Fi ve Bluetooth ile arılık izleme { #_1 }

Arı kovanlarının izlenmesi için, veriler BeeApiary arı kovanı tartım terazileri uygulamaya dört yoldan erişebilir: GSM/SMS, doğrudan Wi-Fi bağlantısı, arı kovanı Wi-Fi ağı veya Bluetooth aracılığıyla. Yerel ve uzaktan izleme arasındaki seçim, telefonun konumuna ve tartı terazisinin yakınındaki mevcut bağlantıya bağlıdır.

| Kanal | Telefon konumu | Gereksinimler | Veriler uygulamaya nasıl ulaşır? |
|---|---|---|---|
| [GSM ve SMS](gsm-and-sms.md) | Mobil kapsama alanı olan her yerde | Cihazda temel SMS planına sahip bir SIM kart; uygulama için SMS izni | Uygulama sıkıştırılmış SMS'leri otomatik işler; mobil internet gerekmez. [GSM kurulumu](../guides/configure-gsm.md) |
| [Cihaz erişim noktasına doğrudan bağlantı](local-wifi.md#direct-access-point) | Cihazın yakınında | Cihazı manyetik anahtarla etkinleştirin ve `apiary_net` mevcut aralık dahilinde, genellikle yaklaşık bir dakika; SIM veya internet gerekmez | Uygulama cihazı bulur, arşivi almak için izin ister ve onaylandıktan sonra verileri içe aktarır. [Arşivi indir](../guides/download-archive.md) |
| [Arı kovanı Wi-Fi ağı üzerinden yönlendirme](local-wifi.md#apiary-wifi-routing) | İnternet erişimi olan her yerde | Cihazın yakınında İnternet erişimi olan yapılandırılmış bir Wi-Fi ağı bulunmalıdır | Veriler uygulamaya otomatik olarak yönlendirilir; her cihaz için ayrı bir SIM karta gerek yoktur. [Wi-Fi kurulumu](../guides/configure-wifi-sync.md) |
| [Bluetooth](bluetooth.md) | Yakınlarda, Bluetooth menzili dahilinde | **BLE info**, BLE taraması ve uygulama arka plan işlemi etkinleştirildi; zaman senkronize edilir; SIM kart veya İnternet gerekmez | Uygulama mevcut verileri otomatik olarak senkronize eder ve mevcut geçmişi geri yükleyebilir. [Bluetooth kurulumu](../guides/configure-bluetooth-sync.md) |

## GSM ve SMS

Normal SMS'ler uygulama olmadan okunabilir; uygulama sıkıştırılmış mesajları ölçüm olarak kaydeder. [SMS biçimleri](gsm-and-sms.md).

## Cihaza Doğrudan Bağlantı

Bağlı telefon arşivi yalnızca kullanıcı onayından sonra alır. [Erişim noktasına bağlanma](../guides/configure-local-wifi.md).

## Arı Kovanı Wi-Fi Ağı Üzerinden Yönlendirme

Kurulumdan önce uygulama cihazdan SMS veya doğrudan arşiv indirme yoluyla en az bir kez veri almış olmalıdır. Aktarma hizmeti kalıcı depolama değildir; kopyalar tartıda ve telefonda kalır. Hizmet kararsız veya ücretli olabilir; [uyumluluğu ve koşulları](../guides/configure-wifi-sync.md) kontrol edin.

## Bluetooth

Geçmiş alma etkinse eksik veriler bir sonraki başarılı bağlantıda tamamlanabilir. [Çalışma ve uyumluluk](bluetooth.md).

## Bağlantı Olmadan Çalıştırma

Herhangi bir iletişim kanalının geçici veya tamamen kaybolması ölçümleri durdurmaz: cihaz bunları microSD'ye kaydetmeye devam eder. Bağlantı yeniden kurulduğunda uygulama kaçırılan verileri alabilir ancak mevcut geçmiş derinliği seçilen kanala bağlıdır.

| Kanal | Bağlantı yeniden kurulduktan sonra mevcut olan geçmiş | Not |
|---|---|---|
| GSM ve SMS | 2 ila 12 saat | Yapılandırılmış SMS iletim planına bağlıdır |
| Cihaz erişim noktasına doğrudan bağlantı | 1 yıla kadar | İlgili kayıtların yerel arşivde mevcut olması durumunda veriler indirilebilir |
| Bluetooth | 1 gün ila 1 hafta | Geçmiş alma ayarına ve mevcut kayıtlara bağlıdır |
| Arı kovanı Wi-Fi ağı üzerinden yönlendirme | Geçmiş kullanılamıyor | Çevrimiçi geçiş mevcut verileri aktarır ancak sunucuda saklamaz |

Bu sınırlar yalnızca belirli bir kanal aracılığıyla geri yüklenebilecek kaçırılan veri miktarı için geçerlidir. Yerel [microSD arşivi](data-storage.md) bir yıllık depolama sınırı yoktur: derinliği yalnızca cihazın beklenen hizmet ömrü boyunca yeterli olan kart kapasitesiyle sınırlıdır. Gerekirse veriler doğrudan microSD karttan da okunabilir.
