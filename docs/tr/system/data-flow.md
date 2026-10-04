---
title: "Kovan verileri telefona nasıl ulaşır"
description: "Nasıl BeeApiary Mevcut okumaları, geçmişi ve grafikleri görüntülemek için arı kovanı verilerini ölçer, saklar ve telefonunuza aktarır."
---

# Kovan verileri telefona nasıl ulaşır { #_1 }

BeeApiary arı kovanı izleme, ölçümü, yerel depolamayı ve uygulamaya veri aktarımını kapsar. Aşağıdaki adımlar, cihazdaki bir ölçümden telefonunuzdaki mevcut okumalara, geçmişe ve grafiklere kadar olan yolu gösterir.

1. Her saat başında, BeeApiary arı kovanı tartım terazileri yapılandırılmış ölçümleri alır.
2. Sonuç, kart mevcut olduğunda yerel microSD arşivine kaydedilir.
3. Cihaz verileri yapılandırılan kanal üzerinden sunar:

    - programa göre düzenli veya kısa bir SMS mesajı gönderir;
    - verileri arı kovanı Wi-Fi ağı üzerinden yönlendirir;
    - [mevcut verileri Bluetooth üzerinden iletir](bluetooth.md) telefon yakında olduğunda;
    - Kullanıcı onayının ardından arşivi kendi erişim noktası üzerinden uygulamaya sağlar.

4. Uygulama alınan değerleri tanır ve telefonun yerel depolamasına ekler.
5. Kullanıcı mevcut değerleri, geçmişi ve grafikleri görüntüler.

GSM, Wi-Fi, Bluetooth veya yakındaki bir telefonun olmaması, çekirdek ölçüm sürecini durdurmaz. Bağlantı mevcut olduğunda veriler uygulamaya aktarılabilir.

Veriler Wi-Fi üzerinden uzaktan yönlendirildiğinde, çevrimiçi geçiş onu saklamaz. Kalıcı kopyalar arşivde kalır. BeeApiary arı kovanı tartı terazisinin hafızasında ve kullanıcının telefonunda.

Kanal karşılaştırması için bkz. [Uygulamada Veri Alma](connectivity.md).

Uzak kanalı yapılandırmak için bkz. [Arı Kovanı Wi-Fi Ağı Üzerinden Senkronizasyon](../guides/configure-wifi-sync.md).

Yerel otomatik kanalı yapılandırmak için bkz. [Bluetooth Senkronizasyonu](../guides/configure-bluetooth-sync.md).
