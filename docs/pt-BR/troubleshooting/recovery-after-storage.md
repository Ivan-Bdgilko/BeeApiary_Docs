# Recupere o dispositivo após armazenamento de longo prazo

Após armazenamento prolongado, a bateria pode ficar completamente descarregada e o dispositivo pode não responder a uma conexão de alimentação normal. Se a tensão da célula 18650 estiver abaixo `3,5 В`, recupere o dispositivo na seguinte ordem.

!!! danger "Polaridade da bateria"
    Antes de remover a bateria, localize o `+` e `-` marcações na célula e no suporte. Lembre-se ou fotografe a orientação correta. Instalar a bateria com a polaridade invertida pode danificar permanentemente o dispositivo.

1. Remova a bateria do dispositivo.
2. Carregue-o em um carregador separado projetado para 18.650 células.
3. Após o carregamento, verifique a voltagem da bateria. Instale-o no dispositivo somente quando a tensão estiver `4,0 В` ou superior.
4. Instale a bateria seguindo cuidadosamente a polaridade marcada.
5. Conecte uma fonte de alimentação externa padrão à porta USB Type-C do dispositivo sem carregamento rápido Power Delivery (PD). Use um carregador com porta USB Tipo A e um cabo USB Tipo A para USB Tipo C; um cabo USB Type-C para USB Type-C não é recomendado.
6. Com a bateria instalada e a alimentação externa conectada, [ativar o dispositivo com a chave magnética](../device/installation.md#activation-reset).
7. Sincronize a hora de uma destas maneiras:

    - [conectar-se ao ponto de acesso do dispositivo por Wi-Fi](../guides/configure-local-wifi.md) e abra sua página inicial — este método está disponível por padrão;
    - [configurar a sincronização Bluetooth](../guides/configure-bluetooth-sync.md), abra o BeeApiary aplicativo e deixe o telefone próximo ao dispositivo – esse método funciona apenas quando as configurações correspondentes estão ativadas no dispositivo e no aplicativo.

8. Certifique-se de que a data e a hora estejam corretas e que o carimbo de data/hora da última sincronização tenha sido atualizado.

O dispositivo está pronto para operação normal após a restauração da energia e da hora.

Veja também [Energia e carregamento](../device/power.md) e [Sincronização de horário](../system/time-synchronization.md).
