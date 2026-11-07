# Calibração e Tara

!!! danger "Um novo dispositivo não precisa de calibração"
    A calibração é necessária principalmente após um reparo ou perda de dados de calibração de fábrica. Não use isso como uma forma geral de solucionar uma leitura incorreta de peso.

<span id="calibration"></span>
## Calibração

1. Desconecte a fonte de alimentação externa.
2. Coloque todos os sensores de peso sobre uma superfície firme e nivelada e deixe a plataforma vazia.
3. Conecte-se ao ponto de acesso do dispositivo e abra **Configurações Gerais → Configurações da balança** em sua interface web.

    ![Botão para abrir as configurações da balança](../../assets/en/device/calibration-and-tare/open-scale-settings.png){ .doc-screenshot }

4. Começar **Calibração Zero** e espere terminar sem tocar na plataforma.

    A tela mostra dois estágios de calibração:

    ![etapas de calibração de balança](../../assets/en/device/calibration-and-tare/calibration-steps.png){ .doc-screenshot }

    ![Calibração zero em andamento](../../assets/en/device/calibration-and-tare/zero-calibration-progress.png){ .doc-screenshot }

5. Selecione um peso de referência disponível de 500, 1.000 ou 5.000 g e coloque-o na plataforma.

    ![Selecionando o peso de referência](../../assets/en/device/calibration-and-tare/reference-weight-selection.png){ .doc-screenshot }

6. Começar **Calibração de Referência** e espere pelo resultado.

    ![Calibração de referência em andamento](../../assets/en/device/calibration-and-tare/reference-weight-calibration-progress.png){ .doc-screenshot }

    ![resultado da calibração da balança](../../assets/en/device/calibration-and-tare/calibration-result.png){ .doc-screenshot }

Resultado: o dispositivo salvou os novos valores de calibração. Verifique se o peso de referência é exibido.

<span id="tare"></span>
## Tara

A tara exclui o peso da plataforma ou de outra estrutura permanente.

1. [Conecte-se à interface web da balança](../guides/configure-local-wifi.md).
2. Abra **Configurações gerais → Configurações da balança**.
3. Escolha um método:

    - Se souber o peso da tara, informe-o em gramas e selecione **Definir peso da tara**.

        ![Inserindo um peso de tara conhecido](../../assets/en/device/calibration-and-tare/known-tare-weight-form.png){ .doc-screenshot }

    - Ou deixe a estrutura sobre os sensores e aceite o valor atual como zero.

        ![Aceitando o peso atual como zero](../../assets/en/device/calibration-and-tare/use-current-weight-as-zero.png){ .doc-screenshot }

4. Confira a leitura ao terminar.

Resultado: o dispositivo subtrai a tara das medições seguintes. A tara não altera o fator de calibração de fábrica.
