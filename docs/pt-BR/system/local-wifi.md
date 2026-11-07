---
title: "Balanças para colmeias com Wi-Fi — conexão direta e pela rede"
description: "Conectar BeeApiary balanças de colmeia via Wi-Fi: ponto de acesso direto ao seu telefone e transmissão remota pela rede do apiário."
---

# Balanças para colmeias com Wi-Fi — conexão direta e pela rede { #wi-fi- }

BeeApiary Balanças de colmeia com Wi-Fi suportam duas formas de receber dados: uma conexão telefônica direta ao ponto de acesso (AP) do dispositivo e transmissão através da rede Wi-Fi do apiário (STA). O primeiro método funciona próximo às balanças; o segundo fornece acesso remoto a dados quando a conectividade com a Internet está disponível.

## Conexão direta ao dispositivo { #direct-access-point }

Após a ativação com a chave magnética, o dispositivo cria temporariamente um ponto de acesso local. Geralmente fica disponível por cerca de um minuto, mas esse intervalo pode ser alterado nas configurações.

Configurações padrão:

```text
SSID: apiary_net
Senha: apiary_wifi
Interface web: http://192.168.4.1
```

Através da conexão local, você pode:

- permitir que o aplicativo recupere o arquivo de medição;
- abra a interface web;
- configurar o telefone do proprietário e o horário;
- veja o nível de carga e a versão do firmware;
- use FTP para acessar arquivos no cartão microSD.

Depois que o telefone se conectar a `apiary_net`, o aplicativo encontra o dispositivo e exibe o prompt **"Dispositivo próximo. Recuperar arquivo?"**. Os dados são baixados somente após o usuário confirmar a solicitação.

!!! warning "Alterar a senha"
    A senha padrão é conhecida publicamente. Após a primeira verificação, defina sua própria senha de até 32 caracteres.

Procedimentos detalhados:

- [Conecte-se ao ponto de acesso do dispositivo](../guides/configure-local-wifi.md);
- [baixe o arquivo para o aplicativo](../guides/download-archive.md);
- [visualizar configurações adicionais do dispositivo](../device/additional-settings.md).

## Roteamento pela rede Wi-Fi do Apiário { #apiary-wifi-routing }

O dispositivo pode se conectar a uma rede Wi-Fi existente no apiário e enviar dados automaticamente pela Internet para o aplicativo do proprietário. O telefone pode estar em qualquer lugar com acesso à Internet.

Este método não requer um cartão SIM separado em cada dispositivo, mas uma rede Wi-Fi configurada com acesso à Internet deve estar disponível perto do dispositivo.

### Como funciona a configuração

Registre um dispositivo já conhecido pelo aplicativo: o serviço cria identificadores e chaves. Depois transfira as configurações da rede do apiário do telefone pelo ponto de acesso `apiary_net` do dispositivo.

Após uma reinicialização com a chave magnética ou durante o próximo ciclo horário programado, o dispositivo utiliza a rede configurada para transmissão automática. O telefone não precisa mais estar por perto.

### Requisitos

- o dispositivo já foi adicionado ao aplicativo;
- o aplicativo recebeu seus dados pelo menos uma vez por SMS ou download direto de arquivo;
- o telefone tem acesso à Internet durante o registro;
- uma rede Wi-Fi com acesso à Internet está disponível próxima ao dispositivo;
- o usuário sabe o nome e a senha dessa rede.

O serviço de trânsito não é armazenamento permanente: os dados permanecem na balança e no telefone. O serviço pode ficar instável ou passar a ser pago; a compatibilidade e outras condições estão no guia.

Para o procedimento passo a passo, consulte [Configurar a sincronização através da rede Wi-Fi do apiário](../guides/configure-wifi-sync.md).
