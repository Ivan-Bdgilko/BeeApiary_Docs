# `HIVE*.XML`: Configuración de la colmena

La configuración de la colmena se guarda en `/setting/<hive>.xml`. El `<hive>` El nombre base está especificado por el `hive1`, `hive2`y atributos posteriores en [`mset.xml`](settings-reference.md); el `.xml` La extensión se agrega automáticamente.

!!! danger "Valores que dependen del hardware"
    No copiar el `scales` sección desde otro dispositivo. Los pines de la placa y los valores de calibración dependen de la versión del hardware y del conjunto particular de sensores de peso. Los valores incorrectos pueden distorsionar las mediciones o hacer que no estén disponibles.

Ver el [reglas de edición segura](service-reference.md).

## Reescritura automática

Después de leer el archivo, el dispositivo podrá guardarlo nuevamente:

- se crea un archivo faltante o dañado a partir del estado actual disponible;
- desaparecido `hive`, `thermometer`, o `schedule` las secciones permiten la normalización;
- un atributo faltante en un existente `scales` o `thermometer` la sección se reemplaza con un valor alternativo y permite la normalización;
- completo `scales`, `booster`, y `range_alarmer` las secciones son opcionales;
- La normalización también escribe el `booster`, `range_alarmer`, `thermometer`, y `schedule` secciones incluso si algunas de ellas estuvieran ausentes en el archivo fuente.

## `hive`

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `hive_name` | Nombre interno de la colmena | Opcional | Cadena; se recomiendan hasta 8 caracteres ASCII por compatibilidad | Nombre de `mset.xml`, por ejemplo `hive1` | `hive_<індекс>`; el archivo está marcado para reescribir | `ADVANCED` |
| `bus_number` | Número de la colmena en el bus interno | Opcional | Número entero; los límites no se comprueban | índice de instancia, `0` por primera | Índice de instancia; el archivo está marcado para reescribir | `SERVICE` |
| `main_device` | Indica el dispositivo principal con sensores de hardware locales. | Opcional | `true`, `false` | `true` en un archivo recién creado | La instancia no se convierte en el dispositivo principal; la omisión por sí sola no permite reescribir | `SERVICE` |

La compatibilidad con dispositivos subordinados está obsoleta. el valor `main_device="false"` se acepta durante la carga, pero después de guardar, el atributo se vuelve `main_device="true"`. no usar `false` como una configuración estable.

## `scales`

Si la sección está totalmente ausente, no se crea el objeto de las balanzas y la medición del peso queda desactivada. Si la sección existe, cada campo ausente o incorrecto se sustituye por un valor de respaldo, tras lo cual se puede volver a escribir el archivo completo.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `pin_hc711_data` | GPIO de datos del HX711 | Obligatorio si la sección existe | GPIO para la placa particular | La sección no se crea automáticamente; dependiente del hardware | Pin para el tablero en particular; el archivo se reescribe | `SERVICE` |
| `pin_hc711_clk` | GPIO de reloj del HX711 | Obligatorio si la sección existe | GPIO para la placa particular | La sección no se crea automáticamente; dependiente del hardware | Pin para el tablero en particular; el archivo se reescribe | `SERVICE` |
| `gain` | Modo de ganancia HX711 | Obligatorio si la sección existe | Valor del modo de ganancia HX711 | Canal A, ganancia 128 | Canal A, gana 128; el archivo se reescribe | `SERVICE` |
| `zero_calibrate_measurement` | Valor ADC sin procesar para carga cero | Obligatorio si la sección existe | Entero de 32 bits con signo | Depende del hardware | Valor de reserva `-486050`; el archivo se reescribe | `SERVICE` |
| `weight_calibrate_measurement` | Valor ADC bruto con el peso de referencia | Obligatorio si la sección existe | Entero de 32 bits con signo | Depende del hardware | Valor de reserva `-498030`; el archivo se reescribe | `SERVICE` |
| `calibrate_weight` | Masa de referencia de calibración | Obligatorio si la sección existe | Gramos; entero positivo; los límites no se verifican automáticamente | Depende del hardware | `500` gramo; el archivo se reescribe | `USER` |
| `start_weight` | Tara restada del resultado | Obligatorio si la sección existe | Gramos; `-100000` a `100000` se recomienda; los límites no se verifican automáticamente | Depende del hardware | `0` gramo; el archivo se reescribe | `USER` |
| `source_weight` | Filtro cuyo resultado se utiliza como peso principal. | Obligatorio si la sección existe | `1` — `immediate`; `2` — `stable`; `3` — `calibration` | La sección no se crea automáticamente. | `1`; el archivo se reescribe. Otros valores se tratan como `1` durante la operación | `SERVICE` |
| `normal_pecision` | Parámetro de precisión del filtro rápido. | Obligatorio si la sección existe | Número de punto flotante; los límites no están controlados | La sección no se crea automáticamente. | `0.5`; el archivo se reescribe | `SERVICE` |
| `normal_desired_deviation` | Desviación deseada del filtro rápido | Obligatorio si la sección existe | Número de punto flotante; los límites no están controlados | La sección no se crea automáticamente. | `10`; el archivo se reescribe | `SERVICE` |
| `stable_pecision` | Parámetro de precisión del filtro estable. | Obligatorio si la sección existe | Número de punto flotante; los límites no están controlados | La sección no se crea automáticamente. | `0.35`; el archivo se reescribe | `SERVICE` |
| `stable_desired_deviation` | Desviación deseada del filtro estable | Obligatorio si la sección existe | Número de punto flotante; los límites no están controlados | La sección no se crea automáticamente. | `5`; el archivo se reescribe | `SERVICE` |
| `calibrate_pecision` | Parámetro de precisión del filtro de calibración. | Obligatorio si la sección existe | Número de punto flotante; los límites no están controlados | La sección no se crea automáticamente. | `0.25`; el archivo se reescribe | `SERVICE` |
| `calibrate_desired_deviation` | Desviación deseada del filtro de calibración | Obligatorio si la sección existe | Número de punto flotante; los límites no están controlados | La sección no se crea automáticamente. | `3`; el archivo se reescribe | `SERVICE` |
| `median_window` | Tamaño de ventana de filtro mediano | Obligatorio si la sección existe | `3`–`100`; los valores fuera de rango se reemplazan | La sección no se crea automáticamente. | `100`; el archivo se reescribe | `SERVICE` |

Los identificadores `normal_pecision`, `stable_pecision`, y `calibrate_pecision` contener el error histórico `pecision`, que no debe corregirse en el XML.

`gain` se carga desde el archivo, pero al guardarlo siempre se configura el canal A con ganancia 128. No lo cambie manualmente sin datos para su dispositivo en particular.

## `thermometer`

Una sección que falta permite la normalización de archivos. el valor `sensors_count="0"` desactiva el sondeo de los sensores DS18B20.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `pin_onewire` | Bus GPIO de 1 cable | Opcional | GPIO para la placa particular | `4` | `4`; el archivo se reescribe | `SERVICE` |
| `sensors_count` | Número de sensores DS18B20 | Opcional | `0` desactiva los sensores; entero positivo; el límite superior no está marcado | `2` | `2`; el archivo se reescribe | `ADVANCED` |

## `schedule`

El `TimeSlot0`–`TimeSlot23` Los atributos definen la acción para la hora correspondiente. Pasado el minuto 30, se selecciona la acción para la siguiente hora; después de la hora 23, `TimeSlot0` está seleccionado.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `TimeSlot0`…`TimeSlot23` | Tipo de acción programada por hora `0`–`23` | Todos los atributos son opcionales, pero al menos un espacio con `2` es requerido | Entero de `0` a `5`; vea abajo | `5` durante horas `0`–`20`; `1` para `21` y `22`; `2` para `23` | Una ranura faltante se convierte `0`. si no `2` permanece después de la lectura, todo el programa se restablece al programa inicial | `ADVANCED` |

| Valor | acción | Recomendación |
|---:|---|---|
| `0` | Ninguna acción programada | Se puede utilizar para una ranura vacía. |
| `1` | Medición | Apoyado |
| `2` | Transmisión por el canal primario. | Requerido en al menos una ranura |
| `3` | Reservado para transmisión a través de Wi-Fi | no usar |
| `4` | Reservado para transmisión a través de BLE | no usar |
| `5` | Despertador cada hora para sincronización | Utilizado por el horario inicial. |

Otros números enteros no se rechazan pero no tienen un comportamiento definido. Utilice sólo valores de la tabla.

### Horario inicial

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

Esta sección establece el intervalo para reactivaciones adicionales para verificar parámetros críticos. Si la sección está ausente, se utiliza un intervalo de una hora durante la operación; la ausencia en sí misma no desencadena la reescritura.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `booster_time_sec` | Intervalo de control adicional | Opcional | `180`, `240`, `300`, `360`, `600`, `720`, `900`, `1200`, `1800`, o `3600` s | `3600` s | `3600` s | `ADVANCED` |

Un valor por debajo `180` s se convierte `180`; un valor por encima `3600` s se convierte `3600`. Otros valores dentro del rango se redondean al intervalo admitido más cercano en la tabla.

## `range_alarmer`

Esta sección es opcional. Si está ausente, la alarma de umbral no se inicializa. si `alarm="false"` o el `alarm` El atributo está ausente, los límites no se leen y la tarea de alarma en segundo plano no se inicia.

| Campo | Función | Obligatoriedad | Valores permitidos / límites | Valor inicial | Si no se especifica | Nivel |
|---|---|---|---|---|---|---|
| `alarm` | Habilita alarmas de umbral | Opcional | `true`, `false` | `false` | `false` | `USER` |
| `T1_min` | Límite inferior T1 | Opcional | Número de coma flotante, °C; Los límites físicos y el orden mínimo/máximo no se verifican automáticamente. | `-500` °C en un archivo recién creado | con `alarm="true"`, no hay límite inferior | `ADVANCED` |
| `T1_max` | Límite superior T1 | Opcional | Número de coma flotante, °C; Los límites físicos y el orden mínimo/máximo no se verifican automáticamente. | `500` °C en un archivo recién creado | con `alarm="true"`, no hay límite superior | `ADVANCED` |
| `T2_min` | Límite inferior T2 | Opcional | Número de coma flotante, °C; Los límites físicos y el orden mínimo/máximo no se verifican automáticamente. | `-500` °C en un archivo recién creado | con `alarm="true"`, no hay límite inferior | `ADVANCED` |
| `T2_max` | Límite superior T2 | Opcional | Número de coma flotante, °C; Los límites físicos y el orden mínimo/máximo no se verifican automáticamente. | `500` °C en un archivo recién creado | con `alarm="true"`, no hay límite superior | `ADVANCED` |
| `Humidity_min` | Límite inferior de humedad | Opcional | Número de punto flotante, %; Los límites físicos y el orden mínimo/máximo no se verifican automáticamente. | `-20` % en un archivo recién creado | con `alarm="true"`, no hay límite inferior | `ADVANCED` |
| `Humidity_max` | Límite superior de humedad | Opcional | Número de punto flotante, %; Los límites físicos y el orden mínimo/máximo no se verifican automáticamente. | `200` % en un archivo recién creado | con `alarm="true"`, no hay límite superior | `ADVANCED` |

Para cada fuente (T1, T2 o humedad) un límite es suficiente. Si no se especifica ningún límite para una fuente en particular, no se agrega al cheque. el orden de `_min` y `_max` no se comprueba automáticamente.

### Ejemplo de alarma unilateral

En este ejemplo, T1 se controla sólo desde arriba, T2 sólo desde abajo y no se controla la humedad:

```xml
<range_alarmer alarm="true" T1_max="45.0" T2_min="-10.0" />
```

La frecuencia general de SMS y la confirmación de alarma PIR se configuran mediante `alarm_sms_sec_interval`, `alarm_by_changes_count`, y `alarm_by_long_state` en [`mset.xml`](settings-reference.md#options).

## Ejemplo estructural Sin báscula

Este archivo utiliza el programa inicial, dos sensores de temperatura y alarmas de umbral deshabilitadas. el `scales` La sección está ausente, por lo que no se crea ningún objeto de balanza.

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

## Sección Balanzas completas

El siguiente ejemplo estructural utiliza valores alternativos y se proporciona únicamente como referencia de archivo. **No lo instales en un dispositivo:** Los valores de calibración y los pines deben provenir de una copia de seguridad de ese dispositivo en particular o crearse mediante el procedimiento de calibración estándar.

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

GPIO `27` y `26` son sólo un ejemplo para un dispositivo y no son universales. Utilice valores de la copia de seguridad de su dispositivo en particular.
