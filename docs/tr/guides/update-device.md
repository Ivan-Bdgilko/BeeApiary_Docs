# BeeApiary kovan tartısının ürün yazılımı nasıl güncellenir

Güncellemeden önce, cihaz nesline ve gerekli arayüz diline uygun ürün yazılımını seçin.

## Ürün yazılımı neslini seçin

| Cihaz | Kaynağı güncelle | Geliştirme durumu |
|---|---|---|
| Ağustos 2026'dan önce üretilmiştir | [Hive_Controller](https://github.com/Ivan-Bdgilko/Hive_Controller) | Önceki sürüm için özellik geliştirme artık desteklenmiyor |
| Ağustos 2026'dan sonra üretilmiştir | [Hive_Controller_Ble](https://github.com/Ivan-Bdgilko/Hive_Controller_Ble) | Yeni sürüm, güncellemeler ve yeni işlevler almaya devam ediyor |

!!! danger "Eski bir cihazı yeni sürüme geçirme"
    Daha önce üretilmiş herhangi bir cihaz yeni yazılım sürümüne geçirilebilir ancak bu, fabrika güncellemesi gerektirir. Şu anda self servis geçiş için basit bir yama bulunmadığından bu sayfadaki standart prosedür, bir cihazın nesiller arasında geçişini sağlamaz.

## Firmware dilini seçin

Her iki nesil de çok dilli yapılar sağlar. Sürüm adındaki sonek dili tanımlar:

| son ek | Dil |
|---|---|
| `-de` | Almanca |
| `-en` | İngilizce |
| `-es` | İspanyolca |
| `-fr` | Fransızca |
| `-pl` | Lehçe |
| `-uk` | Ukraynaca |

İlgili dosyayı indirip yanıp sönerek dili seçin. Dil yapıları yukarıda listelenen depolarda herkese açık olarak mevcuttur ve ihtiyaç duyulması halinde daha sonra daha fazla dil eklenebilir.

## Cihazı microSD kullanarak güncelleyin

1. Cihaz uyku moduna girene kadar bekleyin, ardından microSD kartı çıkarın.
2. Oluştur `/fm` Zaten mevcut değilse, kartın kökündeki dizin.
3. Yerleştirin `Apiary.bin` içindeki dosyayı güncelle `/fm`.
4. MicroSD kartı cihaza tekrar takın.
5. [Cihazı etkinleştirin veya yeniden başlatın](../device/installation.md#activation-reset) manyetik anahtarla.
6. Ölçümleri içeren normal bir SMS mesajını bekleyin; güncelleme genellikle iki dakika kadar sürer.
7. Web arayüzü ana sayfasının alt kısmında donanım yazılımı sürümünü, dil son ekini, yapım tarihini ve saatini ve benzersiz cihaz numarasını kontrol edin.

![Aygıt yazılımı sürümü, dil son eki, oluşturma süresi ve aygıtın web arayüzündeki benzersiz kimlik](../../assets/common/guides/update-device/device-version-build-time-and-id.png){ .doc-screenshot }

Tam sürüm dizesi yerelleştirme son ekini içerir; örneğin `-uk`. Bunu, cihaz nesliniz için depodaki ilgili güncelleme sürümüyle karşılaştırın. Aynı sayfada ayrıca yapım tarihi ve saati ile benzersiz cihaz tanımlayıcısı da gösterilir.

!!! warning "Güncellemeden önce dosyayı kontrol edin"
    Emin olun `Apiary.bin` Cihazınızın üretimi ve gerekli dil için tasarlanmıştır. FTP veya sunucu üzerinden hizmet güncelleme yöntemleri bu prosedürün kapsamı dışındadır.
