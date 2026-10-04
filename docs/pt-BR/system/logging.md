# Registros

O BeeApiary As balanças de colmeia fornecem três tipos diferentes de dados:

1. um arquivo de medição CSV para o usuário;
2. um registro de serviço do dispositivo no cartão microSD;
3. um registro de engenharia em tempo real por meio da interface da web.

Os logs de serviço destinam-se a diagnósticos e não a visualização de rotina. Eles estão disponíveis no cartão microSD; a interface web também fornece os endereços de serviço `/log` e `/tracecontrol`.

!!! warning
    Não altere o nível de log de engenharia, a menos que seja necessário ou recomendado pelo desenvolvedor. Use o [arquivo de dados](data-storage.md) para analisar medições.
