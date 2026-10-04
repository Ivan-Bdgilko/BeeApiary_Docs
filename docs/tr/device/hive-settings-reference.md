# `HIVE*.XML`: arı kovanı Ayarları

Kovan yapılandırması şu konumda saklanır: `/setting/<hive>.xml`. `<hive>` temel adı tarafından belirtilir `hive1`, `hive2`, ve sonraki özellikler [`mset.xml`](settings-reference.md); `.xml` Uzantı otomatik olarak eklenir.

!!! danger "Donanıma bağlı değerler"
    Kopyalamayın `scales` başka bir cihazdan bölüm. Kart pinleri ve kalibrasyon değerleri, donanım sürümüne ve belirli ağırlık sensörleri setine bağlıdır. Yanlış değerler ölçümleri bozabilir veya kullanılamaz hale getirebilir.

Bkz. [güvenli düzenleme kuralları](service-reference.md).

## Otomatik Yeniden Yazma

Dosyayı okuduktan sonra cihaz dosyayı tekrar kaydedebilir:

- mevcut durumdan eksik veya hasarlı bir dosya oluşturulur;
- kayıp `hive`, `thermometer`veya `schedule` bölümler normalleştirmeyi mümkün kılar;
- mevcut bir özellikte eksik bir özellik `scales` veya `thermometer` bölümü bir geri dönüş değeriyle değiştirilir ve normalleştirmeye olanak tanır;
- tamamlandı `scales`, `booster`ve `range_alarmer` bölümler isteğe bağlıdır;
- normalleşme de şunu yazıyor `booster`, `range_alarmer`, `thermometer`ve `schedule` Bazıları kaynak dosyada olmasa bile bölümler.

## `hive`

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `hive_name` | Dahili arı kovanı adı | İsteğe bağlı | Dize; uyumluluk için en fazla 8 ASCII karakteri önerilir | İsim kaynağı `mset.xml`örneğin `hive1` | `hive_<індекс>`; dosya yeniden yazılmak üzere işaretlendi | `ADVANCED` |
| `bus_number` | Dahili veri yolundaki kovan numarası | İsteğe bağlı | Tam sayı; sınırlar denetlenmez | Örnek dizini, `0` ilki için | Örnek dizini; dosya yeniden yazılmak üzere işaretlendi | `SERVICE` |
| `main_device` | Yerel donanım sensörlerine sahip ana cihazı gösterir | İsteğe bağlı | `true`, `false` | `true` yeni oluşturulan bir dosyada | Örnek ana cihaz haline gelmez; ihmal tek başına yeniden yazmaya olanak sağlamaz | `SERVICE` |

Alt cihazlara yönelik destek artık geçerliliğini yitirmiştir. Değer `main_device="false"` yükleme sırasında kabul edilir, ancak kaydedildikten sonra nitelik şöyle olur: `main_device="true"`. Kullanma `false` Kararlı bir konfigürasyon olarak.

## `scales`

Bölüm tamamen yoksa tartı nesnesi oluşturulmaz ve ağırlık ölçümü devre dışı kalır. Bölüm mevcutsa eksik veya geçersiz her alan yedek bir değerle değiştirilir; ardından dosyanın tamamı yeniden yazılabilir.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `pin_hc711_data` | HX711 veri GPIO’su | Bölüm mevcutsa zorunlu | Belirli bir kart için GPIO | Bölüm otomatik olarak oluşturulmaz; donanıma bağlı | Belirli bir pano için pin; dosya yeniden yazıldı | `SERVICE` |
| `pin_hc711_clk` | HX711 saat GPIO’su | Bölüm mevcutsa zorunlu | Belirli bir kart için GPIO | Bölüm otomatik olarak oluşturulmaz; donanıma bağlı | Belirli bir pano için pin; dosya yeniden yazıldı | `SERVICE` |
| `gain` | HX711 kazanç modu | Bölüm mevcutsa zorunlu | HX711 kazanç modu değeri | Kanal A, kazanç 128 | Kanal A, kazanç 128; dosya yeniden yazıldı | `SERVICE` |
| `zero_calibrate_measurement` | Sıfır yük için ham ADC değeri | Bölüm mevcutsa zorunlu | İşaretli 32 bit tam sayı | Donanıma bağlı | Geri dönüş değeri `-486050`; dosya yeniden yazıldı | `SERVICE` |
| `weight_calibrate_measurement` | Referans ağırlığıyla ham ADC değeri | Bölüm mevcutsa zorunlu | İşaretli 32 bit tam sayı | Donanıma bağlı | Geri dönüş değeri `-498030`; dosya yeniden yazıldı | `SERVICE` |
| `calibrate_weight` | Kalibrasyon referans kütlesi | Bölüm mevcutsa zorunlu | Gram; pozitif tamsayı; limitler otomatik olarak kontrol edilmez | Donanıma bağlı | `500` G; dosya yeniden yazıldı | `USER` |
| `start_weight` | Daranın sonuçtan çıkarılması | Bölüm mevcutsa zorunlu | Gram; `-100000` için `100000` tavsiye edilir; limitler otomatik olarak kontrol edilmez | Donanıma bağlı | `0` G; dosya yeniden yazıldı | `USER` |
| `source_weight` | Sonucu birincil ağırlık olarak kullanılan filtre | Bölüm mevcutsa zorunlu | `1` — `immediate`; `2` — `stable`; `3` — `calibration` | Bölüm otomatik olarak oluşturulmaz | `1`; dosya yeniden yazılır. Diğer değerler şu şekilde ele alınır: `1` operasyon sırasında | `SERVICE` |
| `normal_pecision` | Hızlı filtrenin hassasiyet parametresi | Bölüm mevcutsa zorunlu | Kayan nokta sayısı; limitler kontrol edilmiyor | Bölüm otomatik olarak oluşturulmaz | `0.5`; dosya yeniden yazıldı | `SERVICE` |
| `normal_desired_deviation` | Hızlı filtrenin istenen sapması | Bölüm mevcutsa zorunlu | Kayan nokta sayısı; limitler kontrol edilmiyor | Bölüm otomatik olarak oluşturulmaz | `10`; dosya yeniden yazıldı | `SERVICE` |
| `stable_pecision` | Kararlı filtrenin hassasiyet parametresi | Bölüm mevcutsa zorunlu | Kayan nokta sayısı; limitler kontrol edilmiyor | Bölüm otomatik olarak oluşturulmaz | `0.35`; dosya yeniden yazıldı | `SERVICE` |
| `stable_desired_deviation` | Kararlı filtrenin istenen sapması | Bölüm mevcutsa zorunlu | Kayan nokta sayısı; limitler kontrol edilmiyor | Bölüm otomatik olarak oluşturulmaz | `5`; dosya yeniden yazıldı | `SERVICE` |
| `calibrate_pecision` | Kalibrasyon filtresinin hassasiyet parametresi | Bölüm mevcutsa zorunlu | Kayan nokta sayısı; limitler kontrol edilmiyor | Bölüm otomatik olarak oluşturulmaz | `0.25`; dosya yeniden yazıldı | `SERVICE` |
| `calibrate_desired_deviation` | Kalibrasyon filtresinin istenen sapması | Bölüm mevcutsa zorunlu | Kayan nokta sayısı; limitler kontrol edilmiyor | Bölüm otomatik olarak oluşturulmaz | `3`; dosya yeniden yazıldı | `SERVICE` |
| `median_window` | Medyan filtre penceresi boyutu | Bölüm mevcutsa zorunlu | `3`–`100`; aralık dışı değerler değiştirilir | Bölüm otomatik olarak oluşturulmaz | `100`; dosya yeniden yazıldı | `SERVICE` |

tanımlayıcılar `normal_pecision`, `stable_pecision`ve `calibrate_pecision` tarihsel hatayı içeriyor `pecision`XML'de düzeltilmemesi gereken bir hatadır.

`gain` dosyadan yüklenir, ancak kaydetme her zaman A kanalını kazanç 128 ile ayarlar. Cihazınıza ait veriler olmadan bunu manuel olarak değiştirmeyin.

## `thermometer`

Eksik bir bölüm dosyanın normalleştirilmesine olanak tanır. Değer `sensors_count="0"` DS18B20 sensörlerinin yoklanmasını devre dışı bırakır.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `pin_onewire` | 1-Kablolu veri yolu GPIO | İsteğe bağlı | Belirli bir kart için GPIO | `4` | `4`; dosya yeniden yazıldı | `SERVICE` |
| `sensors_count` | DS18B20 sensör sayısı | İsteğe bağlı | `0` sensörleri devre dışı bırakır; pozitif tamsayı; üst limit kontrol edilmiyor | `2` | `2`; dosya yeniden yazıldı | `ADVANCED` |

## `schedule`

 `TimeSlot0`–`TimeSlot23` nitelikler karşılık gelen saate ilişkin eylemi tanımlar. 30. dakikadan sonra bir sonraki saatin eylemi seçilir; saat 23'ten sonra, `TimeSlot0` seçilir.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `TimeSlot0`…`TimeSlot23` | Saatlik planlanmış eylem türü `0`–`23` | Tüm özellikler isteğe bağlıdır, ancak en az bir yuva `2` gerekli | Tam sayı `0` için `5`; aşağıya bakın | `5` saatlerce `0`–`20`; `1` için `21` ve `22`; `2` için `23` | Eksik bir yuva olur `0`. Hayır ise `2` okumadan sonra kalırsa tüm program ilk programa sıfırlanır | `ADVANCED` |

| Değer | Eylem | Tavsiye |
|---:|---|---|
| `0` | Planlanmış eylem yok | Boş bir slot için kullanılabilir |
| `1` | Ölçüm | Destekleniyor |
| `2` | Birincil kanal üzerinden iletim | En az bir yuvada gerekli |
| `3` | Wi-Fi aracılığıyla iletim için ayrılmıştır | Kullanma |
| `4` | BLE aracılığıyla iletim için ayrılmıştır | Kullanma |
| `5` | Senkronizasyon için saatlik uyandırma | İlk program tarafından kullanılır |

Diğer tamsayılar reddedilmez ancak tanımlanmış davranışları yoktur. Yalnızca tablodaki değerleri kullanın.

### İlk Program

```xml
<schedule
  TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
  TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
  TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
  TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
  TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
  TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
```

## `booster`

Bu bölüm, kritik parametreleri kontrol etmek için ek uyandırmaların aralığını ayarlar. Bölüm yoksa çalışma sırasında saatlik aralık kullanılır; yokluğun kendisi yeniden yazmayı tetiklemez.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `booster_time_sec` | Ek kontrol aralığı | İsteğe bağlı | `180`, `240`, `300`, `360`, `600`, `720`, `900`, `1200`, `1800`veya `3600` s | `3600` s | `3600` s | `ADVANCED` |

Aşağıdaki bir değer `180` olur `180`; üstünde bir değer `3600` olur `3600`. Aralık içindeki diğer değerler tabloda desteklenen en yakın aralığa yuvarlanır.

## `range_alarmer`

Bu bölüm isteğe bağlıdır. Eğer yoksa eşik alarmı başlatılmaz. Eğer `alarm="false"` veya `alarm` öznitelik yok, limitler okunmuyor ve arka plan alarm görevi başlatılmıyor.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `alarm` | Eşik alarmlarını etkinleştirir | İsteğe bağlı | `true`, `false` | `false` | `false` | `USER` |
| `T1_min` | T1 alt sınırı | İsteğe bağlı | Kayan nokta sayısı, °C; fiziksel limitler ve minimum/maksimum sıra otomatik olarak kontrol edilmez | `-500` Yeni oluşturulan bir dosyada °C | ile `alarm="true"`, alt sınır yoktur | `ADVANCED` |
| `T1_max` | T1 üst sınırı | İsteğe bağlı | Kayan nokta sayısı, °C; fiziksel limitler ve minimum/maksimum sıra otomatik olarak kontrol edilmez | `500` Yeni oluşturulan bir dosyada °C | ile `alarm="true"`, üst sınır yoktur | `ADVANCED` |
| `T2_min` | T2 alt sınırı | İsteğe bağlı | Kayan nokta sayısı, °C; fiziksel limitler ve minimum/maksimum sıra otomatik olarak kontrol edilmez | `-500` Yeni oluşturulan bir dosyada °C | ile `alarm="true"`, alt sınır yoktur | `ADVANCED` |
| `T2_max` | T2 üst sınırı | İsteğe bağlı | Kayan nokta sayısı, °C; fiziksel limitler ve minimum/maksimum sıra otomatik olarak kontrol edilmez | `500` Yeni oluşturulan bir dosyada °C | ile `alarm="true"`, üst sınır yoktur | `ADVANCED` |
| `Humidity_min` | Nem alt sınırı | İsteğe bağlı | Kayan nokta sayısı, %; fiziksel limitler ve minimum/maksimum sıra otomatik olarak kontrol edilmez | `-20` Yeni oluşturulan bir dosyada % | ile `alarm="true"`, alt sınır yoktur | `ADVANCED` |
| `Humidity_max` | Nem üst sınırı | İsteğe bağlı | Kayan nokta sayısı, %; fiziksel limitler ve minimum/maksimum sıra otomatik olarak kontrol edilmez | `200` Yeni oluşturulan bir dosyada % | ile `alarm="true"`, üst sınır yoktur | `ADVANCED` |

Her kaynak (T1, T2 veya nem) için bir limit yeterlidir. Belirli bir kaynak için limit belirtilmemişse çeke eklenmez. sırası `_min` ve `_max` otomatik olarak kontrol edilmez.

### Tek Taraflı Alarm Örneği

Bu örnekte T1 yalnızca yukarıdan, T2 yalnızca aşağıdan izlenir ve nem izlenmez:

```xml
<range_alarmer alarm="true" T1_max="45.0" T2_min="-10.0" />
```

Genel SMS frekansı ve PIR alarm onayı şu şekilde yapılandırılır: `alarm_sms_sec_interval`, `alarm_by_changes_count`ve `alarm_by_long_state` içinde [`mset.xml`](settings-reference.md#options).

## Tartı Terazisi Olmadan Yapısal Örnek

Bu dosya başlangıç ​​programını, iki sıcaklık sensörünü ve devre dışı bırakılan eşik alarmlarını kullanır. `scales` bölümü bulunmadığından tartım terazisi nesnesi oluşturulmaz.

```xml
<settings>
  <hive hive_name="hive1" bus_number="0" main_device="true" />
  <booster booster_time_sec="3600" />
  <range_alarmer alarm="false"
                 T1_max="500" T1_min="-500"
                 T2_max="500" T2_min="-500"
                 Humidity_max="200" Humidity_min="-20" />
  <thermometer pin_onewire="4" sensors_count="2" />
  <schedule
    TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
    TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
    TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
    TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
    TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
    TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
</settings>
```

## Komple tartım terazileri Bölümü

Aşağıdaki yapısal örnek, geri dönüş değerlerini kullanır ve yalnızca arşiv referansı amacıyla sağlanmıştır. **Bir cihaza kurmayın:** kalibrasyon değerleri ve pinler söz konusu cihazın yedeğinden gelmeli veya standart kalibrasyon prosedürüyle oluşturulmalıdır.

```xml
<scales pin_hc711_data="27" pin_hc711_clk="26" gain="0"
        zero_calibrate_measurement="-486050"
        weight_calibrate_measurement="-498030"
        calibrate_weight="500" start_weight="0" source_weight="1"
        normal_pecision="0.5" normal_desired_deviation="10"
        stable_pecision="0.35" stable_desired_deviation="5"
        calibrate_pecision="0.25" calibrate_desired_deviation="3"
        median_window="100" />
```

GPIO `27` ve `26` yalnızca bir cihaza örnektir ve evrensel değildir. Belirli cihazınızın yedeklemesindeki değerleri kullanın.
