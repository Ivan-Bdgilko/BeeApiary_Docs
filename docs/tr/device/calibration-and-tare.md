# Kalibrasyon ve Dara

!!! danger "Yeni bir cihazın kalibrasyona ihtiyacı yoktur"
    Kalibrasyon öncelikle bir onarımdan veya fabrika kalibrasyon verilerinin kaybolmasından sonra gereklidir. Yanlış ağırlık okumasında sorun gidermenin genel bir yolu olarak kullanmayın.

<span id="calibration"></span>
## Kalibrasyon

1. Harici güç kaynağının bağlantısını kesin.
2. Tüm ağırlık sensörlerini sağlam, düz bir yüzeye yerleştirin ve platformu boş bırakın.
3. Cihazın erişim noktasına bağlanın ve açın **Genel Ayarlar → Tartı Ayarları** web arayüzünde.

    ![Tartım terazisi ayarlarını açma düğmesi](../../assets/en/device/calibration-and-tare/open-scale-settings.png){ .doc-screenshot }

4. Başlat **Sıfır Kalibrasyon** ve platforma dokunmadan bitmesini bekleyin.

    Ekranda iki kalibrasyon aşaması gösterilir:

    ![tartım terazisi kalibrasyon aşamaları](../../assets/en/device/calibration-and-tare/calibration-steps.png){ .doc-screenshot }

    ![Sıfır kalibrasyon devam ediyor](../../assets/en/device/calibration-and-tare/zero-calibration-progress.png){ .doc-screenshot }

5. 500, 1000 veya 5000 g'lık mevcut bir referans ağırlığı seçin ve bunu platforma yerleştirin.

    ![Referans ağırlığının seçilmesi](../../assets/en/device/calibration-and-tare/reference-weight-selection.png){ .doc-screenshot }

6. Başlat **Referans Kalibrasyonu** ve sonucu bekleyin.

    ![Referans kalibrasyonu devam ediyor](../../assets/en/device/calibration-and-tare/reference-weight-calibration-progress.png){ .doc-screenshot }

    ![tartı kalibrasyon sonucu](../../assets/en/device/calibration-and-tare/calibration-result.png){ .doc-screenshot }

Sonuç: Cihaz yeni kalibrasyon değerlerini kaydetti. Referans ağırlığının görüntülendiğini kontrol edin.

<span id="tare"></span>
## Dara

Dara alma, platformun veya başka bir sabit yapının ağırlığını ölçüm dışında bırakır.

1. [Tartının web arayüzüne bağlanın](../guides/configure-local-wifi.md).
2. **Genel ayarlar → Tartı ayarları** bölümünü açın.
3. Bir yöntem seçin:

    - Dara ağırlığı biliniyorsa gram cinsinden girip **Dara ağırlığını ayarla** seçeneğini seçin.

        ![Bilinen bir dara ağırlığının girilmesi](../../assets/en/device/calibration-and-tare/known-tare-weight-form.png){ .doc-screenshot }

    - Veya yapıyı sensörlerin üzerinde bırakıp mevcut değeri sıfır olarak kabul edin.

        ![Mevcut ağırlığı sıfır olarak kabul etmek](../../assets/en/device/calibration-and-tare/use-current-weight-as-zero.png){ .doc-screenshot }

4. İşlem bitince göstergeyi kontrol edin.

Sonuç: Cihaz sonraki ölçümlerden darayı düşer. Dara alma fabrika kalibrasyon katsayısını değiştirmez.
