# Por qué BeeApiary funciona así

## Desde el BeeApiary Creadores

BeeApiary fue diseñado como una herramienta autónoma que mantiene los datos y las decisiones clave bajo el control del apicultor. Esta página explica varias opciones de diseño y software que pueden no ser inmediatamente obvias.

## ¿Por qué las cubiertas son transparentes?

A través de la cubierta transparente se puede ver si el dispositivo está en funcionamiento y si ha entrado condensación, insectos o suciedad en la carcasa. Esto facilita la inspección sin abrir el recinto innecesariamente.

El proyecto está abierto a comentarios y sugerencias: su construcción no oculta al propietario el estado de los componentes principales.

## ¿Por qué no existe un almacenamiento obligatorio en el servidor?

El funcionamiento principal de la báscula para colmenas y de la aplicación no depende de condiciones permanentes. BeeApiary almacenamiento en un servidor externo. Las mediciones se almacenan en el [tarjeta microSD del dispositivo](../system/data-storage.md) y localmente en el teléfono del usuario. El sistema no requiere almacenamiento centralizado de la ubicación del propietario o del historial de actividad.

Se puede utilizar un servicio de retransmisión opcional para [sincronización a través de la red wifi del apiario](../system/local-wifi.md#apiary-wifi-routing). Transfiere datos a la aplicación, pero no es un almacenamiento permanente y no es necesario para los otros canales de comunicación.

## ¿Por qué GSM utiliza SMS?

En el campo o mientras se mueve un colmenar, los SMS suelen estar disponibles cuando el acceso a Internet móvil no es confiable. Un plan mínimo de SMS es suficiente y la aplicación recibe datos sin una suscripción de servidor separada.

Con el formato de mensaje adecuado, dos mensajes SMS por día pueden entregar los resultados de todas las mediciones horarias recopiladas durante ese día. La aplicación funciona directamente en el teléfono del propietario y, en una configuración típica, puede manejar hasta cinco dispositivos; este número se puede aumentar si es necesario.

Para más detalles, consulte [GSM y SMS](../system/gsm-and-sms.md).

## ¿Por qué se toman medidas cada hora?

Un historial horario ayuda a revelar las salidas de las abejas por la mañana y los regresos por la noche, los cambios de peso mientras se seca el néctar y las variaciones diarias de temperatura. Estos datos proporcionan una base para análisis adicionales de la fuerza de la colonia, las reservas de alimentos y otros procesos dentro de la colmena.

## ¿Por qué no se envían mensajes SMS cada hora?

La transmisión frecuente no mejora las mediciones en sí, pero consume energía de la batería y crédito de comunicación. Enviar varios mensajes por día transfiere los datos horarios acumulados de manera mucho más eficiente.

Una estimación práctica para dos mensajes SMS por día es al menos 160 días de funcionamiento con una sola carga. Esto es una guía, no una garantía: la duración de la batería depende de la batería, la configuración del dispositivo, la temperatura, la cobertura GSM y los canales de transmisión habilitados.

Si se instala un sensor de alarma, un evento de emergencia o un intento de mover la colmena pueden activar por separado una llamada y un SMS sin esperar el horario habitual.

## ¿Por qué no se debe quitar la batería?

El dispositivo tiene tres niveles de protección de la batería y entra automáticamente en un modo de ahorro de energía profundo cuando la carga es baja. No es necesario retirar la batería para guardarla, mientras que una polaridad incorrecta durante la reinstalación puede dañar permanentemente los componentes electrónicos.

Las excepciones y reglas de almacenamiento en invierno se describen en [Energía y carga](power.md) y [Uso y almacenamiento en invierno](winter-use-and-storage.md).

## ¿Por qué las actualizaciones de firmware no son automáticas?

El propietario decide cuándo actualizar el dispositivo y si se necesitan las funciones de una nueva versión. Una actualización controlada reduce el riesgo de cambios inesperados en el comportamiento de un sistema autónomo.

La balanza para colmenas puede funcionar sin teléfono como balanza autónoma y registrador de datos meteorológicos. La aplicación de Android amplía las funciones de visualización, diario del apiario y sincronización, pero no es necesaria para las mediciones. Procedimiento: [Actualizar el dispositivo](../guides/update-device.md).

## ¿Cuánto tiempo se almacenan las mediciones?

El archivo en la tarjeta microSD no está limitado a un año. El período de almacenamiento depende de la capacidad y el estado de la tarjeta; con un volumen de mediciones normal, es suficiente para la vida útil esperada del dispositivo.

## Dos tipos de SMS y un horario flexible. ¿Por qué?

Hay muchas opiniones sobre cuándo, cómo y dónde empezar a tomar mediciones; Para solucionar este problema, los usuarios pueden configurar libremente el formato de SMS y la hora de envío según sus preferencias. Sin embargo, existen ciertas recomendaciones en cuanto a la cantidad de mensajes por día para poder conservar energía.
