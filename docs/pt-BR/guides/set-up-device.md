# Como configurar a balança de colmeia BeeApiary

1. Carregue o dispositivo através de USB Type-C.

    !!! note "Escolhendo um carregador e cabo"
        O dispositivo não suporta carregamento rápido, incluindo USB Power Delivery (PD). Use uma fonte de alimentação padrão com uma porta USB Tipo A e um cabo USB Tipo A–USB Tipo C. Um cabo USB Type-C – USB Type-C não é recomendado para carregamento.

2. Instale o dispositivo e os sensores de acordo com as [diretrizes de posicionamento](../device/placement.md).
3. Insira um micro-SIM com a proteção PIN desativada.

    Use o formato micro SIM:

    ![Comparação de formatos de cartão SIM](../../assets/pt-BR/quick-start/gsm/micro-sim-format-comparison.png){ .doc-photo }

    Cartão instalado corretamente:

    A posição do módulo GSM difere entre placas anteriores a 2026 e placas mais recentes a partir de 2026.

    **Placa anterior (antes de 2026):**

    ![Micro-SIM instalado corretamente](../../assets/common/device/installation/micro-sim-insertion-orientation.jpeg){ .doc-photo }

    **Placa mais recente (a partir de 2026):**

    ![Orientação do micro-SIM na placa mais recente](../../assets/common/device/installation/micro-sim-new-board-orientation.png){ .doc-photo }

    Insira o cartão SIM e pressione-o suavemente quase completamente no slot até ouvir um clique suave confirmando que está travado no lugar:

    **Placa anterior (antes de 2026):**

    ![micro-SIM bloqueado no slot](../../assets/common/device/installation/micro-sim-locked-in-slot.jpeg){ .doc-photo }

    **Placa mais recente (a partir de 2026):**

    ![micro-SIM travado na placa mais recente](../../assets/common/device/installation/micro-sim-new-board-locked.png){ .doc-photo }

4. <span id="activation-reset"></span>Ative ou reinicie o dispositivo: segure brevemente a chave magnética contra a marca na parte traseira da unidade principal.

    ![BeeApiary chave magnética](../../assets/common/device/installation/magnetic-key.png){ .doc-photo }

    ![Alvo de chave magnética de marca](../../assets/common/device/installation/magnetic-key-target.png){ .doc-photo }

5. Se precisar verificar ou alterar as configurações, [conecte-se à `apiary_net`](configure-local-wifi.md) e abra `http://192.168.4.1`. Caso contrário, pule esta etapa.
6. O número do proprietário normalmente já é configurado pelo fabricante. Apenas se necessário, [verifique, altere ou remova o número nas configurações GSM](configure-gsm.md).
7. Se você se conectou à `apiary_net`, desconecte-se. Aguarde o primeiro SMS: ele geralmente chega antes de o dispositivo entrar em repouso, cerca de um minuto após a desconexão ou ativação.

    Após alterar a transmissão, a calibração ou outros ajustes, pode ser necessário esperar o dispositivo entrar em repouso e ativá-lo novamente com a chave magnética, sem reconectar à `apiary_net`.

Resultado: o dispositivo coleta medições, envia-as ao proprietário e armazena um arquivo.
