# Documentação de serviço

Esta seção é um arquivo de configuração técnica para o BeeApiary balanças de colmeia. Destina-se a técnicos de serviço e usuários experientes que precisam restaurar ou inspecionar arquivos XML manualmente.

Os valores iniciais de alguns parâmetros de hardware e rede dependem da configuração do dispositivo específico.

!!! danger "Edição manual"
    Pinos de hardware, valores de calibração ou intervalos de manutenção incorretos podem interromper as medições ou a operação do dispositivo. Use a interface da web para alterações comuns. Sempre crie um backup do `/setting` diretório antes de editar os arquivos manualmente.

## Procedimento Seguro

1. Aguarde até que o dispositivo entre no modo de suspensão. O dispositivo não possui botão liga / desliga padrão: durante a operação, ele está ativo ou em hibernação.
2. Remova o cartão microSD e salve uma cópia completa do `/setting` diretório.
3. Edite o XML em um editor de texto sem alterar nomes de seções ou atributos.
4. Certifique-se de que o XML tenha um `<settings>` elemento raiz e que todas as aspas e tags de fechamento estão presentes.
5. Reinsira o cartão microSD enquanto o dispositivo estiver em suspensão. As configurações atualizadas serão aplicadas na próxima vez que a configuração for carregada normalmente; algumas alterações feitas por meio da interface da web também entram em vigor somente após a reinicialização.
6. Verifique as medições, a comunicação e o registro de serviço. Mantenha o backup até que a verificação seja concluída.

Ao salvar, o dispositivo pode normalizar o arquivo: adicionar seções ou atributos ausentes, substituir valores substitutos e reescrever a ordem dos elementos.

## Arquivos

- [`/setting/mset.xml`](settings-reference.md) — rede, GSM, hora, opções de hardware, alarmes gerais e BLE.
- [`/setting/<hive>.xml`](hive-settings-reference.md) — sensores para uma colmeia específica, peso, programação, frequência de verificação e alarmes de limite.
- [Restaurando a configuração](recovery.md) — substituição segura de microSD, restauração de um backup e verificação XML.

O nome do arquivo da colmeia é especificado pelo `hive1`, `hive2`e atributos subsequentes sem extensão. O `.xml` extensão é adicionada automaticamente.

## Níveis de acesso

| Etiqueta | Significado |
|---|---|
| `USER` | O valor pode ser alterado através da interface padrão. |
| `ADVANCED` | É necessária uma compreensão de seu efeito na comunicação ou na lógica operacional. |
| `SERVICE` | Alterações manuais podem tornar o dispositivo inoperante ou distorcer os dados. |

Nas tabelas, `—` significa que os limites não se aplicam ao campo. **Valor inicial** é o valor em uma configuração recém-criada, não no XML de um dispositivo específico. **Se não especificado** descreve o valor usado quando o atributo está ausente, que pode diferir do valor inicial.

## Nomes históricos

Os identificadores XML exatos não são corrigidos mesmo quando contêm erros: `apairy_set`, `sefe_start_interval`, `normal_pecision`e `calibrate_pecision` deve permanecer exatamente como está escrito. A ortografia `synсhronize` com a letra cirílica `с` está incorreto; usar `synchronize`.
