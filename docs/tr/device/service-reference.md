# Servis Dokümantasyonu

Bu bölüm, teknik konfigürasyon arşividir. BeeApiary arı kovanı tartı terazileri. XML dosyalarını manuel olarak geri yüklemesi veya incelemesi gereken servis teknisyenleri ve deneyimli kullanıcılar için tasarlanmıştır.

Bazı donanım ve ağ parametrelerinin başlangıç değerleri, söz konusu cihazın konfigürasyonuna ve kurulumuna bağlıdır.

!!! danger "Manuel düzenleme"
    Yanlış donanım pinleri, kalibrasyon değerleri veya servis aralıkları ölçümleri veya cihazın çalışmasını bozabilir. Sıradan değişiklikler için web arayüzünü kullanın. Her zaman bir yedeğini oluşturun `/setting` Dosyaları manuel olarak düzenlemeden önce dizini.

## Güvenli Prosedür

1. Cihaz uyku moduna girene kadar bekleyin. Cihazın standart bir güç düğmesi yoktur: çalışma sırasında ya etkindir ya da hazırda bekletme modundadır.
2. microSD kartı çıkarın ve tam bir kopyasını kaydedin. `/setting` dizin.
3. Bölüm veya nitelik adlarını değiştirmeden XML'i bir metin düzenleyicide düzenleyin.
4. XML'de bir tane olduğundan emin olun `<settings>` kök öğenin ve tüm tırnak işaretlerinin ve kapanış etiketlerinin mevcut olduğunu.
5. Cihaz uykudayken microSD kartı tekrar takın. Güncellenen ayarlar, yapılandırmanın normal şekilde yüklendiği bir sonraki seferde uygulanır; web arayüzü aracılığıyla yapılan bazı değişiklikler de yalnızca yeniden başlatmanın ardından etkili olur.
6. Ölçümleri, iletişimi ve servis günlüğünü kontrol edin. Doğrulama tamamlanana kadar yedeği saklayın.

Kaydederken cihaz dosyayı normalleştirebilir: eksik bölümleri veya nitelikleri ekleyebilir, geri dönüş değerlerini değiştirebilir ve öğe sırasını yeniden yazabilir.

## Dosyalar

- [`/setting/mset.xml`](settings-reference.md) — ağ, GSM, saat, donanım seçenekleri, genel alarmlar ve BLE.
- [`/setting/<hive>.xml`](hive-settings-reference.md) — belirli bir arı kovanı, ağırlık, program, kontrol sıklığı ve eşik alarmları için sensörler.
- [Yapılandırmayı Geri Yükleme](recovery.md) — microSD'nin güvenli değişimi, yedekten geri yükleme ve XML doğrulaması.

Arı kovanı dosya adı şu şekilde belirtilir: `hive1`, `hive2`ve uzantısı olmayan sonraki özellikler. `.xml` Uzantı otomatik olarak eklenir.

## Erişim Düzeyleri

| Etiket | Anlamı |
|---|---|
| `USER` | Değer standart arayüz üzerinden değiştirilebilir. |
| `ADVANCED` | Bunun iletişim veya çalışma mantığı üzerindeki etkisinin anlaşılması gerekir. |
| `SERVICE` | Manuel değişiklikler, cihazı çalışmaz hale getirebilir veya verileri bozabilir. |

Tablolarda, `—` sınırların alan için geçerli olmadığı anlamına gelir. **Başlangıç değeri** belirli bir aygıtın XML'indeki değil, yeni oluşturulan yapılandırmadaki değerdir. **Belirtilmemişse** öznitelik olmadığında kullanılan ve başlangıç değerinden farklı olabilecek değeri açıklar.

## Tarihsel İsimler

Tam XML tanımlayıcıları, hatalar içerseler bile düzeltilmez: `apairy_set`, `sefe_start_interval`, `normal_pecision`ve `calibrate_pecision` aynen yazıldığı gibi kalmalıdır. Yazım `synсhronize` Kiril harfiyle `с` yanlıştır; kullanmak `synchronize`.
