# Kalibrasyon ve Dara

!!! danger "Yeni bir cihazın kalibrasyona ihtiyacı yoktur"
    Kalibrasyon öncelikle bir onarımdan veya fabrika kalibrasyon verilerinin kaybolmasından sonra gereklidir. Yanlış ağırlık okumasında sorun gidermenin genel bir yolu olarak kullanmayın.

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

## Dara

Bilinen bir dara ağırlığını gram cinsinden girebilirsiniz:

![Bilinen bir dara ağırlığının girilmesi](../../assets/en/device/calibration-and-tare/known-tare-weight-form.png){ .doc-screenshot }

Alternatif olarak mevcut platform ağırlığını sıfır olarak kabul edin:

![Mevcut ağırlığı sıfır olarak kabul etmek](../../assets/en/device/calibration-and-tare/use-current-weight-as-zero.png){ .doc-screenshot }

Dara alma fabrika kalibrasyon faktörünü değiştirmez.

Ayrı prosedürler: [Tartı terazisinin darasını alın](../guides/tare-scales.md) ve [Tartım terazilerini kalibre edin](../guides/calibrate-scales.md).
