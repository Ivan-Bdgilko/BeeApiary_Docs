# Armazenamento de dados

O BeeApiary As balanças de colmeia registram dados em microSD, independentemente de o GSM estar disponível ou não. Um `YEARxx` é criado para cada ano, com arquivos CSV para cada mês contendo data, hora e leituras disponíveis.

O arquivo CSV pode conter:

- `Date`, `Time`;
- `Weight[Kg]`;
- `T1 [°C]`, `T2 [°C]`, e temperaturas adicionais;
- carga da bateria;
- pressão e umidade;
- RSSI GSM;
- metadados de serviço de firmware.

As colunas dependem da configuração do dispositivo e da versão do firmware. As medições usam aproximadamente 2 MB por ano, enquanto os logs de serviço usam cerca de 40 a 50 MB por ano.

Para recuperar os dados, consulte [Baixe o arquivo](../guides/download-archive.md).
