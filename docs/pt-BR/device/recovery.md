# Restaurando a configuração

Esta página explica como substituir o cartão microSD com segurança, restaurar a configuração de um backup e verificar os arquivos XML após a inicialização do dispositivo.

!!! danger "Não remova o cartão microSD enquanto o dispositivo estiver ativo"
    O dispositivo não possui botão liga / desliga padrão. Antes de remover ou instalar o cartão microSD, espere até que o dispositivo entre no modo de suspensão. Primeiro, salve uma cópia completa do `/setting` diretório.

## Normalização Automática

- o arquivo principal está em `/setting/mset.xml`;
- se faltar o arquivo principal, o dispositivo pode criar uma configuração inicial;
- um arquivo de colmeia ausente ou incompleto pode ser salvo novamente usando valores de fallback do estado atual;
- um desaparecido `hive`, `thermometer`, ou `schedule` seção, bem como um existente incompleto `scales` seção, aciona a normalização do arquivo colmeia;
- um completamente desaparecido `scales` seção não é um erro: as balanças simplesmente não são criadas;
- erros estruturais no elemento XML raiz, o `apairy_set` seção, ou o `hiveN` atributo pode impedir que a configuração seja lida.

Criando uma inicial `mset.xml` não significa que todo parâmetro terá um valor universal. `UPLOAD_URL`, credenciais de FTP, pinos HX711 e alguns outros campos dependem da configuração do dispositivo ou da configuração individual.

!!! warning "É necessário um backup"
    Não confie na recuperação automática como seu único backup. Antes de substituir o cartão microSD, salve todo o `/setting` diretório se o cartão ainda puder ser lido.

## Substituindo o cartão microSD com segurança

1. Aguarde o dispositivo entrar no modo de suspensão.
2. Remova o cartão microSD e, se estiver legível, copie todo o seu conteúdo.
3. Prepare o cartão microSD de acordo com os requisitos da versão específica do hardware do dispositivo.
4. Restaure o `/setting` diretório de um backup verificado.
5. Se não existir nenhum backup, não use valores de calibração da balança de outro dispositivo. Primeiro restaure um mínimo [`mset.xml`](settings-reference.md#minimal-example)e, em seguida, crie o arquivo colmeia sem um `scales` seção ou execute o procedimento de calibração padrão.
6. Instale o cartão microSD enquanto o dispositivo estiver em suspensão e aguarde o próximo ciclo operacional.
7. Verifique a hora, rede, números GSM, sensores disponíveis, horário e peso.
8. Compare os arquivos XML normalizados com o backup: o dispositivo pode ter adicionado campos com valores substitutos ou seções reescritas.

## Se a configuração não puder ser lida

1. Verifique se o arquivo possui um `<settings>` elemento raiz.
2. Verifique os nomes exatos `apairy_set`, `synchronize`, `sefe_start_interval`e `pecision` nos três campos de filtro.
3. Certifique-se `hive_count` tem correspondência `hive1`…`hiveN` atributos.
4. Certifique-se de que cada referência `/setting/<hive>.xml` arquivo existe.
5. Não tente resolver o problema copiando `scales` de outro dispositivo. Remova temporariamente a seção da balança e verifique o restante da configuração.
6. Salve os arquivos XML e logs de serviço problemáticos para diagnóstico.

Para uma descrição completa dos campos, consulte o [`mset.xml`](settings-reference.md) e [`HIVE*.XML`](hive-settings-reference.md) referências.
