# BeeApiary kovan tartısı nasıl kurulur

1. Cihazı USB Type-C ile şarj edin.

    !!! note "Şarj cihazı ve kablo seçimi"
        Cihaz, USB Güç Dağıtımı (PD) dahil olmak üzere hızlı şarjı desteklemez. USB Type-A bağlantı noktası ve USB Type-A–USB Type-C kablosuyla standart bir güç kaynağı kullanın. Şarj için USB Type-C–USB Type-C kablosunun kullanılması önerilmez.

2. Cihazı ve sensörleri aşağıdaki talimatlara göre kurun. [yerleştirme yönergeleri](../device/placement.md).
3. PIN koruması devre dışı bırakılmış bir mikro SIM takın.

    Mikro SIM biçimini kullanın:

    ![SIM kart formatlarının karşılaştırılması](../../assets/tr/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Doğru takılmış kart:

    ![Doğru takılmış mikro SIM](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    SIM kartı takın ve yerine kilitlendiğini onaylayan yumuşak bir tıklama duyuncaya kadar neredeyse tamamen yuvaya doğru yavaşça bastırın:

    ![mikro SIM yuvaya kilitlendi](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

4. <span id="activation-reset"></span>Cihazı etkinleştirin veya yeniden başlatın: manyetik anahtarı ana ünitenin arkasındaki marka işaretine kısa süreliğine tutun.

    ![BeeApiary manyetik anahtar](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Markalı manyetik anahtarlı hedef](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

5. Ayarları kontrol etmeniz veya değiştirmeniz gerekiyorsa [`apiary_net` ağına bağlanın](configure-local-wifi.md) ve `http://192.168.4.1` adresini açın. Aksi halde bu adımı atlayın.
6. Kullanıcının numarası genellikle üretici tarafından ayarlanmıştır. Yalnızca gerektiğinde [GSM ayarlarında numarayı kontrol edin, değiştirin veya kaldırın](configure-gsm.md).
7. `apiary_net` ağına bağlandıysanız bağlantıyı kesin. İlk SMS'i bekleyin: mesaj genellikle cihaz uykuya geçmeden önce, bağlantı kesildikten veya cihaz etkinleştirildikten yaklaşık bir dakika sonra gelir.

    İletim ayarlarını, kalibrasyonu veya diğer ayarları değiştirdikten sonra cihazın uyumasını bekleyip `apiary_net` ağına yeniden bağlanmadan manyetik anahtarla tekrar etkinleştirmeniz gerekebilir.

Sonuç: Cihaz ölçümleri toplar, sahibine gönderir ve bir arşiv olarak saklar.
