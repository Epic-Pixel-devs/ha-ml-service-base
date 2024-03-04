# ha-ml-service-base


### Instalação e Configuração de Ambiente

* Fazer download Python 3.7
  [download here](https://www.python.org/downloads/) compatível com Tensorflow versão 2.11 https://www.tensorflow.org/install/ 
* Fazer download do gitbash: [download here](https://git-scm.com/)
* Fazer clone do projeto no
  github: [clone here](https://github.com/Epic-Pixel-devs/ha-ml-service-base): `git clone https://github.com/Epic-Pixel-devs/ha-ml-service-base`
* Entrar no diretório e criar ambiente: `cd ha-ml-service-base`
* Criar novo Ambiente Virtual: `python -m venv .venv`
* Fazer update do pip:
    * windows: `.venv\Script\Activate` e `pip install pip --upgrade`
      > obs: caso ocorra error de script no power shell deverá fazer
      a permissão. Rodar este comando como admin  
      `Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser`
    * Linux: `source .venv/bin/activate` e `pip install pip --upgrade`
* Fazer a instalação das dependências: `pip install -r requirements`
* Fazer a inclusão das variáveis de ambiente.
* Roder o projeto local: `flask run`

Crontab Syntax

```text 
*     *     *     *     *
-     -     -     -     -
|     |     |     |     |
|     |     |     |     +----- day of the week (0 - 6) (Sunday=0)
|     |     |     +------- month (1 - 12)
|     |     +--------- day of the month (1 - 31)
|     +----------- hour (0 - 23)
+------------- min (0 - 59)
```