# Configurações adicionais do dispositivo

O **Configurações adicionais** página pertence à interface web do BeeApiary balanças de colmeia. Ele especifica qual hardware adicional está instalado e controla canais individuais de transmissão de dados.

## Como abri-lo

1. [Conecte-se ao ponto de acesso do dispositivo](../guides/configure-local-wifi.md).
2. Abrir `http://192.168.4.1`.
3. Na página inicial, selecione **Configurações adicionais**.
4. Leia o aviso da interface da web. Prossiga apenas para verificar ou alterar deliberadamente as configurações.

!!! warning "Não altere as configurações aleatoriamente"
    Um valor incorreto pode interromper a operação do dispositivo. Habilite sinalizadores de hardware somente quando o hardware correspondente estiver instalado fisicamente. Não altere as configurações ou chaves de rede desnecessariamente.

![Configurações adicionais na interface web do BeeApiary balanças de colmeia](../../assets/uk/device/additional-settings/device-additional-settings.jpg){ .doc-screenshot }

Os valores de rede na captura de tela são apenas exemplos. Eles serão diferentes no seu dispositivo.

## Interruptores

| Artigo | Função | Notas |
|---|---|---|
| **BLE info** | Permite a sincronização local de dados via Bluetooth. | Depois de habilitá-lo, configure [Sincronização Bluetooth no aplicativo](../guides/configure-bluetooth-sync.md). |
| **GSM** | Habilita o módulo GSM e transmissão de dados via SMS. | Desative-o se a comunicação GSM não for utilizada, por exemplo, durante o armazenamento no inverno sem transmissão de dados. |
| **Sincronização Wi-Fi** | Permite a transmissão automática de dados através de uma rede Wi-Fi externa. | Geralmente ativado automaticamente quando o aplicativo transfere as configurações preparadas de Wi-Fi e nuvem para o dispositivo. Não ative-o manualmente sem os campos de rede corretos. |
| **Tela** | Informa ao dispositivo que um display OLED está fisicamente instalado e permite sua operação. | Ative somente se um monitor estiver instalado. |
| **Invertido** | Gira a imagem do display OLED em 180°. | Relevante apenas quando **Tela** está habilitado. |
| **Tempo** | Ativa o sensor meteorológico instalado para pressão, umidade e temperatura adicional. | Habilite somente se o sensor estiver instalado. |
| **Trocar T1/T2** | Troca os valores transmitidos dos principais termômetros T1 e T2. | Útil se os sensores internos e externos tiverem sido trocados fisicamente. Deixe os nomes e configurações dos canais no aplicativo inalterados. |
| **Sensor PIR** | Ativa a entrada de alarme para PIR ou outro sensor de despertar de sistema compatível. | Habilite somente se um sensor estiver conectado. |

## Campos de rede

| Campo | Função | Notas |
|---|---|---|
| **Rede Wi-Fi** | Nome da rede Wi-Fi externa à qual o dispositivo se conectará. | Deve corresponder exatamente ao SSID da rede disponível próximo ao dispositivo. |
| **Senha Wi-Fi** | Senha da rede Wi-Fi externa. | A interface da web mascara o valor. |
| **Chave STA** | Chave de transmissão do serviço obtida durante o cadastro pelo app. | Não edite manualmente. |

É mais seguro definir parâmetros de Wi-Fi através [configurações de sincronização no aplicativo](../guides/configure-wifi-sync.md). O aplicativo cria os dados necessários e os transfere para o dispositivo durante uma conexão direta com `apiary_net`.
