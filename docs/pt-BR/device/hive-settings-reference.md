# `HIVE*.XML`: configurações de colmeia

A configuração da colmeia é armazenada em `/setting/<hive>.xml`. O `<hive>` o nome base é especificado pelo `hive1`, `hive2`e atributos subsequentes em [`mset.xml`](settings-reference.md); o `.xml` extensão é adicionada automaticamente.

!!! danger "Valores dependentes do hardware"
    Não copie o `scales` seção de outro dispositivo. Os pinos da placa e os valores de calibração dependem da versão do hardware e do conjunto específico de sensores de peso. Valores incorretos podem distorcer as medições ou torná-las indisponíveis.

Veja o [regras de edição segura](service-reference.md).

## Reescrita Automática

Depois de ler o arquivo, o dispositivo poderá salvá-lo novamente:

- um arquivo ausente ou danificado é criado a partir do estado atual disponível;
- faltando `hive`, `thermometer`, ou `schedule` seções permitem normalização;
- um atributo ausente em um existente `scales` ou `thermometer` a seção é substituída por um valor substituto e permite a normalização;
- completo `scales`, `booster`e `range_alarmer` as seções são opcionais;
- normalização também escreve o `booster`, `range_alarmer`, `thermometer`e `schedule` seções, mesmo que algumas delas estivessem ausentes do arquivo de origem.

## `hive`

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `hive_name` | Nome da colmeia interna | Opcional | String; recomenda-se até 8 caracteres ASCII para compatibilidade | Nome de `mset.xml`, por exemplo `hive1` | `hive_<індекс>`; o arquivo está marcado para reescrever | `ADVANCED` |
| `bus_number` | Número da colmeia no barramento interno | Opcional | Número inteiro; os limites não são verificados | Índice de instância, `0` para o primeiro | Índice de instância; o arquivo está marcado para reescrever | `SERVICE` |
| `main_device` | Indica o dispositivo principal com sensores de hardware locais | Opcional | `true`, `false` | `true` em um arquivo recém-criado | A instância não se torna o dispositivo principal; a omissão por si só não permite reescrever | `SERVICE` |

O suporte para dispositivos subordinados está obsoleto. O valor `main_device="false"` é aceito durante o carregamento, mas após salvar, o atributo se torna `main_device="true"`. Não use `false` como uma configuração estável.

## `scales`

Se a seção estiver totalmente ausente, o objeto da balança não será criado e a medição de peso ficará desativada. Se a seção existir, cada campo ausente ou incorreto será substituído por um valor de reserva, após o que o arquivo inteiro poderá ser regravado.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `pin_hc711_data` | GPIO de dados do HX711 | Obrigatório se a seção existir | GPIO para a placa específica | A seção não é criada automaticamente; dependente de hardware | Pin para a placa específica; o arquivo foi reescrito | `SERVICE` |
| `pin_hc711_clk` | GPIO de clock do HX711 | Obrigatório se a seção existir | GPIO para a placa específica | A seção não é criada automaticamente; dependente de hardware | Pin para a placa específica; o arquivo foi reescrito | `SERVICE` |
| `gain` | Modo de ganho HX711 | Obrigatório se a seção existir | Valor do modo de ganho HX711 | Canal A, ganho 128 | Canal A, ganho 128; o arquivo foi reescrito | `SERVICE` |
| `zero_calibrate_measurement` | Valor ADC bruto para carga zero | Obrigatório se a seção existir | Inteiro de 32 bits com sinal | Depende do hardware | Valor de reserva `-486050`; o arquivo foi reescrito | `SERVICE` |
| `weight_calibrate_measurement` | Valor ADC bruto com o peso de referência | Obrigatório se a seção existir | Inteiro de 32 bits com sinal | Depende do hardware | Valor de reserva `-498030`; o arquivo foi reescrito | `SERVICE` |
| `calibrate_weight` | Massa de referência de calibração | Obrigatório se a seção existir | Gramas; inteiro positivo; os limites não são verificados automaticamente | Depende do hardware | `500` g; o arquivo foi reescrito | `USER` |
| `start_weight` | Tara subtraída do resultado | Obrigatório se a seção existir | Gramas; `-100000` para `100000` é recomendado; os limites não são verificados automaticamente | Depende do hardware | `0` g; o arquivo foi reescrito | `USER` |
| `source_weight` | Filtro cujo resultado é usado como peso principal | Obrigatório se a seção existir | `1` — `immediate`; `2` — `stable`; `3` — `calibration` | A seção não é criada automaticamente | `1`; o arquivo é reescrito. Outros valores são tratados como `1` durante a operação | `SERVICE` |
| `normal_pecision` | Parâmetro de precisão do filtro rápido | Obrigatório se a seção existir | Número de ponto flutuante; limites não são verificados | A seção não é criada automaticamente | `0.5`; o arquivo foi reescrito | `SERVICE` |
| `normal_desired_deviation` | Desvio desejado do filtro rápido | Obrigatório se a seção existir | Número de ponto flutuante; limites não são verificados | A seção não é criada automaticamente | `10`; o arquivo foi reescrito | `SERVICE` |
| `stable_pecision` | Parâmetro de precisão do filtro estável | Obrigatório se a seção existir | Número de ponto flutuante; limites não são verificados | A seção não é criada automaticamente | `0.35`; o arquivo foi reescrito | `SERVICE` |
| `stable_desired_deviation` | Desvio desejado do filtro estável | Obrigatório se a seção existir | Número de ponto flutuante; limites não são verificados | A seção não é criada automaticamente | `5`; o arquivo foi reescrito | `SERVICE` |
| `calibrate_pecision` | Parâmetro de precisão do filtro de calibração | Obrigatório se a seção existir | Número de ponto flutuante; limites não são verificados | A seção não é criada automaticamente | `0.25`; o arquivo foi reescrito | `SERVICE` |
| `calibrate_desired_deviation` | Desvio desejado do filtro de calibração | Obrigatório se a seção existir | Número de ponto flutuante; limites não são verificados | A seção não é criada automaticamente | `3`; o arquivo foi reescrito | `SERVICE` |
| `median_window` | Tamanho da janela do filtro mediano | Obrigatório se a seção existir | `3`–`100`; valores fora do intervalo são substituídos | A seção não é criada automaticamente | `100`; o arquivo foi reescrito | `SERVICE` |

Os identificadores `normal_pecision`, `stable_pecision`e `calibrate_pecision` contém o erro histórico `pecision`, que não deve ser corrigido no XML.

`gain` é carregado a partir do arquivo, mas salvar sempre define o canal A com ganho 128. Não altere-o manualmente sem dados para o seu dispositivo específico.

## `thermometer`

Uma seção ausente permite a normalização do arquivo. O valor `sensors_count="0"` desativa a pesquisa de sensores DS18B20.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `pin_onewire` | Barramento GPIO de 1 fio | Opcional | GPIO para a placa específica | `4` | `4`; o arquivo foi reescrito | `SERVICE` |
| `sensors_count` | Número de sensores DS18B20 | Opcional | `0` desativa os sensores; inteiro positivo; limite superior não é verificado | `2` | `2`; o arquivo foi reescrito | `ADVANCED` |

## `schedule`

O `TimeSlot0`–`TimeSlot23` atributos definem a ação para a hora correspondente. Após 30 minutos, a ação para a próxima hora é selecionada; depois das 23 horas, `TimeSlot0` está selecionado.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `TimeSlot0`…`TimeSlot23` | Tipo de ação agendada por hora `0`–`23` | Todos os atributos são opcionais, mas pelo menos um slot com `2` é obrigatório | Inteiro de `0` para `5`; Veja abaixo | `5` por horas `0`–`20`; `1` para `21` e `22`; `2` para `23` | Um slot perdido torna-se `0`. Se não `2` permanece após a leitura, todo o agendamento é redefinido para o agendamento inicial | `ADVANCED` |

| Valor | Ação | Recomendação |
|---:|---|---|
| `0` | Nenhuma ação agendada | Pode ser usado para um slot vazio |
| `1` | Medição | Suportado |
| `2` | Transmissão através do canal primário | Obrigatório em pelo menos um slot |
| `3` | Reservado para transmissão via Wi-Fi | Não use |
| `4` | Reservado para transmissão através de BLE | Não use |
| `5` | Despertar de hora em hora para sincronização | Usado pela programação inicial |

Outros inteiros não são rejeitados, mas não possuem comportamento definido. Use apenas valores da tabela.

### Cronograma Inicial

```xml
<schedule
  TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
  TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
  TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
  TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
  TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
  TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
```

## `booster`

Esta seção define o intervalo para ativações adicionais para verificar parâmetros críticos. Se a seção estiver ausente, é utilizado um intervalo de hora em hora durante a operação; a ausência em si não desencadeia a reescrita.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `booster_time_sec` | Intervalo de verificação adicional | Opcional | `180`, `240`, `300`, `360`, `600`, `720`, `900`, `1200`, `1800`, ou `3600` é | `3600` é | `3600` é | `ADVANCED` |

Um valor abaixo `180` torna-se `180`; um valor acima `3600` torna-se `3600`. Outros valores dentro do intervalo são arredondados para o intervalo suportado mais próximo na tabela.

## `range_alarmer`

Esta seção é opcional. Se estiver ausente, o alarme de limite não será inicializado. Se `alarm="false"` ou o `alarm` atributo está ausente, os limites não são lidos e a tarefa de alarme em segundo plano não é iniciada.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `alarm` | Habilita alarmes de limite | Opcional | `true`, `false` | `false` | `false` | `USER` |
| `T1_min` | Limite inferior T1 | Opcional | Número de ponto flutuante, °C; limites físicos e ordem mín/máx não são verificados automaticamente | `-500` °C em um arquivo recém-criado | Com `alarm="true"`, não há limite inferior | `ADVANCED` |
| `T1_max` | Limite superior T1 | Opcional | Número de ponto flutuante, °C; limites físicos e ordem mín/máx não são verificados automaticamente | `500` °C em um arquivo recém-criado | Com `alarm="true"`, não há limite superior | `ADVANCED` |
| `T2_min` | Limite inferior T2 | Opcional | Número de ponto flutuante, °C; limites físicos e ordem mín/máx não são verificados automaticamente | `-500` °C em um arquivo recém-criado | Com `alarm="true"`, não há limite inferior | `ADVANCED` |
| `T2_max` | Limite superior T2 | Opcional | Número de ponto flutuante, °C; limites físicos e ordem mín/máx não são verificados automaticamente | `500` °C em um arquivo recém-criado | Com `alarm="true"`, não há limite superior | `ADVANCED` |
| `Humidity_min` | Limite inferior de umidade | Opcional | Número de ponto flutuante,%; limites físicos e ordem mín/máx não são verificados automaticamente | `-20` % em um arquivo recém-criado | Com `alarm="true"`, não há limite inferior | `ADVANCED` |
| `Humidity_max` | Limite superior de umidade | Opcional | Número de ponto flutuante,%; limites físicos e ordem mín/máx não são verificados automaticamente | `200` % em um arquivo recém-criado | Com `alarm="true"`, não há limite superior | `ADVANCED` |

Para cada fonte – T1, T2 ou umidade – um limite é suficiente. Se nenhum limite for especificado para uma fonte específica, ele não será adicionado à verificação. A ordem de `_min` e `_max` não é verificado automaticamente.

### Exemplo de alarme unilateral

Neste exemplo, T1 é monitorado apenas por cima, T2 apenas por baixo e a umidade não é monitorada:

```xml
<range_alarmer alarm="true" T1_max="45.0" T2_min="-10.0" />
```

A frequência geral de SMS e a confirmação de alarme PIR são configuradas por `alarm_sms_sec_interval`, `alarm_by_changes_count`e `alarm_by_long_state` em [`mset.xml`](settings-reference.md#options).

## Exemplo estrutural sem balança

Este arquivo usa a programação inicial, dois sensores de temperatura e alarmes de limite desabilitados. O `scales` está ausente, portanto nenhum objeto de balança é criado.

```xml
<settings>
  <hive hive_name="hive1" bus_number="0" main_device="true" />
  <booster booster_time_sec="3600" />
  <range_alarmer alarm="false"
                 T1_max="500" T1_min="-500"
                 T2_max="500" T2_min="-500"
                 Humidity_max="200" Humidity_min="-20" />
  <thermometer pin_onewire="4" sensors_count="2" />
  <schedule
    TimeSlot0="5" TimeSlot1="5" TimeSlot2="5" TimeSlot3="5"
    TimeSlot4="5" TimeSlot5="5" TimeSlot6="5" TimeSlot7="5"
    TimeSlot8="5" TimeSlot9="5" TimeSlot10="5" TimeSlot11="5"
    TimeSlot12="5" TimeSlot13="5" TimeSlot14="5" TimeSlot15="5"
    TimeSlot16="5" TimeSlot17="5" TimeSlot18="5" TimeSlot19="5"
    TimeSlot20="5" TimeSlot21="1" TimeSlot22="1" TimeSlot23="2" />
</settings>
```

## Seção completa de balanças

O exemplo estrutural a seguir usa valores de fallback e é fornecido apenas para referência de arquivamento. **Não instale-o em um dispositivo:** os valores e pinos de calibração devem vir de um backup desse dispositivo específico ou ser criados pelo procedimento de calibração padrão.

```xml
<scales pin_hc711_data="27" pin_hc711_clk="26" gain="0"
        zero_calibrate_measurement="-486050"
        weight_calibrate_measurement="-498030"
        calibrate_weight="500" start_weight="0" source_weight="1"
        normal_pecision="0.5" normal_desired_deviation="10"
        stable_pecision="0.35" stable_desired_deviation="5"
        calibrate_pecision="0.25" calibrate_desired_deviation="3"
        median_window="100" />
```

GPIO `27` e `26` são apenas um exemplo para um dispositivo e não são universais. Use valores do backup do seu dispositivo específico.
