# Como configurar novas balanças BeeApiary

1. Carregue o dispositivo através de USB Type-C.

    !!! note "Escolhendo um carregador e cabo"
        O dispositivo não suporta carregamento rápido, incluindo USB Power Delivery (PD). Use uma fonte de alimentação padrão com uma porta USB Tipo A e um cabo USB Tipo A–USB Tipo C. Um cabo USB Type-C – USB Type-C não é recomendado para carregamento.

2. Instale o dispositivo e os sensores de acordo com as [diretrizes de posicionamento](../device/placement.md).
3. Insira um micro-SIM com a proteção PIN desativada.

    Use o formato micro SIM:

    ![Comparação de formatos de cartão SIM](../../assets/en/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Cartão instalado corretamente:

    ![Micro-SIM instalado corretamente](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    Insira o cartão SIM e pressione-o suavemente quase completamente no slot até ouvir um clique suave confirmando que está travado no lugar:

    ![micro-SIM bloqueado no slot](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

4. Ative ou reinicie o dispositivo: segure brevemente a chave magnética contra a marca na parte traseira da unidade principal.

    ![BeeApiary chave magnética](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Alvo de chave magnética de marca](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

    Para obter mais informações, consulte [Ativação e reinicialização](../device/installation.md#activation-reset).

5. Conectar-se a `apiary_net` e aberto `http://192.168.4.1`.
6. Digite o número de telefone do proprietário em formato internacional.
7. Desconectar de `apiary_net` e verifique a primeira mensagem SMS.

Resultado: o dispositivo coleta medições, envia-as ao proprietário e armazena um arquivo.
