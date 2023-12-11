---
weight: 100
title: "Access Google Sheets API through Python"
description: "Access Google sheets through python"
icon: "article"
date: "2023-12-11T18:27:51+01:00"
lastmod: "2023-12-11T18:27:51+01:00"
draft: false
toc: true
---

[En este tutorial](https://hackernoon.com/how-to-use-the-google-sheets-api-with-python)
la parte de crear la cuenta y acceder a la api funciona perfecto, pero las librerias que utilizan no van en python2.7

## Resumen 

El abstracto de todo es que este sistema funciona creando un usuario dentro de un proyecto de Google Cloud con acceso a multiples APIs. Para acceder a la hoja que queramos solamente es necesario compartir la hoja a ese usuario y ya tendriamos acceso desde codigo

## Configuración

### Step 1 - Crear un proyecto de Google Cloud

Hay un limite de 12 proyectos (Pendiente investigar limite de llamadas de la api, y toda esa movida)

Por lo que he visto y probado, el proyecto engloba el acceso a todas las herramientas de la api, este tutorial te crea un usuario con acceso a dicha api, pero las hojas de calculo no tienen por qué estar dentro de eso proyecto. He podido acceder a hojas ya creadas de calculo que utilizamos para blippi.

1. Acceder a [Google Cloud Console](https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fconsole.cloud.google.com%2F&flowEntry=ServiceLogin&flowName=GlifWebSignIn&followup=https%3A%2F%2Fconsole.cloud.google.com%2F&ifkv=ASKXGp3nvNCXU8VjjvZRE1UAG2XFpeWSCg-ig7uRlommmZOoD8dAEoJBwJ-rsjW6SMhwYldEeUdWfQ&osid=1&passive=1209600&ref=hackernoon.com&service=cloudconsole&dsh=S1711400996%3A1700570631773078&theme=glif) e iniciar sesion con una cuenta cualquiera.

1. Click on the main menu (hamburger) icon in the upper-left corner of the screen and select IAM & Admin > Create a Project from the drop-down menu.

1. Abrir el panel lateral izquierdo (Menu hamburguesa) y abrir el menu `IAM y administracion`

1. Introducir un nombre para el nuevo proyecto (El Project ID se crea en base al nombre, se puede editar, pero una vez creado el proyecto deja de ser modificable )

    1. Optionally, enter a location for the project. The location specifies the organization or folder to which the project will belong. As a new user, the default value of this field may display No organization and does not need to be changed. If you used a Google account that is managed, by your employer for example, when logging in, the Location field may display a different value.

1. Crear el nuevo proyecto y nos redirige al dashboard principal

### Step 2 - Enable the Google Sheets API

Los pasos siguientes indican como activar los API

1. En el panel lateral izquierdo, navegar a `APIs & Services` > `Library`.
1. En la pagina `Library`, buscar la seccion de Google Workspace y seleccionar `Google Sheets API`

1. Habilitar Google Sheets API.

Listo, esto se hace a nivel de proyecto de Google Cloud.

### Step 3a - Create a New Service Account

1. From the Dashboard page, click on the main menu icon in the upper-left corner again and select `APIs & Services` > `Credentials`.

1. On the Credentials page, click on Manage Service Accounts under Service Accounts.

1. You will be directed to the Service Accounts page where you need to click on Create Service Account.

1. Enter a new name for the service account. You can choose any name that you would like. Notice that as you enter your chosen service account name, an associated Service account ID will be automatically generated in the Service account ID field. Additionally, an e-mail address matching the service account ID will also be automatically generated. For example, if you entered some new service account in the name field, you might see a strange looking e-mail address ending in .iam.gserviceaccount.com like some-new-service-account@young-home-460928.iam.gserviceaccount.com as the service account e-mail. Copy this e-mail address since you will use it later when connecting a Python application to a Google Sheets spreadsheet via the Google Sheets API.

1. Once you have entered a name for the service account, click on Create And Continue.

1. Click on the Select a role dropdown menu from the Grant this service account access to project section. Look for the Basic option on the left side of the menu and hover over it. Then, click on Editor from the right-side of the menu. The Editor role will allow a Python application using this service account to read and write to a Google Sheets spreadsheet that it is interacting with via the Google Sheets API.

1. Click on Done to create the new service account.
You will be redirected back to the Service Accounts page.

### Step 3b - Create a New Key for the Service Account

1. From the Service Accounts page, click on the options menu icon (i.e. the icon with three vertical dots) under the Actions label for the new service account. When the menu opens, click on Manage Keys.

1. On the Keys page, click on Add Key and then select Create new key.

1. The key format should already be set to JSON when the Create private key modal opens. Click on Create. A new private key will be generated and a JSON file download with the new key should automatically start. Note the location of the JSON file with the private key value as it will be needed later when connecting to the Google Sheets API from a Python application.


### Instalar librerias propias de google

#### Python2

Para python2, que funcionara, encontré `gspread` que se instala directamente desde pip

Te dicen que la api de google (google-cloud, o el paquete google-api-python-client) funciona, pero no consegui hacerlo funcionar con ninguna de las dos.

##### OPCIONES DE INSTALADO


```bash
pip install gspread
```

```bash
python2-pip install gspread
```

```bash
pip2 install gspread
```

```bash
python -m pip install gspread
```

#### Python3

En python3 podemos tambien utilizar `gspread`.

Sin embargo, la libreria de google si que funciona correctamente, dandonos acceso a cualquier API dentro de google, no solo google sheets


###### [Pagina quickstart Python & Google Sheets API](https://developers.google.com/sheets/api/quickstart/python?hl=es-419)

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```