# Arşiv Nasıl İndirilir

Başlamadan önce, emin olun BeeApiary uygulama Google Play aracılığıyla günceldir ve arı kovanı tartım terazileri, Ağustos 2024 veya sonrasında piyasaya sürülen donanım yazılımını çalıştırmaktadır. Yüklü sürüm daha eskiyse veya tarihinden emin değilseniz aşağıdaki adımları izleyin: [Güncelleme BeeApiary Arı kovanı tartı terazileri Firmware](update-device.md).

Tartım terazisinde SIM kart bulunmadığında, diğer senkronizasyon yöntemleri geçici olarak kullanılamadığında veya ölçümlerde boşluklar oluştuğunda manuel arşiv indirme işlemi faydalıdır. Uygulama, depolanan verileri içe aktarır ve yerel geçmişe ekler.

!!! warning "microSD ve pil şarjı"
    Tartım terazilerine mevcut verileri içeren çalışan bir microSD kart takılmalıdır. Doğrudan Wi-Fi bağlantısı tartıyı aktif tutar ve güç tüketimini artırır, bu nedenle bu işlemi gerekmedikçe günde bir kereden fazla yapmayın.

1. [Etkinleştirin veya yeniden başlatın BeeApiary arı kovanı tartı terazileri](../device/installation.md#activation-reset) manyetik anahtarla.
2. Kullanılabilir aralık dahilinde (genellikle yaklaşık bir dakika), telefonu `apiary_net` ve tartı terazisinin yakınında durun.
3. Aç BeeApiary uygulama.
4. Uygulamanın yakındaki tartı terazilerini otomatik olarak algılamasını bekleyin.
5. içinde **"Cihaz yakında. Arşiv indirilsin mi?"** istemi, dokunun **Evet**.

    ![BeeApiary arşivi yakındaki bir cihazdan indirmeye yönelik uygulama istemi](../../assets/en/guides/download-archive/nearby-device-archive-prompt.jpg){ .doc-screenshot }

6. İçe aktarmanın bitmesini bekleyin ve ardından hemen telefonun bağlantısını kesin. `apiary_net`. Bağlantı kesildiğinde tartım terazileri uyku moduna girebilir ve pilin gereksiz yere tükenmesini önleyebilir.
7. İndirilen verileri uygulamanın standart ekranlarını kullanarak görüntüleyin.

    ![BeeApiary içe aktarılan ölçümleri içeren uygulama ana ekranı](../../assets/en/app/main-screen/app-home-screen.png){ .doc-screenshot }

Onaylandıktan sonra uygulama arşivi otomatik olarak indirir ve ölçümlerin yerel bir kopyasını saklar. Diğer kanalların bazı verileri kaçırması durumunda arşiv, geçmişteki ilgili boşlukları doldurabilir. Arşiv formatı ve saklama süresi aşağıda açıklanmıştır. [Veri Depolama](../system/data-storage.md).
