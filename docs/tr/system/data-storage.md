# Veri Depolama

 BeeApiary arı kovanı tartım terazileri GSM mevcut olsun veya olmasın verileri microSD'ye kaydeder. bir `YEARxx` dizin, her ay için tarih, saat ve mevcut okumaları içeren CSV dosyalarıyla birlikte her yıl için oluşturulur.

CSV dosyası şunları içerebilir:

- `Date`, `Time`;
- `Weight[Kg]`;
- `T1 [°C]`, `T2 [°C]`ve ek sıcaklıklar;
- pil şarjı;
- basınç ve nem;
- GSM RSSI'sı;
- ürün yazılımı hizmeti meta verileri.

Sütunlar cihaz konfigürasyonuna ve donanım yazılımı sürümüne bağlıdır. Ölçümler yılda yaklaşık 2 MB, hizmet günlükleri ise yılda yaklaşık 40-50 MB kullanır.

Verileri almak için bkz. [Arşivi İndir](../guides/download-archive.md).
