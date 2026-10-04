# Como configurar a sincronização Bluetooth

!!! danger "Compatibilidade do dispositivo"
    Esse recurso é compatível apenas com dispositivos fabricados após agosto de 2026. Dispositivos fabricados anteriormente também podem ganhar essa funcionalidade, mas devem ser atualizados de fábrica. Atualmente não existe um patch simples que você mesmo possa instalar.

Este procedimento configura a recuperação automática de dados de BeeApiary balanças de colmeia enquanto o telefone está por perto. A sincronização não requer cartão SIM ou acesso à Internet.

## Antes de começar

1. Certifique-se de que as balanças atendam aos requisitos de compatibilidade acima.
2. [Sincronize o relógio da balança](../system/time-synchronization.md) com o telefone. A diferença não deve ultrapassar dois minutos.
3. Ligue o Bluetooth no telefone.
4. Conceda ao aplicativo todas as permissões solicitadas, incluindo permissões de Bluetooth.
5. Permita que o aplicativo seja executado em segundo plano e acorde no horário necessário. Revise o atual [recomendações de instalação de aplicativos](../app/installation.md).

!!! warning "Verifique o tempo antes da configuração"
    Se a diferença ultrapassar dois minutos, a balança poderá ficar disponível antes ou depois do telefone começar a escutar, impedindo a sincronização automática.

## Habilite informações BLE nas balanças

1. [Conecte-se ao ponto de acesso da balança](configure-local-wifi.md).
2. Abrir `http://192.168.4.1` e selecione **Configurações adicionais**.
3. Selecione **BLE info** e salve as alterações.

Esta opção e as outras opções são explicadas em [Configurações adicionais do dispositivo](../device/additional-settings.md).

## Habilite a sincronização no aplicativo

4. Abra o menu principal do aplicativo, vá para **Configurações**e abra **Configurações adicionais**.
5. Habilitar **Procure dispositivos BLE** para que o aplicativo possa encontrar balanças próximas e receber medições.
6. Habilitar **História do BLE** para que o aplicativo também recupere o histórico armazenado, incluindo dados do dia anterior.

    ![Opções de Bluetooth nas configurações adicionais do BeeApiary Aplicativo Android](../../assets/en/app/additional-settings/app-additional-settings.jpg){ .doc-screenshot }

    !!! warning "Habilite as opções necessárias"
        A captura de tela é um exemplo geral, portanto, ambos os interruptores Bluetooth são mostrados como desativados. **Procure dispositivos BLE** deve estar habilitado para sincronização. Habilitando **História do BLE** também é recomendado para que o aplicativo possa recuperar o histórico disponível e restaurar medições perdidas.

    Para obter uma descrição completa desta tela, consulte [Configurações adicionais do aplicativo](../app/additional-settings.md).

7. Volte para a tela inicial do aplicativo. Mantenha o Bluetooth ativado e o telefone dentro do alcance confiável do Bluetooth durante o próximo ciclo horário.

## Verifique o resultado

A sincronização ocorre somente quando **BLE info** está habilitado nas balanças e no Bluetooth e as opções de aplicativos correspondentes estão habilitadas no telefone. As balanças ficam disponíveis para comunicação durante um despertar programado ou após [ativação com a chave magnética](../device/installation.md#activation-reset).

O aplicativo pode trocar dados enquanto está aberto ou em segundo plano se o Android permitir que ele seja executado e ativado no horário necessário.

8. Aguarde uma mensagem confirmando que os dados foram recebidos.

    ![Resultado do recebimento de medições via Bluetooth no BeeApiary aplicativo](../../assets/en/system/bluetooth/bluetooth-sync-result.jpg){ .doc-screenshot }

    Esta janela mostra:

    - o nome da colmeia e o número da balança;
    - o último conjunto de medidas disponíveis para configuração das balanças;
    - a data e a hora da medição recebida;
    - o horário e o resultado da sincronização do relógio.

    Ao conectar a balanças que ainda não foram registradas, um **Adicionar dispositivo** botão também pode aparecer. Use-o para completar o padrão [procedimento para adicionar BeeApiary balanças de colmeia](../app/add-device.md) uma vez. O aplicativo irá reconhecê-los automaticamente.

9. Toque **OK**. Se necessário, abra novamente a última mensagem através **BLE Info** no menu principal.
10. Certifique-se de que os novos valores apareçam na tela inicial e nos gráficos do aplicativo.

Pronto: enquanto o telefone estiver por perto, o aplicativo recuperará automaticamente os dados disponíveis. Se a conexão ficou indisponível por várias horas, habilitada **História do BLE** pode restaurar as medições perdidas durante a próxima sincronização bem-sucedida, dentro da profundidade do histórico disponível de um dia a uma semana.

Para obter mais informações sobre como funciona, consulte [Sincronização de dados Bluetooth](../system/bluetooth.md).
