# Por que o BeeApiary funciona assim

## Do BeeApiary Criadores

BeeApiary foi projetado como uma ferramenta independente que mantém os dados e as principais decisões sob o controle do apicultor. Esta página explica diversas opções de design e software que podem não ser imediatamente óbvias.

## Por que as capas são transparentes?

A tampa transparente permite ver quando o dispositivo está funcionando e se entrou condensação, insetos ou sujeira no gabinete. Isto facilita a inspeção sem abrir o gabinete desnecessariamente.

O projeto está aberto a comentários e sugestões: sua construção não esconde do proprietário o estado dos componentes principais.

## Por que não há armazenamento obrigatório no servidor?

O funcionamento central das balanças de colmeia e do aplicativo não depende de permanente BeeApiary armazenamento em um servidor externo. As medições são armazenadas no [cartão microSD do dispositivo](../system/data-storage.md) e localmente no telefone do usuário. O sistema não requer armazenamento centralizado da localização ou histórico de atividades do proprietário.

Um serviço de retransmissão opcional pode ser usado para [sincronização através da rede Wi-Fi do apiário](../system/local-wifi.md#apiary-wifi-routing). Ele transfere dados para o aplicativo, mas não é um armazenamento permanente e não é necessário para outros canais de comunicação.

## Por que o GSM usa SMS?

No campo ou durante a movimentação de um apiário, o SMS está frequentemente disponível onde o acesso à Internet móvel não é confiável. Um plano mínimo de SMS é suficiente e o aplicativo recebe dados sem uma assinatura de servidor separada.

Com o formato de mensagem apropriado, duas mensagens SMS por dia podem entregar os resultados de todas as medições horárias coletadas durante aquele dia. O aplicativo funciona diretamente no telefone do proprietário e, em uma configuração típica, pode lidar com até cinco dispositivos; este número pode ser aumentado se necessário.

Para obter detalhes, consulte [GSM e SMS](../system/gsm-and-sms.md).

## Por que as medições são feitas a cada hora?

Um histórico de hora em hora ajuda a revelar as partidas matinais das abelhas e os retornos noturnos, mudanças de peso enquanto o néctar seca e variações diárias de temperatura. Esses dados fornecem uma base para análises adicionais da força das colônias, das reservas alimentares e de outros processos dentro da colmeia.

## Por que as mensagens SMS não são enviadas a cada hora?

A transmissão frequente não melhora as medições em si, mas consome energia da bateria e crédito de comunicação. O envio de várias mensagens por dia transfere os dados acumulados por hora com muito mais eficiência.

Uma estimativa prática para duas mensagens SMS por dia é de pelo menos 160 dias de operação com uma única carga. Esta é uma orientação, não uma garantia: a vida útil da bateria depende da bateria, da configuração do dispositivo, da temperatura, da cobertura GSM e dos canais de transmissão habilitados.

Se um sensor de alarme estiver instalado, um evento de emergência ou uma tentativa de mover a colmeia pode acionar separadamente uma chamada e um SMS sem esperar pela programação regular.

## Por que a bateria não deve ser removida?

O dispositivo possui três níveis de proteção de bateria e entra automaticamente em um modo de economia profunda de energia quando a carga está baixa. A bateria não precisa ser removida para armazenamento, enquanto a polaridade incorreta durante a reinstalação pode danificar permanentemente os componentes eletrônicos.

Exceções e regras de armazenamento no inverno estão descritas em [Energia e carregamento](power.md) e [Uso e armazenamento no inverno](winter-use-and-storage.md).

## Por que as atualizações de firmware não são automáticas?

O proprietário decide quando atualizar o dispositivo e se os recursos de uma nova versão são necessários. Uma atualização controlada reduz o risco de mudanças inesperadas no comportamento de um sistema autônomo.

As balanças de colmeia podem operar sem um telefone como balanças independentes e um registrador de dados meteorológicos. O aplicativo Android amplia os recursos de visualização, diário do apiário e sincronização, mas não é necessário para medições. Procedimento: [Atualize o dispositivo](../guides/update-device.md).

## Por quanto tempo as medições são armazenadas?

O arquivo no cartão microSD não está limitado a um ano. O período de armazenamento depende da capacidade e estado do cartão; com um volume normal de medições, é suficiente para a vida útil esperada do dispositivo.

## Dois tipos de SMS e um horário flexível. Por que?

Existem muitas opiniões sobre quando, como e onde começar a fazer medições; para resolver isso, os usuários podem configurar livremente o formato do SMS e o horário de envio de acordo com suas preferências. No entanto, existem certas recomendações relativas ao número de mensagens por dia para economizar energia.
