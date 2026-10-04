# Güç Sorunları

!!! note "Şarj etme"
    Cihaz, USB Güç Dağıtımı (PD) dahil olmak üzere hızlı şarjı desteklemez. Test için, USB Tip A bağlantı noktası ve USB Tip A'dan USB Tip C'ye kabloya sahip standart bir güç kaynağı kullanın. USB Type-C'den USB Type-C'ye kablo kullanılması önerilmez.

1. Uzun süreli saklamanın ardından akü voltajını kontrol edin. Aşağıda ise `3,5 В`, takip et [Depolamadan sonra kurtarma prosedürü](recovery-after-storage.md).
2. Diğer durumlarda, çalışan standart bir güç kaynağını USB Type-C bağlantı noktasına bağlayın ve pilin şarj olmasını sağlayın.
3. Pilin cihaza takılı olduğundan emin olun. BeeApiary arı kovanı tartım terazileri söz konusu modelin konfigürasyonu için tasarlanmıştır. 18650 hücre kullanan modellerde bu türden en az bir hücrenin kurulu olması gerekir.
4. Pil değiştirilmişse, tutucudaki işaretlere göre kutuplarını kontrol edin.
5. Kritik bir deşarjın ardından akü şarjının düzelmesini bekleyin; cihaz bir sonraki döngü sırasında normal çalışmasına devam edebilir.
6. Kurtarma işleminden sonra saati kontrol edin ve gerekirse senkronize edin.

!!! danger
    18650 hücresi olmadan cihaza yalnızca harici USB'den güç sağlamaya çalışmayın. Yanlış pil polaritesi cihaza kalıcı hasar verebilir.

Ayrıntılar için bkz. [Güç](../device/power.md).
