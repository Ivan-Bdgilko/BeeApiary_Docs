# `mset.xml`: Configurações do dispositivo

A configuração principal é armazenada em `/setting/mset.xml` no cartão microSD e tem um `<settings>` elemento raiz.

!!! warning "O arquivo atual não é uma lista de valores de fábrica"
    Os valores no XML de um determinado dispositivo podem ter sido alterados pelo usuário, pela interface da web ou automaticamente. Por exemplo, `sefe_start_interval="60000"` e `alarm_sms_sec_interval="10"` não são valores iniciais: uma nova configuração usa `120000` milissegundos e `180` respectivamente.

Veja também o [regras de edição segura](service-reference.md). Não mude `SERVICE` parâmetros sem backup e uma compreensão de seu efeito no dispositivo.

## `net_settings`

Esta seção armazena parâmetros para o ponto de acesso do dispositivo, conexão a uma rede Wi-Fi externa, transmissão de dados e FTP. Um `SSID`/`PASSWORD` ou `SSID_STA`/`PASSWORD_STA` pair é aplicado somente quando ambos os valores estão presentes e não vazios.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `SSID` | Nome do ponto de acesso local do dispositivo | Condicionalmente exigido com `PASSWORD` | String; até 32 caracteres | `apiary_net` | O novo par de pontos de acesso não é aplicado | `USER` |
| `PASSWORD` | Senha do ponto de acesso local | Condicionalmente exigido com `SSID` | String; até 32 caracteres | `apiary_wifi` | O novo par de pontos de acesso não é aplicado | `USER` |
| `SSID_STA` | SSID da rede Wi-Fi externa | Opcional | String não vazia; comprimento máximo não especificado | `-` | Novos parâmetros STA não são aplicados | `ADVANCED` |
| `PASSWORD_STA` | Senha da rede Wi-Fi externa | Condicionalmente exigido com `SSID_STA` | String; comprimento máximo não especificado | `-` | Novos parâmetros STA não são aplicados | `ADVANCED` |
| `STA_KEY` | Chave de autenticação usada durante a transmissão | Opcional | String; o formato depende do método de autenticação | `-` | O parâmetro Wi-Fi não é alterado | `SERVICE` |
| `UPLOAD_URL` | Endereço do receptor de dados Wi-Fi | Opcional | URL; o comprimento máximo não é especificado | Depende da configuração do dispositivo | Defina para um único espaço; a transmissão não está efetivamente configurada | `SERVICE` |
| `wifi_sync` | Permite a sincronização através de uma rede Wi-Fi externa | Opcional | `true`, `false` | `false` | `false` | `ADVANCED` |
| `FTP_USER` | Nome de usuário para FTP local | Opcional como parte de um par | String; até 32 caracteres | Depende da configuração do dispositivo | Se algum dos campos FTP estiver faltando, as configurações iniciais de FTP serão usadas | `ADVANCED` |
| `FTP_PASSWORD` | Senha para FTP local | Opcional como parte de um par | String; até 32 caracteres | Depende da configuração do dispositivo | Se algum dos campos FTP estiver faltando, as configurações iniciais de FTP serão usadas | `ADVANCED` |

!!! note "O `-` valor"
    Para `SSID_STA`, `PASSWORD_STA`e `STA_KEY`, o hífen é um valor inicial literal. Ela é processada como uma sequência não vazia, portanto, não a utilize como uma indicação confiável de que uma configuração “não está configurada”.

Alterar a senha inicial `apiary_wifi` após a primeira verificação do dispositivo.

## `apairy_set`

O nome da seção contém um erro histórico e deve permanecer `apairy_set`. Esta seção é necessária para criar a lista de colmeias.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `hive_count` | Número de arquivos de configuração da colmeia | Campo opcional em uma seção obrigatória | Inteiro; `1` ou mais é recomendado; os limites não são verificados automaticamente | `1` | `1` | `ADVANCED` |
| `hive1`…`hiveN` | Nomes básicos de arquivos colmeia sem `.xml` | Obrigatório para cada número até `hive_count` | String; recomenda-se até 8 caracteres ASCII para compatibilidade | `hive1` | Erro de leitura de atributo; a colmeia correspondente não é criada | `SERVICE` |

O caminho tem a forma `/setting/<значення>.xml`. O nome usa um buffer interno de 24 bytes, portanto, não use nomes longos ou separadores de caminho.

## `GSM`

Esta seção descreve dois destinatários. Se a seção estiver ausente, a estrutura GSM será apagada. A seção em si deve, portanto, ser considerada necessária mesmo ao operar sem cartão SIM.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `sms_format1` | Formato SMS para `number1` | Opcional | `1` - texto; `2` — formato de aplicativo compacto | `2` | `2` | `USER` |
| `sms_format2` | Formato SMS para `number2` | Opcional | `1` - texto; `2` — formato de aplicativo compacto | `2` | `2` | `USER` |
| `number1` | Número do destinatário principal | Opcional | Formato internacional; buffer interno de 15 bytes | String vazia | Nenhum destinatário está configurado no primeiro carregamento | `USER` |
| `number2` | Número de destinatário adicional | Opcional | Formato internacional; buffer interno de 15 bytes | String vazia | Nenhum destinatário está configurado no primeiro carregamento | `USER` |
| `sms_wait_to_send_sec` | É hora de esperar antes de enviar um SMS em uma rede fraca | Opcional | Número inteiro de segundos; sem limites fixos | `50` é | `50` é | `ADVANCED` |
| `alarm_call_wait_sec` | Intervalo entre repetidas tentativas de chamada de alarme | Opcional | Número inteiro de segundos; sem limites fixos | `80` é | `80` é | `ADVANCED` |

Especifique um número vazio como `number1=""` ou `number2=""`. Não inclua números de telefone reais em exemplos publicados.

## `NTP`

Esta seção pertence à mesma estrutura interna do GSM. Se `NTP` estiver completamente ausente, os parâmetros GSM que acabaram de ser lidos também serão redefinidos. A seção deve, portanto, permanecer presente mesmo quando a sincronização estiver desabilitada.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `synchronize` | Sincronização automática de horário através de um mecanismo de rede disponível | Campo opcional em uma seção obrigatória | `true`, `false` | `false` | `false` | `USER` |
| `time_zone` | Deslocamento de fuso horário especificado em horas inteiras no XML | Opcional | Inteiro; `-11` para `12` é recomendado; os limites não são verificados automaticamente | `2` | `3` | `ADVANCED` |
| `ntp1` | Servidor de horário principal | Opcional | Nome do host; buffer interno de até 30 bytes | `0.europe.pool.ntp.org` | Vazio na primeira carga | `ADVANCED` |
| `ntp2` | Servidor de horário secundário | Opcional | Nome do host; buffer interno de até 30 bytes | `1.europe.pool.ntp.org` | Vazio na primeira carga | `ADVANCED` |
| `ntp3` | Servidor de terceira vez | Opcional | Nome do host; buffer interno de até 30 bytes | `2.europe.pool.ntp.org` | Vazio na primeira carga | `ADVANCED` |

`time_zone` tem valores diferentes nos dois casos: um novo arquivo recebe `2`, enquanto um atributo ausente resulta em `3`. Considere essa diferença antes de alterar a configuração inicial.

A ortografia `synсhronize` contém a letra cirílica `с` e não é reconhecido. Use apenas `synchronize`.

## `options`

Atributos individuais são opcionais e possuem valores substitutos. **Não remova a seção inteira:** se estiver ausente, os parâmetros da seção são zerados ao invés de receberem os valores iniciais mostrados abaixo.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `meteo` | Indica a presença de um sensor de pressão e umidade | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `pir_sensor` | Indica a presença de um sensor de movimento PIR | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `temperature_twist` | Troca os valores lógicos T1 e T2 | Opcional | `true`, `false` | `false` | `false` | `ADVANCED` |
| `oled` | Indica a presença de um display OLED | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `oled_invert` | Inverte a imagem OLED | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `sefe_start_interval` | Duração da janela ativa após inicialização | Opcional | Milissegundos; os limites não são verificados automaticamente | `120000` milissegundos | `120000` milissegundos | `SERVICE` |
| `alarm_sms_sec_interval` | Intervalo mínimo entre mensagens SMS de alarme | Opcional | Número inteiro não assinado de segundos | `180` é | `180` é | `ADVANCED` |
| `alarm_by_changes_count` | Número de alterações de estado PIR necessárias para confirmar um alarme | Opcional | Inteiro não assinado; o valor prático depende da colocação | `3` | `3` | `ADVANCED` |
| `alarm_by_long_state` | Duração de um estado PIR ativo necessário para um alarme | Opcional | Número inteiro não assinado de segundos | `10` é | `10` é | `ADVANCED` |
| `time_ms_compensate` | Compensação diária da taxa de relógio | Opcional | Número assinado de milissegundos de 32 bits | `0` milissegundos | `0` milissegundos | `SERVICE` |
| `sync_time_sec` | Carimbo de data/hora do serviço para sincronização manual | Opcional | Número de segundos assinados de 64 bits | `0` | `0` | `SERVICE` |

`sefe_start_interval` é o nome exato do campo histórico. Seu valor inicial é `120000` milissegundos; o intervalo não é verificado automaticamente, portanto, reduzi-lo arbitrariamente é perigoso.

Os sinalizadores de hardware alterados através da interface web são salvos imediatamente, mas a configuração operacional os aplica após as configurações serem lidas novamente.

## `BLE`

A seção inteira é opcional para compatibilidade com arquivos mais antigos. Se estiver ausente, o BLE é desabilitado e os valores atuais e intervalos padrão são usados.

| Campo | Função | Obrigatoriedade | Valores permitidos / limites | Valor inicial | Se não especificado | Nível |
|---|---|---|---|---|---|---|
| `ble_enable` | Habilita BLE | Opcional | `true`, `false` | `false` | `false`; um valor inválido também desativa o BLE | `USER` |
| `static_values` | Seleciona valores estáticos em vez de valores atuais | Opcional | `true`, `false` | `false` | `false` | `SERVICE` |
| `update_time_sec` | Intervalo de atualização de dados BLE | Opcional | `3`–`60` é; valores mais baixos são normalizados para `3`, valores mais altos para `60` | `30` é | `30` é | `ADVANCED` |
| `advertising_time_sec` | Duração da publicidade BLE | Opcional | `0` ou `10`–`60` é; valores de `1` para `9` são normalizados para `0`, valores acima `60` para `60` | `20` é | `20` é | `ADVANCED` |

Para `static_values`, apenas a seleção de valores estáticos em vez de valores atuais é descrita; nenhum outro efeito do parâmetro é definido.

## Exemplo Mínimo { #minimal-example }

Este exemplo deixa STA, FTP e BLE com seus valores iniciais. Um vazio, mas presente `<options />` seção ativa o valor substituto de cada atributo em vez de limpar toda a estrutura.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options />
</settings>
```

## Exemplo completo de higienização { #full-example }

Os valores `SITE_WIFI`, `WIFI_PASSWORD`, `DEVICE_KEY`, `FTP_USER`, `FTP_PASSWORD`e o URL são espaços reservados, e não dados de um dispositivo operacional.

```xml
<settings>
  <net_settings SSID="apiary_net" PASSWORD="apiary_wifi"
                SSID_STA="SITE_WIFI" PASSWORD_STA="WIFI_PASSWORD"
                STA_KEY="DEVICE_KEY"
                UPLOAD_URL="https://example.invalid/beeapiary"
                wifi_sync="false"
                FTP_USER="FTP_USER" FTP_PASSWORD="FTP_PASSWORD" />
  <apairy_set hive_count="1" hive1="hive1" />
  <GSM sms_format1="2" sms_format2="2"
       number1="+380XXXXXXXXX" number2=""
       sms_wait_to_send_sec="50" alarm_call_wait_sec="80" />
  <NTP synchronize="false" time_zone="2"
       ntp1="0.europe.pool.ntp.org"
       ntp2="1.europe.pool.ntp.org"
       ntp3="2.europe.pool.ntp.org" />
  <options meteo="false" pir_sensor="false"
           temperature_twist="false" oled="false" oled_invert="false"
           sefe_start_interval="120000"
           alarm_sms_sec_interval="180"
           alarm_by_changes_count="3" alarm_by_long_state="10"
           time_ms_compensate="0" sync_time_sec="0" />
  <BLE ble_enable="false" static_values="false"
       update_time_sec="30" advertising_time_sec="20" />
</settings>
```
