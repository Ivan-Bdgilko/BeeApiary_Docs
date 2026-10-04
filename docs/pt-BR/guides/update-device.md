# Como atualizar o firmware das balanças BeeApiary

Antes de atualizar, selecione o firmware que corresponda à geração do dispositivo e ao idioma de interface necessário.

## Selecione a geração do firmware

| Dispositivo | Fonte de atualização | Status de desenvolvimento |
|---|---|---|
| Fabricado antes de agosto de 2026 | [Hive_Controller](https://github.com/Ivan-Bdgilko/Hive_Controller) | O desenvolvimento de recursos para a versão anterior não é mais compatível |
| Fabricado após agosto de 2026 | [Hive_Controller_Ble](https://github.com/Ivan-Bdgilko/Hive_Controller_Ble) | A nova versão continua recebendo atualizações e novas funcionalidades |

!!! danger "Migrando um dispositivo antigo para a nova versão"
    Qualquer dispositivo fabricado anteriormente pode ser migrado para a nova versão do software, mas isso requer atualização de fábrica. Atualmente não existe um patch simples para uma migração de autoatendimento, portanto o procedimento padrão nesta página não migra um dispositivo entre gerações.

## Selecione o idioma do firmware

Ambas as gerações fornecem construções multilíngues. O sufixo no nome da versão identifica o idioma:

| Sufixo | Idioma |
|---|---|
| `-de` | Alemão |
| `-en` | Inglês |
| `-es` | Espanhol |
| `-fr` | Francês |
| `-pl` | Polonês |
| `-uk` | Ucraniano |

Selecione o idioma baixando e atualizando o arquivo correspondente. As compilações de idiomas estão disponíveis publicamente nos repositórios listados acima e mais idiomas podem ser adicionados posteriormente, se necessário.

## Atualize o dispositivo usando microSD

1. Aguarde até que o dispositivo entre no modo de suspensão e remova o cartão microSD.
2. Crie o `/fm` diretório na raiz do cartão, se ainda não existir.
3. Coloque o `Apiary.bin` atualizar arquivo em `/fm`.
4. Reinsira o cartão microSD no dispositivo.
5. [Ative ou reinicie o dispositivo](../device/installation.md#activation-reset) com a chave magnética.
6. Aguarde uma mensagem SMS normal contendo medições; a atualização geralmente leva até dois minutos.
7. Na parte inferior da página inicial da interface da web, verifique a versão do firmware, o sufixo do idioma, a data e hora da compilação e o número exclusivo do dispositivo.

![Versão do firmware, sufixo do idioma, tempo de compilação e ID exclusivo na interface web do dispositivo](../../assets/common/guides/update-device/device-version-build-time-and-id.png){ .doc-screenshot }

A string da versão completa inclui o sufixo de localização, por exemplo `-uk`. Compare-o com a versão de atualização correspondente no repositório para a geração do seu dispositivo. A mesma página também mostra a data e hora da construção e o identificador exclusivo do dispositivo.

!!! warning "Verifique o arquivo antes de atualizar"
    Certifique-se `Apiary.bin` destina-se à geração do seu dispositivo e ao idioma necessário. Os métodos de atualização de serviço por FTP ou servidor estão fora do escopo deste procedimento.
