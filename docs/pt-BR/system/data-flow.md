---
title: "Como os dados da colmeia chegam ao telefone"
description: "Como BeeApiary mede, armazena e transfere dados da colmeia para o seu telefone para visualizar leituras atuais, histórico e gráficos."
---

# Como os dados da colmeia chegam ao telefone { #_1 }

BeeApiary o monitoramento de colmeias abrange medição, armazenamento local e transmissão de dados para o aplicativo. As etapas abaixo mostram o caminho desde uma medição no dispositivo até as leituras, histórico e gráficos atuais no seu telefone.

1. No início de cada hora, o BeeApiary balanças de colmeia fazem as medições configuradas.
2. O resultado é salvo no arquivo microSD local quando o cartão está disponível.
3. O dispositivo disponibiliza os dados pelo canal configurado:

    - envia uma mensagem SMS normal ou compacta de acordo com a programação;
    - encaminha dados pela rede Wi-Fi do apiário;
    - [transmite os dados disponíveis por Bluetooth](bluetooth.md) quando o telefone está próximo;
    - fornece o arquivo ao aplicativo por meio de seu próprio ponto de acesso após a confirmação do usuário.

4. O aplicativo reconhece os valores recebidos e os adiciona ao armazenamento local do celular.
5. O usuário visualiza valores atuais, histórico e gráficos.

A ausência de GSM, Wi-Fi, Bluetooth ou de um telefone próximo não interrompe o processo de medição principal. Os dados podem ser transferidos para o aplicativo quando uma conexão estiver disponível.

Quando os dados são roteados remotamente por Wi-Fi, o relé online não os armazena. Cópias permanentes permanecem no BeeApiary memória da balança de colmeia e no telefone do usuário.

Para uma comparação de canais, consulte [Recebendo dados no aplicativo](connectivity.md).

Para configurar o canal remoto, consulte [Sincronização Através da Rede Wi-Fi do Apiário](../guides/configure-wifi-sync.md).

Para configurar o canal automático local, consulte [Sincronização Bluetooth](../guides/configure-bluetooth-sync.md).
