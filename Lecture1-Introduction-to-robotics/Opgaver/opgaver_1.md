# Opgave 1: Forbind SSH i Visual Studio Code

![SSH i VS Code](../images/image1.png)

## Forbind SSH i Visual Studio Code (Komplet Opgave)

### Formål

Efter gennemførelse af denne opgave skal den studerende kunne:

* Oprette og anvende SSH-nøgler.
* Konfigurere filen `~/.ssh/config`.
* Installere og anvende udvidelsen **Remote - SSH** i Visual Studio Code til at oprette forbindelse til en fjernserver.
* Åbne en mappe på en fjernserver i VS Code og køre terminalkommandoer via SSH.
* Fejlsøge almindelige SSH-relaterede problemer.

---

## Forudsætninger (Det skal du have klar)

Før du starter, skal du sikre dig, at du har:

* En lokal computer med **Visual Studio Code** installeret.
* En internetforbindelse.
* En fjernserver med SSH-adgang (IP-adresse/værtsnavn og brugernavn), for eksempel:

  * En Linux-virtuel maskine (VM)
  * En VPS (Virtual Private Server)
* Adgang til fjernserverens `~/.ssh/authorized_keys`-fil (kan opdateres af serveradministratoren, hvis det er nødvendigt).

---

## Materialer / Værktøjer

* **Visual Studio Code** (seneste version)
* VS Code-udvidelse: **Remote - SSH** (Microsoft)
* En terminalapplikation:

  * Bash
  * PowerShell
  * macOS Terminal
  * WSL (Windows Subsystem for Linux)
* *(Valgfrit)* Git-klient

---

## Videovejledning

📺 **YouTube-tutorial:**

[Sådan opretter du SSH-forbindelse i VS Code](#)

---

## Forventet Resultat

Når opgaven er afsluttet, skal du kunne oprette forbindelse til en fjernserver direkte fra Visual Studio Code, redigere filer på serveren og anvende den integrerede terminal til at udføre kommandoer via SSH.

# Autoriserede rettigheder af Zuhair Haroon Khan