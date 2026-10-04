# Kış Kullanımı ve Depolama

BeeApiary Arı kovanı tartı terazileri kışın açık havada kalıp ölçüm almaya devam edebildiği gibi veri aktarmadan da saklanabilir. Bu dönemde kovanları izlemeniz gerekip gerekmediğine göre senaryoyu seçin.

## Kışın Operasyon

Ne zaman [yüklü](installation.md) doğru şekilde ayarlanmışsa, tartım terazileri açık havada, kılavuzda listelenen sıcaklık aralığı dahilinde normal şekilde çalışır. [özellikler](specifications.md). Kış ölçümleri aşağıdakileri izlemenize yardımcı olur:

- ağırlık değişiklikleri ve kalan yiyecek rezervleri;
- izlenen arı kovanının içindeki ve dışındaki sıcaklık;
- İlgili sensör takılıysa nem.

Kıştan önce muhafazayı ve koruyucu kapakları inceleyin, akü şarjını kontrol edin ve platformun sağlam olduğundan emin olun. Suyun mahfazaya girmesine izin vermeyin.

## Veri İletimi Olmadan Depolama

Kış ölçümlerine gerek yoksa cihazı kapatmanıza veya sökmenize gerek yoktur. Başarısız SMS mesajı gönderme girişimleri nedeniyle pil gücü ve iletişim kredisi tüketmesini önlemek için aşağıdaki yöntemlerden birini kullanın:

- SIM kartı çıkarın veya devreden çıkıp çalışma konumundan çıkana kadar karta bastırın;
- devre dışı bırak **GSM** geçiş yap [ek cihaz ayarları](additional-settings.md).

Aktif bir SIM kartı, kredisiz veya ücretli bir plan olmadan cihazda bırakmayın. Cihaz, kartı algılayabilir ancak hesap veya plan durumunu belirleyemediğinden SMS mesajları göndermeye ve pil gücünü tüketmeye devam edecektir.

Depolamadan önce pili tamamen şarj edin. Normal veri aktarımında bir şarj 2-3 ay sürebilir. Ayarlarda GSM devre dışı bırakılırsa veya SIM kart çalışma konumundan çıkarılırsa pil ömrü düşük sıcaklıklarda bile altı ayı aşabilir. Gerçek süre pilin durumuna ve türüne, sıcaklığa ve cihaz konfigürasyonuna bağlıdır; şarjı periyodik olarak kontrol edin ve [cihazı şarj edin](power.md) gerektiğinde.

## Depolama için Pili Çıkarmayın

Cihaz iki akıllı ve bir elektronik seviye pil korumasına sahiptir. Şarj %20'nin altına düştüğünde otomatik olarak derin güç tasarrufu moduna geçer ve şarj edilmeyi bekler. Bu modda güç tüketimi, pilin kendi kendine boşalmasıyla karşılaştırılabilir düzeydedir.

Tahmin olarak, %20'lik bir şarj bile derin uykuda neredeyse iki yıllık bekleme süresi sağlayabilir. Bu, düzenli ölçümler veya veri aktarımı sırasında pil ömrünün garantisi değildir: pilin durumu ve türü, sıcaklığı ve cihaz konfigürasyonunun tümü sonucu etkiler.

!!! danger "Polariteyi Ters Çevirmeyin"
    Normal saklama veya şarj için pili çıkarmayın. Her yeniden kurulum, kutupların tersine çevrilmesi ve cihazın kalıcı olarak hasar görmesi riskini doğurur. İstisnalar: [acil kurtarma](../troubleshooting/recovery-after-storage.md) voltaj düşük olduğunda `3,5 В`veya doğrulanmış bir prosedüre göre gerçekleştirilen servis işi.

Depolamadan sonra cihazın pil şarjını ve süresini kontrol edin. Ek öneriler şu adreste mevcuttur: [Bakım](maintenance.md) sayfa.
