# Yapılandırmayı Geri Yükleme

Bu sayfada microSD kartın güvenli bir şekilde nasıl değiştirileceği, yapılandırmanın bir yedekten nasıl geri yükleneceği ve cihaz başlatıldıktan sonra XML dosyalarının nasıl kontrol edileceği açıklanmaktadır.

!!! danger "Cihaz aktifken microSD kartı çıkarmayın"
    Cihazın standart bir güç düğmesi yoktur. MicroSD kartı çıkarmadan veya takmadan önce cihazın uyku moduna girmesini bekleyin. Öncelikle tam bir kopyasını kaydedin. `/setting` dizin.

## Otomatik Normalleştirme

- ana dosya şu konumdadır: `/setting/mset.xml`;
- ana dosya eksikse cihaz bir başlangıç ​​konfigürasyonu oluşturabilir;
- eksik veya tamamlanmamış bir arı kovanı dosyası, mevcut durumdan geri dönüş değerleri kullanılarak yeniden kaydedilebilir;
- bir kayıp `hive`, `thermometer`veya `schedule` bölümün yanı sıra tamamlanmamış bir mevcut `scales` bölümü, arı kovanı dosyasının normalizasyonunu tetikler;
- tamamen eksik `scales` bölüm bir hata değildir: tartı terazileri basitçe oluşturulmamıştır;
- kök XML öğesindeki yapısal hatalar, `apairy_set` bölüm veya `hiveN` öznitelik yapılandırmanın okunmasını engelleyebilir.

Bir başlangıç oluşturma `mset.xml` her parametrenin evrensel bir değere sahip olacağı anlamına gelmez. `UPLOAD_URL`, FTP kimlik bilgileri, HX711 pinleri ve diğer bazı alanlar aygıt yapılandırmasına veya bireysel kuruluma bağlıdır.

!!! warning "Yedekleme gerekli"
    Tek yedeklemeniz olarak otomatik kurtarmaya güvenmeyin. microSD kartı değiştirmeden önce tüm bilgileri kaydedin. `/setting` kart hala okunabiliyorsa dizin.

## microSD Kartı Güvenli Bir Şekilde Değiştirme

1. Cihazın uyku moduna girmesini bekleyin.
2. MicroSD kartı çıkarın ve okunabiliyorsa tüm içeriğini kopyalayın.
3. MicroSD kartı, cihazın donanım sürümünün gereksinimlerine göre hazırlayın.
4. Geri yükle `/setting` doğrulanmış bir yedekten dizin.
5. Yedekleme yoksa başka bir cihazdaki tartı kalibrasyon değerlerini kullanmayın. İlk önce minimumu geri yükleyin [`mset.xml`](settings-reference.md#minimal-example), ardından arı kovanı dosyasını `scales` bölümüne bakın veya standart kalibrasyon prosedürünü gerçekleştirin.
6. Cihaz uykudayken microSD kartı takın ve bir sonraki çalışma döngüsünü bekleyin.
7. Saati, ağı, GSM numaralarını, mevcut sensörleri, programı ve ağırlığı kontrol edin.
8. Normalleştirilmiş XML dosyalarını yedeklemeyle karşılaştırın: cihazda yedek değerlere sahip alanlar veya yeniden yazılmış bölümler bulunabilir.

## Yapılandırma Okunamıyorsa

1. Dosyada bir tane olup olmadığını kontrol edin `<settings>` kök elemanı.
2. Tam adları kontrol edin `apairy_set`, `synchronize`, `sefe_start_interval`ve `pecision` üç filtre alanında.
3. Emin olun `hive_count` eşleşen var `hive1`…`hiveN` nitelikler.
4. Referans verilen her şeyin olduğundan emin olun `/setting/<hive>.xml` dosya mevcut.
5. Kopyalayarak sorunu çözmeye çalışmayın `scales` başka bir cihazdan. Tartım terazisi bölümünü geçici olarak çıkarın ve yapılandırmanın geri kalanını kontrol edin.
6. Tanılama için sorunlu XML dosyalarını ve hizmet günlüklerini kaydedin.

Alanların tam açıklaması için bkz. [`mset.xml`](settings-reference.md) ve [`HIVE*.XML`](hive-settings-reference.md) referanslar.
