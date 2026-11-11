# Não é possível conectar-se ao Wi-Fi

!!! warning "Wi-Fi do dispositivo: somente 2,4 GHz"
    O ponto de acesso `apiary_net` das balanças funciona somente em 2,4 GHz. O celular, tablet ou notebook deve oferecer suporte a conexões Wi-Fi nessa faixa. Selecione o SSID de uma rede de 2,4 GHz; redes exclusivas de 5 GHz não são compatíveis.

1. [Ative ou reinicie o BeeApiary balanças de colmeia](../guides/set-up-device.md#activation-reset): segure brevemente a chave magnética contra a marca na parte traseira da unidade principal.
2. Procure a rede durante o primeiro minuto após a reinicialização.
3. Verifique o SSID; o valor padrão é `apiary_net`.
4. Verifique a senha; o valor padrão é `apiary_wifi` a menos que tenha sido alterado.
5. Após conectar, abra manualmente `http://192.168.4.1`.
6. Se a página não abrir, desative os dados móveis ou a mudança automática para uma conexão com a Internet nesta sessão local e tente novamente.

Depois de decorrido um minuto, pressione novamente a tecla brevemente contra a marca. Para obter detalhes, consulte [Wi-Fi local](../system/local-wifi.md).
