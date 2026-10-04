# Sistem Kurulumu

!!! danger "Dikkat: cihaz zaten tam olarak yapılandırılmıştır"
    Yeni BeeApiary Arı kovanı tartım terazileri yapılandırılmış ve kalibre edilmiş olarak sağlanır. Kullanıcı numarası tartım terazisinin ayarlarında zaten kayıtlı olduğundan bunları yeniden yapılandırmanıza gerek yoktur.

    Kendi başınıza değişiklik yapmayın. Genellikle her şeyin işe yaraması için aşağıdaki ilk dört adımı tamamlamanız yeterlidir.

    İlgili talimatları sonuna kadar okumadan pili çıkarmayın, terazinin darasını almayın, kalibre etmeyin veya herhangi bir ayarı değiştirmeyin. İlk kurulum sırasında bunu yapmanız kesinlikle önerilmez.

!!! warning "SIM kartı takmadan önce"
    Yalnızca mikro SIM kullanın ve PIN korumasını önceden devre dışı bırakın.

1. Veri toplama ünitesinin kapağını açın.

    ![Açık veri toplama birimi](../../assets/common/device/installation/open-data-collection-unit.png){ .doc-photo }

2. Mikro SIM'i uygun yuvaya takın.

    Doğru kart konumu:

    ![Doğru şekilde yerleştirilmiş mikro SIM](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    SIM kartı takın ve yuvaya neredeyse tamamen girinceye kadar hafifçe bastırın; yerine kilitlendiğini onaylayan hafif bir tıklama duyuncaya kadar:

    ![mikro SIM yuvaya kilitlendi](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

3. [Cihazı etkinleştirin veya yeniden başlatın](../device/installation.md#activation-reset): Manyetik anahtarı ana ünitenin arkasındaki marka işaretine kısa süreliğine tutun.

    ![BeeApiary manyetik anahtar](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Markalı manyetik anahtarlı hedef](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

4. Yaklaşık bir dakika bekleyin ve ilk SMS'in önceden yapılandırılmış kullanıcı numarasına ulaştığını doğrulayın.

Bitti. Tebrikler: Cihaz veri topluyor, GSM üzerinden gönderiyor ve yerel bir arşiv tutuyor.

## Uygulama – gerekirse

 BeeApiary Uygulamanın sıradan SMS mesajları almasına gerek yoktur. Cihaz verilerini otomatik olarak almak, ölçümleri görüntülemek ve diğer uygulama özelliklerini kullanmak istiyorsanız bunu yükleyin.

1. [Şunu yükleyin: BeeApiary uygulama](app-only.md) ve SMS mesajlarını işlemesine izin verdiğinizden emin olun.
2. Uygulamada şunu seçin: **Cihaz ekle**.
3. Takılı olan mikro SIM numarasını girin BeeApiary arı kovanı tartı terazileri.

!!! note
    Kullanıcının telefon numarasını değil, cihaza takılı SIM kartın numarasını girin.

İlk SMS gelmezse ayarları rastgele değiştirmeyin. Bkz. [SMS alınmadı](../troubleshooting/no-sms.md). Kullanıcı numarasını şu şekilde değiştirin: [GSM ayarları](../guides/configure-gsm.md) yalnızca gerektiğinde.

[Video: SIM kartı takma](https://www.youtube.com/shorts/GF2KLso4DMo)

Daha fazla bilgi edinin: [GSM ve SMS](../system/gsm-and-sms.md) ve [Veri akışı](../system/data-flow.md).
