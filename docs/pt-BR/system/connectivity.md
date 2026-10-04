---
title: "Monitoramento do apiário via GSM, Wi-Fi e Bluetooth"
description: "Compare GSM, Wi-Fi direto, rede de apiário e Bluetooth para receber medições em BeeApiary: requisitos de conexão e histórico disponível."
---

# Monitoramento do apiário via GSM, Wi-Fi e Bluetooth { #_1 }

Para monitoramento do apiário, dados do BeeApiary As balanças colmeias podem acessar o aplicativo de quatro maneiras: através de GSM/SMS, conexão Wi-Fi direta, rede Wi-Fi do apiário ou Bluetooth. A escolha entre monitoramento local e remoto depende da localização do telefone e da conexão disponível próximo às balanças.

| Canal | Localização do telefone | Requisitos | Como os dados chegam ao aplicativo |
|---|---|---|---|
| [GSM e SMS](gsm-and-sms.md) | Em qualquer lugar com cobertura móvel | Um cartão SIM no dispositivo com plano básico de SMS | O aplicativo processa mensagens SMS automaticamente; Internet móvel não é necessária |
| [Conexão direta ao ponto de acesso do dispositivo](local-wifi.md#direct-access-point) | Perto do dispositivo | Ative o dispositivo com a chave magnética e conecte-o `apiary_net` dentro do intervalo disponível, geralmente cerca de um minuto | O aplicativo encontra o dispositivo, pede permissão para recuperar o arquivo e importa os dados após a confirmação |
| [Roteamento pela rede Wi-Fi do apiário](local-wifi.md#apiary-wifi-routing) | Em qualquer lugar com acesso à Internet | Uma rede Wi-Fi configurada com acesso à Internet deve estar disponível perto do dispositivo | Os dados são encaminhados para o aplicativo automaticamente; não é necessário um cartão SIM separado para cada dispositivo |
| [Bluetooth](bluetooth.md) | Perto, dentro do alcance do Bluetooth | **BLE info**, a digitalização BLE e a operação em segundo plano do aplicativo estão habilitadas; a hora está sincronizada; nenhum cartão SIM ou Internet é necessário | O aplicativo sincroniza automaticamente os dados atuais e pode restaurar o histórico disponível |

## GSM e SMS

O dispositivo envia mensagens SMS regulares ou compactas sem Internet móvel. O aplicativo reconhece mensagens compactas e adiciona automaticamente as medidas ao armazenamento local do telefone.

## Conexão direta ao dispositivo

Após a ativação com a chave magnética, o dispositivo cria temporariamente o `apiary_net` ponto de acesso. Um telefone conectado a ele não precisa de cartão SIM ou acesso à Internet. O aplicativo encontra o dispositivo automaticamente, mas baixa o arquivo somente depois que o usuário confirma a solicitação.

Para o procedimento detalhado, consulte [Baixe o arquivo](../guides/download-archive.md).

## Roteamento pela rede Wi-Fi do Apiário

O dispositivo pode usar uma rede Wi-Fi existente com acesso à Internet no apiário. O proprietário recebe dados remotamente no aplicativo sem um cartão SIM separado para cada dispositivo.

Antes da configuração inicial, o aplicativo deve ter recebido dados do dispositivo pelo menos uma vez por SMS ou download direto de arquivo. O registro é concluído em um telefone com acesso à Internet, e as configurações de Wi-Fi e nuvem preparadas são então transferidas para o dispositivo por meio de seu `apiary_net` ponto de acesso.

O relé online não armazena dados. Cópias permanentes permanecem no BeeApiary memória da balança de colmeia e no telefone do usuário.

Para o procedimento detalhado, consulte [Configurar a sincronização através da rede Wi-Fi do apiário](../guides/configure-wifi-sync.md).

## Bluetooth

Quando o telefone está dentro do alcance do Bluetooth, o aplicativo sincroniza automaticamente os dados disponíveis. Isso não requer um cartão SIM, Internet móvel ou ativação do `apiary_net` ponto de acesso. Quando a recuperação do histórico está habilitada, lacunas temporárias podem ser preenchidas durante a próxima conexão bem-sucedida.

Para uma explicação, veja [Sincronização de dados Bluetooth](bluetooth.md). Para o procedimento prático, consulte [Configurar a sincronização Bluetooth](../guides/configure-bluetooth-sync.md).

## Operação sem conexão

Uma perda temporária ou completa de qualquer canal de comunicação não interrompe as medições: o dispositivo continua a gravá-las no microSD. Depois que a conexão for restaurada, o aplicativo poderá recuperar os dados perdidos, mas a profundidade do histórico disponível depende do canal selecionado.

| Canal | Histórico disponível após a conexão ser restaurada | Nota |
|---|---|---|
| GSM e SMS | 2 a 12 horas | Depende da programação de transmissão de SMS configurada |
| Conexão direta ao ponto de acesso do dispositivo | Até 1 ano | Os dados podem ser baixados se os registros correspondentes estiverem presentes no arquivo local |
| Bluetooth | 1 dia a 1 semana | Depende da configuração de recuperação do histórico e dos registros disponíveis |
| Roteamento pela rede Wi-Fi do apiário | O histórico não está disponível | O relé online transfere os dados atuais, mas não os armazena no servidor |

Estes limites aplicam-se apenas à quantidade de dados perdidos que podem ser restaurados através de um canal específico. O local [Arquivo microSD](data-storage.md) não tem limite de armazenamento de um ano: sua profundidade é limitada apenas pela capacidade do cartão, que é suficiente para toda a vida útil esperada do aparelho. Se necessário, os dados também podem ser lidos diretamente do cartão microSD.
