# `mset.xml`: Cihaz Ayarları

Ana konfigürasyon şurada saklanır: `/setting/mset.xml` microSD kartta bulunur ve bir `<settings>` kök elemanı.

!!! warning "Geçerli dosya fabrika değerlerinin bir listesi değil"
    Belirli bir cihazın XML'indeki değerler kullanıcı, web arayüzü tarafından veya otomatik olarak değiştirilmiş olabilir. Örneğin, `sefe_start_interval="60000"` ve `alarm_sms_sec_interval="10"` başlangıç değerleri değildir: yeni bir konfigürasyon şunu kullanır: `120000` milisaniye ve `180` sırasıyla.

Ayrıca bkz. [güvenli düzenleme kuralları](service-reference.md). Değiştirme `SERVICE` Yedekleme olmadan parametreler ve bunların cihaz üzerindeki etkilerinin anlaşılması.

## `net_settings`

Bu bölümde cihazın erişim noktası, harici Wi-Fi ağına bağlantı, veri iletimi ve FTP ile ilgili parametreler saklanır. bir `SSID`/`PASSWORD` veya `SSID_STA`/`PASSWORD_STA` çifti yalnızca her iki değer de mevcut olduğunda ve boş olmadığında uygulanır.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `SSID` | Cihazın yerel erişim noktasının adı | Şartlı olarak gerekli `PASSWORD` | Dize; en fazla 32 karakter | `apiary_net` | Yeni erişim noktası çifti uygulanmadı | `USER` |
| `PASSWORD` | Yerel erişim noktasının şifresi | Şartlı olarak gerekli `SSID` | Dize; en fazla 32 karakter | `apiary_wifi` | Yeni erişim noktası çifti uygulanmadı | `USER` |
| `SSID_STA` | Harici Wi-Fi ağının SSID'si | İsteğe bağlı | Boş olmayan dize; azami uzunluk belirtilmemiş | `-` | Yeni STA parametreleri uygulanmaz | `ADVANCED` |
| `PASSWORD_STA` | Harici Wi-Fi ağının şifresi | Şartlı olarak gerekli `SSID_STA` | Dize; azami uzunluk belirtilmemiş | `-` | Yeni STA parametreleri uygulanmaz | `ADVANCED` |
| `STA_KEY` | İletim sırasında kullanılan kimlik doğrulama anahtarı | İsteğe bağlı | Dize; biçim kimlik doğrulama yöntemine bağlıdır | `-` | Wi-Fi parametresi değişmedi | `SERVICE` |
| `UPLOAD_URL` | Wi-Fi veri alıcısının adresi | İsteğe bağlı | URL'si; maksimum uzunluk belirtilmedi | Cihaz konfigürasyonuna bağlıdır | Tek bir alana ayarlayın; iletim etkili bir şekilde yapılandırılmamış | `SERVICE` |
| `wifi_sync` | Harici bir Wi-Fi ağı üzerinden senkronizasyonu etkinleştirir | İsteğe bağlı | `true`, `false` | `false` | `false` | `ADVANCED` |
| `FTP_USER` | Yerel FTP için kullanıcı adı | Bir çiftin parçası olarak isteğe bağlı | Dize; en fazla 32 karakter | Cihaz konfigürasyonuna bağlıdır | FTP alanlarından herhangi biri eksikse başlangıç FTP ayarları kullanılır | `ADVANCED` |
| `FTP_PASSWORD` | Yerel FTP şifresi | Bir çiftin parçası olarak isteğe bağlı | Dize; en fazla 32 karakter | Cihaz konfigürasyonuna bağlıdır | FTP alanlarından herhangi biri eksikse başlangıç FTP ayarları kullanılır | `ADVANCED` |

!!! note " `-` değer"
    için `SSID_STA`, `PASSWORD_STA`ve `STA_KEY`kısa çizgi gerçek bir başlangıç değeridir. Boş olmayan bir dize olarak işlenir, bu nedenle bunu bir ayarın "yapılandırılmadığını" gösteren güvenilir bir gösterge olarak kullanmayın.

Başlangıç şifresini değiştirin `apiary_wifi` İlk cihaz kontrolünden sonra.

## `apairy_set`

Bölüm adı geçmiş bir hata içeriyor ve bu şekilde kalması gerekiyor `apairy_set`. Bu bölüm arı kovanlarının listesini oluşturmak için gereklidir.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `hive_count` | Arı kovanı yapılandırma dosyalarının sayısı | Gerekli bölümdeki isteğe bağlı alan | Tamsayı; `1` veya daha fazlası tavsiye edilir; limitler otomatik olarak kontrol edilmez | `1` | `1` | `ADVANCED` |
| `hive1`…`hiveN` | Arı kovanı dosyalarının temel adları olmadan `.xml` | 'a kadar her sayı için gereklidir `hive_count` | Dize; uyumluluk için en fazla 8 ASCII karakteri önerilir | `hive1` | Öznitelik okuma hatası; karşılık gelen arı kovanı oluşturulmadı | `SERVICE` |

Yolun bir formu var `/setting/<значення>.xml`. Ad, 24 baytlık dahili bir arabellek kullanır, bu nedenle uzun adlar veya yol ayırıcılar kullanmayın.

## `GSM`

Bu bölümde iki alıcı açıklanmaktadır. Bölüm yoksa GSM yapısı temizlenir. Bu nedenle, SIM kart olmadan çalışırken bile bölümün kendisinin gerekli olduğu düşünülmelidir.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `sms_format1` | için SMS formatı `number1` | İsteğe bağlı | `1` - metin; `2` — kompakt uygulama formatı | `2` | `2` | `USER` |
| `sms_format2` | için SMS formatı `number2` | İsteğe bağlı | `1` - metin; `2` — kompakt uygulama formatı | `2` | `2` | `USER` |
| `number1` | Birincil alıcı numarası | İsteğe bağlı | Uluslararası format; dahili 15 bayt arabellek | Boş dize | İlk yüklemede hiçbir alıcı yapılandırılmadı | `USER` |
| `number2` | Ek alıcı numarası | İsteğe bağlı | Uluslararası format; dahili 15 bayt arabellek | Boş dize | İlk yüklemede hiçbir alıcı yapılandırılmadı | `USER` |
| `sms_wait_to_send_sec` | Zayıf bir ağda SMS göndermeden önce beklenecek süre | İsteğe bağlı | Tamsayı saniye sayısı; sabit limit yok | `50` s | `50` s | `ADVANCED` |
| `alarm_call_wait_sec` | Tekrarlanan alarm çağrısı girişimleri arasındaki aralık | İsteğe bağlı | Tamsayı saniye sayısı; sabit limit yok | `80` s | `80` s | `ADVANCED` |

Boş bir sayıyı şu şekilde belirtin: `number1=""` veya `number2=""`. Yayınlanan örneklere gerçek telefon numaralarını dahil etmeyin.

## `NTP`

Bu bölüm GSM ile aynı iç yapıya aittir. Eğer `NTP` tamamen yok ise, yeni okunan GSM parametreleri de sıfırlanır. Bu nedenle, senkronizasyon devre dışı bırakıldığında bile bölümün mevcut kalması gerekir.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `synchronize` | Mevcut bir ağ mekanizması aracılığıyla otomatik zaman senkronizasyonu | Gerekli bölümdeki isteğe bağlı alan | `true`, `false` | `false` | `false` | `USER` |
| `time_zone` | XML'de tam saat cinsinden belirtilen saat dilimi farkı | İsteğe bağlı | Tamsayı; `-11` için `12` tavsiye edilir; limitler otomatik olarak kontrol edilmez | `2` | `3` | `ADVANCED` |
| `ntp1` | Birincil zaman sunucusu | İsteğe bağlı | Ana bilgisayar adı; 30 bayta kadar dahili arabellek | `0.europe.pool.ntp.org` | İlk yüklemede boş | `ADVANCED` |
| `ntp2` | İkincil zaman sunucusu | İsteğe bağlı | Ana bilgisayar adı; 30 bayta kadar dahili arabellek | `1.europe.pool.ntp.org` | İlk yüklemede boş | `ADVANCED` |
| `ntp3` | Üçüncü kez sunucu | İsteğe bağlı | Ana bilgisayar adı; 30 bayta kadar dahili arabellek | `2.europe.pool.ntp.org` | İlk yüklemede boş | `ADVANCED` |

`time_zone` iki durumda farklı değerlere sahiptir: yeni bir dosya alınır `2`, eksik bir özellik ise `3`. İlk konfigürasyonu değiştirmeden önce bu farkı hesaba katın.

Yazım `synсhronize` Kiril harfini içerir `с` ve tanınmıyor. Yalnızca kullan `synchronize`.

## `options`

Bireysel özellikler isteğe bağlıdır ve geri dönüş değerlerine sahiptir. **Bölümün tamamını kaldırmayın:** eğer mevcut değilse, aşağıda gösterilen başlangıç ​​değerlerinin alınması yerine kesit parametreleri temizlenir.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `meteo` | Basınç ve nem sensörünün varlığını gösterir | İsteğe bağlı | `true`, `false` | `false` | `false` | `SERVICE` |
| `pir_sensor` | PIR hareket sensörünün varlığını gösterir | İsteğe bağlı | `true`, `false` | `false` | `false` | `SERVICE` |
| `temperature_twist` | Mantıksal T1 ve T2 değerlerini değiştirir | İsteğe bağlı | `true`, `false` | `false` | `false` | `ADVANCED` |
| `oled` | Bir OLED ekranın varlığını gösterir | İsteğe bağlı | `true`, `false` | `false` | `false` | `SERVICE` |
| `oled_invert` | OLED görüntüsünü tersine çevirir | İsteğe bağlı | `true`, `false` | `false` | `false` | `SERVICE` |
| `sefe_start_interval` | Başlatma sonrasında etkin pencerenin süresi | İsteğe bağlı | Milisaniye; limitler otomatik olarak kontrol edilmez | `120000` milisaniye | `120000` milisaniye | `SERVICE` |
| `alarm_sms_sec_interval` | Alarm SMS mesajları arasındaki minimum aralık | İsteğe bağlı | İşaretsiz tamsayı saniye sayısı | `180` s | `180` s | `ADVANCED` |
| `alarm_by_changes_count` | Bir alarmı onaylamak için gereken PIR durumu değişikliği sayısı | İsteğe bağlı | İşaretsiz tamsayı; pratik değer yerleşime bağlıdır | `3` | `3` | `ADVANCED` |
| `alarm_by_long_state` | Bir alarm için gerekli aktif PIR durumunun süresi | İsteğe bağlı | İşaretsiz tamsayı saniye sayısı | `10` s | `10` s | `ADVANCED` |
| `time_ms_compensate` | Günlük saat hızı telafisi | İsteğe bağlı | İmzalı 32 bitlik milisaniye sayısı | `0` milisaniye | `0` milisaniye | `SERVICE` |
| `sync_time_sec` | Manuel senkronizasyon için servis zaman damgası | İsteğe bağlı | İmzalı 64 bitlik saniye sayısı | `0` | `0` | `SERVICE` |

`sefe_start_interval` tam tarihsel alan adıdır. Başlangıç değeri `120000` milisaniye; aralık otomatik olarak kontrol edilmediğinden, keyfi olarak azaltılması tehlikelidir.

Web arayüzü aracılığıyla değiştirilen donanım bayrakları hemen kaydedilir, ancak işletim konfigürasyonu, ayarlar tekrar okunduktan sonra bunları uygular.

## `BLE`

Eski dosyalarla uyumluluk açısından bölümün tamamı isteğe bağlıdır. Eğer yoksa BLE devre dışı bırakılır ve mevcut değerler ile standart aralıklar kullanılır.

| Alan | İşlev | Zorunluluk | İzin verilen değerler / sınırlar | Başlangıç değeri | Belirtilmemişse | Düzey |
|---|---|---|---|---|---|---|
| `ble_enable` | BLE'yi etkinleştirir | İsteğe bağlı | `true`, `false` | `false` | `false`; geçersiz bir değer aynı zamanda BLE'yi de devre dışı bırakır | `USER` |
| `static_values` | Geçerli değerler yerine statik değerleri seçer | İsteğe bağlı | `true`, `false` | `false` | `false` | `SERVICE` |
| `update_time_sec` | BLE veri güncelleme aralığı | İsteğe bağlı | `3`–`60` S; daha düşük değerler normalize edilir `3`, daha yüksek değerler `60` | `30` s | `30` s | `ADVANCED` |
| `advertising_time_sec` | BLE reklam süresi | İsteğe bağlı | `0` veya `10`–`60` s; gelen değerler `1` için `9` normalize edilir `0`, yukarıdaki değerler `60` için `60` | `20` s | `20` s | `ADVANCED` |

için `static_values`, yalnızca geçerli değerlerin yerine statik değerlerin seçimi açıklanmaktadır; parametrenin başka bir etkisi tanımlanmamıştır.

## Asgari Örnek { #minimal-example }

Bu örnekte STA, FTP ve BLE başlangıç değerlerinde bırakılır. Boş ama mevcut `<options />` bölümü, tüm yapıyı temizlemek yerine her bir özelliğin geri dönüş değerini etkinleştirir.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options />
</settings>
```

## Tam Temizlenmiş Örnek { #full-example }

Değerler `SITE_WIFI`, `WIFI_PASSWORD`, `DEVICE_KEY`, `FTP_USER`, `FTP_PASSWORD`ve URL, bir işletim cihazından gelen veriler değil, yer tutuculardır.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi"
                SSID_STA="SITE_WIFI" PASSWORD_STA="WIFI_PASSWORD"
                STA_KEY="DEVICE_KEY"
                UPLOAD_URL="https://example.invalid/beeapiary"
                wifi_sync="false"
                FTP_USER="FTP_USER" FTP_PASSWORD="FTP_PASSWORD" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="+380XXXXXXXXX" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options meteo="false" pir_sensor="false"
           temperature_twist="false" oled="false" oled_invert="false"
           sefe_start_interval="120000"
           alarm_sms_sec_interval="180"
           alarm_by_changes_count="3" alarm_by_long_state="10"
           time_ms_compensate="0" sync_time_sec="0" />
  <BLE ble_enable="false" static_values="false"
       update_time_sec="30" advertising_time_sec="20" />
</settings>
```
