# Como baixar o arquivo

Antes de começar, certifique-se de que BeeApiary o aplicativo está atualizado por meio do Google Play e as balanças de colmeia estão executando firmware lançado em agosto de 2024 ou posterior. Se a versão instalada for mais antiga ou você não tiver certeza da data, siga [Atualize o BeeApiary Firmware de balanças para colmeia](update-device.md).

O download manual do arquivo é útil quando as balanças não possuem cartão SIM, outros métodos de sincronização estão temporariamente indisponíveis ou aparecem lacunas nas medições. O aplicativo importa os dados armazenados e os adiciona ao histórico local.

!!! warning "microSD e carga da bateria"
    Um cartão microSD funcional contendo os dados disponíveis deve ser instalado na balança. Uma conexão Wi-Fi direta mantém a balança ativa e aumenta o consumo de energia, portanto, não execute este procedimento mais de uma vez por dia, a menos que seja necessário.

1. [Ative ou reinicie o BeeApiary balanças de colmeia](../device/installation.md#activation-reset) com a chave magnética.
2. Dentro do intervalo disponível, geralmente cerca de um minuto, conecte o telefone ao `apiary_net` e permaneça perto da balança.
3. Abra o BeeApiary aplicativo.
4. Aguarde até que o aplicativo detecte automaticamente as balanças próximas.
5. No **"Dispositivo próximo. Baixar arquivo?"** solicitar, toque **Sim**.

    ![BeeApiary solicitação do aplicativo para baixar o arquivo de um dispositivo próximo](../../assets/en/guides/download-archive/nearby-device-archive-prompt.jpg){ .doc-screenshot }

6. Aguarde a conclusão da importação e desconecte imediatamente o telefone do `apiary_net`. Uma vez desconectadas, as balanças podem entrar no modo de espera e evitar o consumo desnecessário da bateria.
7. Visualize os dados baixados usando as telas padrão do aplicativo.

    ![BeeApiary tela inicial do aplicativo com medidas importadas](../../assets/en/app/main-screen/app-home-screen.png){ .doc-screenshot }

Após a confirmação, o aplicativo baixa o arquivo automaticamente e armazena uma cópia local das medições. Se outros canais perderem alguns dados, o arquivo poderá preencher as lacunas correspondentes no histórico. O formato do arquivo e o período de retenção estão descritos em [Armazenamento de dados](../system/data-storage.md).
