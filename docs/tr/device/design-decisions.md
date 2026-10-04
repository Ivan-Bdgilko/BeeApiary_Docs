# BeeApiary neden böyle çalışır

## itibaren BeeApiary Yaratıcılar

BeeApiary verileri ve önemli kararları arıcının kontrolü altında tutan bağımsız bir araç olarak tasarlanmıştır. Bu sayfada hemen belli olmayabilecek çeşitli tasarım ve yazılım seçenekleri açıklanmaktadır.

## Kapaklar Neden Şeffaftır?

Şeffaf kapak, cihazın ne zaman çalıştığını ve muhafazaya yoğuşma, böcek veya kir girip girmediğini görmenizi sağlar. Bu, muhafazayı gereksiz yere açmadan incelemeyi kolaylaştırır.

Proje geri bildirime ve önerilere açıktır: inşaatı ana bileşenlerin durumunu sahibinden gizlemez.

## Neden Zorunlu Sunucu Depolama Alanı Yok?

Arı kovanı tartım terazilerinin ve uygulamanın temel çalışması kalıcı ölçümlere bağlı değildir. BeeApiary harici bir sunucuda depolama. Ölçümler hafızada saklanır [cihazın microSD kartı](../system/data-storage.md) ve yerel olarak kullanıcının telefonunda. Sistem, sahibinin konumunun veya etkinlik geçmişinin merkezi olarak saklanmasını gerektirmez.

İsteğe bağlı bir aktarma hizmeti aşağıdakiler için kullanılabilir: [arı kovanı Wi-Fi ağı üzerinden senkronizasyon](../system/local-wifi.md#apiary-wifi-routing). Verileri uygulamaya aktarır ancak kalıcı depolama değildir ve diğer iletişim kanalları için gerekli değildir.

## GSM Neden SMS Kullanıyor?

Tarlada veya bir arı kovanını taşırken, mobil İnternet erişiminin güvenilir olmadığı durumlarda SMS sıklıkla kullanılabilir. Minimum SMS planı yeterlidir ve uygulama, verileri ayrı bir sunucu aboneliği olmadan alır.

Uygun mesaj formatı ile günde iki SMS mesajı, o gün içinde toplanan tüm saatlik ölçümlerin sonuçlarını iletebilir. Uygulama doğrudan sahibinin telefonunda çalışır ve tipik bir yapılandırmada en fazla beş cihazı işleyebilir; Gerektiğinde bu sayı artırılabilir.

Ayrıntılar için bkz. [GSM ve SMS](../system/gsm-and-sms.md).

## Neden Her Saatte Ölçüm Alınıyor?

Saatlik geçmiş, arıların sabah kalkışlarını ve akşam dönüşlerini, nektar kururken ağırlık değişimlerini ve günlük sıcaklık değişimlerini ortaya çıkarmaya yardımcı olur. Bu veriler koloni gücü, yiyecek rezervleri ve arı kovanı içindeki diğer süreçlerin daha ileri analizi için bir temel sağlar.

## SMS Mesajları Neden Her Saat Gönderilmiyor?

Sık iletim, ölçümleri iyileştirmez ancak pil gücünü ve iletişim kredisini tüketir. Günde birkaç mesaj göndermek, biriken saatlik verileri çok daha verimli bir şekilde aktarır.

Günde iki SMS mesajı için pratik bir tahmin, tek şarjla en az 160 günlük çalışmadır. Bu bir garanti değil, bir kılavuzdur: pil ömrü pile, cihaz yapılandırmasına, sıcaklığa, GSM kapsama alanına ve etkin iletim kanallarına bağlıdır.

Bir alarm sensörü takılıysa, bir acil durum olayı veya arı kovanını hareket ettirme girişimi, normal programı beklemeden ayrı ayrı bir çağrıyı ve bir SMS'i tetikleyebilir.

## Pil Neden Çıkarılmamalıdır?

Cihaz üç seviyeli pil korumasına sahiptir ve şarj azaldığında otomatik olarak derin güç tasarrufu moduna girer. Pilin saklanması için çıkarılmasına gerek yoktur; yeniden kurulum sırasında yanlış kutuplama, elektronik aksama kalıcı olarak zarar verebilir.

İstisnalar ve kış mevsiminde saklama kuralları şurada açıklanmıştır: [Güç ve Şarj](power.md) ve [Kış Kullanımı ve Depolama](winter-use-and-storage.md).

## Firmware Güncellemeleri Neden Otomatik Değil?

Cihazın ne zaman güncelleneceğine ve yeni bir sürümün özelliklerinin gerekli olup olmadığına cihaz sahibi karar verir. Kontrollü bir güncelleme, otonom bir sistemin davranışında beklenmeyen değişiklik riskini azaltır.

Arı kovanı tartım terazileri, bağımsız tartım terazileri ve hava durumu veri kaydedicisi olarak telefon olmadan çalışabilir. Android uygulaması görüntüleme, arı kovanı günlüğü ve senkronizasyon özelliklerini genişletir ancak ölçümler için gerekli değildir. Prosedür: [Cihazı Güncelle](../guides/update-device.md).

## Ölçümler Ne Kadar Süre Saklanıyor?

MicroSD karttaki arşiv bir yılla sınırlı değildir. Saklama süresi kartın kapasitesine ve durumuna bağlıdır; normal ölçüm hacmiyle cihazın beklenen hizmet ömrü için yeterlidir.

## İki Tür SMS ve Esnek Program. Neden?

Ölçüm almaya ne zaman, nasıl ve nerede başlanacağı konusunda pek çok görüş vardır; Bu sorunu çözmek için kullanıcılar SMS formatını ve gönderim süresini tercihlerine göre serbestçe yapılandırabilirler. Ancak güç tasarrufu sağlamak amacıyla günlük mesaj sayısına ilişkin bazı öneriler bulunmaktadır.
