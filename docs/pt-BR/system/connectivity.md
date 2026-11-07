---
title: "Monitoramento do apiário via GSM, Wi-Fi e Bluetooth"
description: "Compare GSM, Wi-Fi direto, rede de apiário e Bluetooth para receber medições em BeeApiary: requisitos de conexão e histórico disponível."
---

# Monitoramento do apiário via GSM, Wi-Fi e Bluetooth { #_1 }

Para monitoramento do apiário, dados do BeeApiary As balanças colmeias podem acessar o aplicativo de quatro maneiras: através de GSM/SMS, conexão Wi-Fi direta, rede Wi-Fi do apiário ou Bluetooth. A escolha entre monitoramento local e remoto depende da localização do telefone e da conexão disponível próximo às balanças.

| Canal | Localização do telefone | Requisitos | Como os dados chegam ao aplicativo |
|---|---|---|---|
| [GSM e SMS](gsm-and-sms.md) | Em qualquer lugar com cobertura móvel | Um cartão SIM no dispositivo com plano básico de SMS; permissão de SMS para o aplicativo | O aplicativo processa SMS compactos automaticamente; não é necessária Internet móvel. [Configurar GSM](../guides/configure-gsm.md) |
| [Conexão direta ao ponto de acesso do dispositivo](local-wifi.md#direct-access-point) | Perto do dispositivo | Ative o dispositivo com a chave magnética e conecte-o `apiary_net` dentro do intervalo disponível, geralmente cerca de um minuto; SIM e Internet não são necessários | O aplicativo encontra o dispositivo, pede permissão para recuperar o arquivo e importa os dados após a confirmação. [Baixar arquivo](../guides/download-archive.md) |
| [Roteamento pela rede Wi-Fi do apiário](local-wifi.md#apiary-wifi-routing) | Em qualquer lugar com acesso à Internet | Uma rede Wi-Fi configurada com acesso à Internet deve estar disponível perto do dispositivo | Os dados são encaminhados para o aplicativo automaticamente; não é necessário um cartão SIM separado para cada dispositivo. [Configurar Wi-Fi](../guides/configure-wifi-sync.md) |
| [Bluetooth](bluetooth.md) | Perto, dentro do alcance do Bluetooth | **BLE info**, a digitalização BLE e a operação em segundo plano do aplicativo estão habilitadas; a hora está sincronizada; nenhum cartão SIM ou Internet é necessário | O aplicativo sincroniza automaticamente os dados atuais e pode restaurar o histórico disponível. [Configurar Bluetooth](../guides/configure-bluetooth-sync.md) |

## GSM e SMS

SMS comuns podem ser lidos sem o aplicativo; o aplicativo salva mensagens compactas como medições. [Formatos de SMS](gsm-and-sms.md).

## Conexão direta ao dispositivo

O telefone conectado recebe o arquivo somente após confirmação. [Conectar ao ponto de acesso](../guides/configure-local-wifi.md).

## Roteamento pela rede Wi-Fi do Apiário

Antes da configuração, o aplicativo deve ter recebido dados ao menos uma vez por SMS ou download direto do arquivo. O serviço não é armazenamento permanente: as cópias permanecem na balança e no telefone. Ele pode ficar instável ou ser pago; confira [compatibilidade e condições](../guides/configure-wifi-sync.md).

## Bluetooth

Com a recuperação do histórico ativada, lacunas podem ser preenchidas na próxima conexão bem-sucedida. [Funcionamento e compatibilidade](bluetooth.md).

## Operação sem conexão

Uma perda temporária ou completa de qualquer canal de comunicação não interrompe as medições: o dispositivo continua a gravá-las no microSD. Depois que a conexão for restaurada, o aplicativo poderá recuperar os dados perdidos, mas a profundidade do histórico disponível depende do canal selecionado.

| Canal | Histórico disponível após a conexão ser restaurada | Nota |
|---|---|---|
| GSM e SMS | 2 a 12 horas | Depende da programação de transmissão de SMS configurada |
| Conexão direta ao ponto de acesso do dispositivo | Até 1 ano | Os dados podem ser baixados se os registros correspondentes estiverem presentes no arquivo local |
| Bluetooth | 1 dia a 1 semana | Depende da configuração de recuperação do histórico e dos registros disponíveis |
| Roteamento pela rede Wi-Fi do apiário | O histórico não está disponível | O relé online transfere os dados atuais, mas não os armazena no servidor |

Estes limites aplicam-se apenas à quantidade de dados perdidos que podem ser restaurados através de um canal específico. O local [Arquivo microSD](data-storage.md) não tem limite de armazenamento de um ano: sua profundidade é limitada apenas pela capacidade do cartão, que é suficiente para toda a vida útil esperada do aparelho. Se necessário, os dados também podem ser lidos diretamente do cartão microSD.
