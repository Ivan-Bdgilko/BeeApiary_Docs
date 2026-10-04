# Yeni BeeApiary kovan tartısı nasıl kurulur

1. Cihazı USB Type-C ile şarj edin.

    !!! note "Şarj cihazı ve kablo seçimi"
        Cihaz, USB Güç Dağıtımı (PD) dahil olmak üzere hızlı şarjı desteklemez. USB Type-A bağlantı noktası ve USB Type-A–USB Type-C kablosuyla standart bir güç kaynağı kullanın. Şarj için USB Type-C–USB Type-C kablosunun kullanılması önerilmez.

2. Cihazı ve sensörleri aşağıdaki talimatlara göre kurun. [yerleştirme yönergeleri](../device/placement.md).
3. PIN koruması devre dışı bırakılmış bir mikro SIM takın.

    Mikro SIM biçimini kullanın:

    ![SIM kart formatlarının karşılaştırılması](../../assets/en/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Doğru takılmış kart:

    ![Doğru takılmış mikro SIM](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    SIM kartı takın ve yerine kilitlendiğini onaylayan yumuşak bir tıklama duyuncaya kadar neredeyse tamamen yuvaya doğru yavaşça bastırın:

    ![mikro SIM yuvaya kilitlendi](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

4. Cihazı etkinleştirin veya yeniden başlatın: manyetik anahtarı ana ünitenin arkasındaki marka işaretine kısa süreliğine tutun.

    ![BeeApiary manyetik anahtar](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Markalı manyetik anahtarlı hedef](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

    Daha fazla bilgi için bkz. [Etkinleştirme ve Yeniden Başlatma](../device/installation.md#activation-reset).

5. Bağlan `apiary_net` ve açık `http://192.168.4.1`.
6. Sahibinin telefon numarasını uluslararası formatta girin.
7. Bağlantıyı kes `apiary_net` ve ilk SMS mesajını kontrol edin.

Sonuç: Cihaz ölçümleri toplar, sahibine gönderir ve bir arşiv olarak saklar.
