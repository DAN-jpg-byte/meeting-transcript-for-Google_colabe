# User Guide · googlecolab/colab-vscode Wiki

- Source: https://github.com/googlecolab/colab-vscode/wiki/User-Guide
- Saved: 2026-04-19T09:21:45.896Z

---

# User Guide

[Jump to bottom](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#wiki-pages-box)

Jack Yang edited this pageApr 9, 2026·[17 revisions](https://github.com/googlecolab/colab-vscode/wiki/User-Guide/_history)
# Hello World 🌎

Provision your first server by opening a notebook ( `.ipynb` ), clicking *Select Kernel* in the top right and selecting *Colab* .

![selecting a kernel with the Colab option highlighted](https://private-user-images.githubusercontent.com/6925321/511452248-1c37673c-f5fe-41fa-862e-ccbbe964047b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii82OTI1MzIxLzUxMTQ1MjI0OC0xYzM3NjczYy1mNWZlLTQxZmEtODYyZS1jY2JiZTk2NDA0N2IucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTlUMDkyMTM3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YWQzMzBmM2M0ODQ4NzYzZTQxNzQ3ZGVjZjUyNjAxMGJiMTgyMmE1ZGVhZjE2YjIwMGJjYTBkNjcxOGM0Y2Q5MSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.-Nvs7pTjhm0y7nDhnsvf2nPPAan6UXjZdhLO8Hc5pDY)

Either *Auto Connect* to a default Colab server or select *New Colab Server* to provision a specific machine type.

![the Colab options when selecting a kernel](https://private-user-images.githubusercontent.com/6925321/511454394-8a5ed28f-783a-4f9f-80b7-37f8ee047ec5.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii82OTI1MzIxLzUxMTQ1NDM5NC04YTVlZDI4Zi03ODNhLTRmOWYtODBiNy0zN2Y4ZWUwNDdlYzUucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTlUMDkyMTM3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MTVlYWJhMTY3YTMwMzQ1YTUzM2JhOGJkYmFhOGJlOWNiNDVkNGYwOTM4OTMzNTczZDM4Mjk5ODM3ZDBjNzY1OCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.R1FXDHt0U9FinPPX4EcOvfFE6FYFfKzMgqLTvGrTl5U)

When prompted to *sign in using Google* , select *Allow* . You may be prompted to allow VS Code to open external links. Once you consent, your browser will open and you can select the account you wish to use and complete the OAuth sign-in flow.

![the Google OAuth consent screen where a user can select the account they want to sign in with and continue](https://private-user-images.githubusercontent.com/6925321/511461260-9b45b91d-0adb-405c-9bd6-7822b39ad5b8.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii82OTI1MzIxLzUxMTQ2MTI2MC05YjQ1YjkxZC0wYWRiLTQwNWMtOWJkNi03ODIyYjM5YWQ1YjgucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTlUMDkyMTM3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ODIzYWJiZmFmNjNiNDdmZTk5NzQxYWFhZDQ1YzJiNzIzMjJmZjI1ODBlNTU4NzFiOWFjMzdlYmRkNzUwOTg0YSZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.mP28w0wx2ibUe7ech_0Otq3qy2V5CyMt8nYwKIUMg2o)

Upon signing in, you should be automatically redirected back to VS Code. Depending on whether you have previously allowed your browser and VS Code to open links, you may be prompted before automatic redirection.

Once signed in, select the kernel you'd like to connect to.

![select the Colab kernel to connect to](https://private-user-images.githubusercontent.com/6925321/511458003-4f9c9a2d-6e5c-4174-86a7-4f6efc620fac.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii82OTI1MzIxLzUxMTQ1ODAwMy00ZjljOWEyZC02ZTVjLTQxNzQtODZhNy00ZjZlZmM2MjBmYWMucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTlUMDkyMTM3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9NWI5YTY4ZjU3MTdjNDM4MDFmYzUxZTA0YjhiMzkxZDI1YjA5ZGU2MDEyMGI5MWVmMDc0ODdlMzg0NTNlMWMzMCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.9VSbbC_95rYKTN7rXZIKgMiAF1t-Rt9GnsA6YDsJFTM)

Write some code!

![a successfully executed cell in a Jupyter notebook connected to a Colab server](https://private-user-images.githubusercontent.com/6925321/511458581-0de0530a-f5e8-418a-9843-1ac2c883b7e1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii82OTI1MzIxLzUxMTQ1ODU4MS0wZGUwNTMwYS1mNWU4LTQxOGEtOTg0My0xYWMyYzg4M2I3ZTEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTlUMDkyMTM3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9YWE0ZTRjZTk3YjQ1NzM1NjE0YzExYjAzNzJlMzliMjg0ODdkNjc2ODI5MzU2YmFjNTFkYmE4YjA2Nzk3Y2ZhOCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.HKzJYOBt25W23SiQebOodA8wSIHDQNsKhLgkqaZFqzo)

# Managing servers

## Removing a server

A server can be removed by either:

- Opening the command palette ( `[Ctrl|Cmd]+Shift+P` ) and invoking the `Colab: Remove Server` command, or
- Clicking the *Colab* button at the top of the notebook and selecting *Remove Server* .

## Provisioning a new server

Decided you want a different machine type? Doing work in parallel across notebooks? A new server can be provisioned by following the same steps detailed above (in the *Hello World 🌎* section) and selecting the *New Colab Server* option.

# Monitoring usage

## Status Bar

Once you signed in with Colab, you will see a Colab icon at the bottom right of your VS Code status bar with your current consumption rate:

![ColabStatusBar](https://private-user-images.githubusercontent.com/77074952/575612038-b5de98fe-f72f-4ba8-a2c0-1f2bc839fc6f.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii83NzA3NDk1Mi81NzU2MTIwMzgtYjVkZTk4ZmUtZjcyZi00YmE4LWEyYzAtMWYyYmM4MzlmYzZmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDE5VDA5MjEzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTgzOTg3M2Q1NTRmZDdkNGQzNzBiOWY1OTQ3ZGE0MmE2YzM0ZGM4NGIxZmVhOTAwZThiMTA2MmQ0ZDE1YWY0MjImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.H1ojrSRlt_mmRhBaPTx97FkzWLR4SDtqQ6CjPJ0AQns)

On hover, you can see more details about your current usage based on your Colab subscription.

## Activity Bar

See [Resource Monitor](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#resource-monitor) in the *Experimental Features* section.

# Working with files

## Activity Bar

Colab exposes an activity bar entry (the left panel, by default). Here in the *Contents* view, you can view Colab servers and interact with their `/content` directories right in VS Code.

## Uploading Files to Colab Servers

Once you've connected to a Colab server, you can right click files and folders in your VS Code *Explorer view* (or multi-selections of them) then select *Upload to Colab* .

If you only have one server assigned, your upload will begin immediately. If you have multiple servers, select the server you'd like to upload to.

The notification should communicate the outcome, but you can always manually peruse the Colab server's filesystem (e.g. `!ls /content` ).

File.upload.demo.webm## Mounting Google Drive

To get started, you can either:

- Open the command palette ( `[Ctrl|Cmd]+Shift+P` ) and invoke the `Colab: Mount Google Drive to Server...` command, or
- Click the *Colab* button at the top of the notebook and select *Mount Google Drive to Server* .

This will append a new cell to the active notebook with the snippet to kick-off Drive mounting:

Drive.mount.demo.for.wiki.webm# Coming from Colab on the web?

Are you coming from using Colab on the web? Learn about some of the differences and parallels between Colab on the web and Colab in VS Code.

## Runtimes, servers, kernels and sessions

When you go to [https://colab.research.google.com/](https://colab.research.google.com/) , you write some code, click ▶ and it auto-magically works! For a majority of Colab users, that simplicity is exactly what they want and love. This *auto-magical* executor of code is referred to as a *Runtime* in Colab on the web. In order to best understand how Colab's exposed in VS Code, the following terms are defined:

- A *Jupyter Server* : this core backend application that orchestrates the entire notebook experience. The intermediary between the notebook frontend (e.g. the Colab website or the VS Code notebook) and the computation engine (kernels).
- A *Kernel* : the computation engine that executes notebook code. When you click ▶ on a cell, that code is sent to a kernel which returns the output back to the server to be displayed in the notebook. Kernels are language specific (e.g. Python, Julia or R).
- A *Session* : links a specific notebook to a specific kernel instance.

**Analogy** : A restaurant manager ( *server* ) takes orders from waiters ( *notebook* ), delegates to the chefs ( *kernels* ) that read orders from an order ticket ( *session* ) and ensures the food gets back to the customer.

In Colab on the web, that simple *runtime* is actually a connection from your browser, to a single kernel session. In VS Code, you have the power to connect to exactly *what* you want.

# Experimental Features

Okay being on the bleeding edge and using some features which may be a bit rough around the edges? Read on!

Experimental features can be enabled in settings. After toggling, you may need to reload VS Code for it to take effect.

![Image](https://private-user-images.githubusercontent.com/6925321/529805914-602a1769-c6df-4c83-b8d2-b3704bb3b3f1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii82OTI1MzIxLzUyOTgwNTkxNC02MDJhMTc2OS1jNmRmLTRjODMtYjhkMi1iMzcwNGJiM2IzZjEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTlUMDkyMTM3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9ZDU1YzRjM2YyMjczZmZkMWRhZDQ3MGRjYjI2Y2FjN2U0ZTBhYjNhY2VmOTE3NzIyNGFkZjZjNGI5YzI3YzhlOCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.3JDD-0AjDBuBF5OMlSQo2KdX331VK3pJgwzY9Z47AXk)

Please search for existing issues before filing a new one, especially for experimental features.

## Server Mounting

With the experimental *Server Mounting* feature enabled, once you've created a Colab server you can mount it through:

- The command palette: `[Ctrl|Cmd]+Shift+P > Colab: Mount Server To Workspace...` .
- The notebook toolbar ( *Colab* button in notebooks) \> *Mount Server To Workspace* .

With the server mounted, you can view, create, edit, and delete files right in VS Code. Currently, file modifications outside of VS Code aren't picked up but can be by hitting the refresh icon at the top of the *Workspace* toolbar.

mount.demo.webm## Colab Terminal

With the experimental *Terminal* feature enabled, you may now open a terminal connected to your Colab runtime in 2 ways:

- Open the command palette ( `[Ctrl|Cmd]+Shift+P` ) and invoke the `Colab: Open Terminal` command.
- Click the *Colab* button at the top of the notebook and select *Open Terminal* .

Colab.terminal.demo.webm## Resource Monitor

With the experimental *Activity Bar Resource View* feature enabled, you may monitor your Colab server resources (RAM, Disk, GPU) in the existing *Colab* activity bar.

![image](https://private-user-images.githubusercontent.com/77074952/571507475-078b6699-aff3-4e88-9db3-62b71508e286.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii83NzA3NDk1Mi81NzE1MDc0NzUtMDc4YjY2OTktYWZmMy00ZTg4LTlkYjMtNjJiNzE1MDhlMjg2LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MTklMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDE5VDA5MjEzN1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWNkYmJmM2JiZjJiMTZhMTg1ODJhZWVjOWM5M2M2MTQ0ZWEzZWUzNTE0MWFjYTI4NjhlMWE3ZWYxNDgzZGI3MWImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.JNHkYSeov1Ud768hPebVtALICQI_11koYsqRe1aLbfo)

# Changing Log Verbosity

Often useful when debugging issues with the team, you can change the log verbosity by modifying the `Colab > Logging: Level` setting.

![Colab logging setting](https://private-user-images.githubusercontent.com/6925321/517632332-67a4111a-29c2-4aae-9dfc-d71ce0850de1.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzY1OTA3OTcsIm5iZiI6MTc3NjU5MDQ5NywicGF0aCI6Ii82OTI1MzIxLzUxNzYzMjMzMi02N2E0MTExYS0yOWMyLTRhYWUtOWRmYy1kNzFjZTA4NTBkZTEucG5nP1gtQW16LUFsZ29yaXRobT1BV1M0LUhNQUMtU0hBMjU2JlgtQW16LUNyZWRlbnRpYWw9QUtJQVZDT0RZTFNBNTNQUUs0WkElMkYyMDI2MDQxOSUyRnVzLWVhc3QtMSUyRnMzJTJGYXdzNF9yZXF1ZXN0JlgtQW16LURhdGU9MjAyNjA0MTlUMDkyMTM3WiZYLUFtei1FeHBpcmVzPTMwMCZYLUFtei1TaWduYXR1cmU9MGYyMTRjMWE1NjU3OTIyYTcwZjVhN2JhNDQ5MTE2ZDI1MzE2ZjAxZTVjNGY2OTFlYWFhMjYxMjk0YjYzY2Q1NCZYLUFtei1TaWduZWRIZWFkZXJzPWhvc3QmcmVzcG9uc2UtY29udGVudC10eXBlPWltYWdlJTJGcG5nIn0.9ihLrtd6DbAyZtI-wL-529_K98_tHiR-P6oYz5ZG7NA)

## Toggle table of contents Pages3

- LoadingHome
  
  ### Uh oh!
  
  There was an error while loading. Please reload this page .
- LoadingKnown Issues and Workarounds
  
  ### Uh oh!
  
  There was an error while loading. Please reload this page .
- LoadingUser Guide
  
    - [Hello World 🌎](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#hello-world-)
    - [Managing servers](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#managing-servers)
    - [Removing a server](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#removing-a-server)
    - [Provisioning a new server](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#provisioning-a-new-server)
    - [Monitoring usage](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#monitoring-usage)
    - [Status Bar](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#status-bar)
    - [Activity Bar](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#activity-bar)
    - [Working with files](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#working-with-files)
    - [Activity Bar](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#activity-bar-1)
    - [Uploading Files to Colab Servers](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#uploading-files-to-colab-servers)
    - [Mounting Google Drive](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#mounting-google-drive)
    - [Coming from Colab on the web?](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#coming-from-colab-on-the-web)
    - [Runtimes, servers, kernels and sessions](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#runtimes-servers-kernels-and-sessions)
    - [Experimental Features](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#experimental-features)
    - [Server Mounting](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#server-mounting)
    - [Colab Terminal](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#colab-terminal)
    - [Resource Monitor](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#resource-monitor)
    - [Changing Log Verbosity](https://github.com/googlecolab/colab-vscode/wiki/User-Guide#changing-log-verbosity)

### Clone this wiki locally
