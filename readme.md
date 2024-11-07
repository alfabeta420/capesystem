# Capesystem

This project pretends to be an Optifine server and makes you able to wear custom cosmetics in Minecraft!

## How to install

You have to configure your Discord bot in file `config.py`. All information relative to the configuration process are written in the file.



Install following Python modules:
- `flask`
- `py-cord==2.0.0rc1`

<hr>

If you finished configuring the bot and installing the required modules you can run the project fine! Try using:

    python3 main.py

for Ubuntu or for Windows:

    py main.py

<hr>

To redirect all connections from optifine server to your vps use hosts file located in:

    C:\Windows\System32\drivers\etc\hosts

Just add there a line: 

    0.0.0.0 s.optifine.net

And then change `0.0.0.0` to your vps IPv4.

<hr>

<i>Warning: DO NOT host this `localhost` server. The script will not be able to download files from origin optifine server if the connection is redirected to the localhost. Hosting this project on a vps is recommended!</i>

## Using the bot

### Register

Use `/register <username>` command in the selected channel to bind your Minecraft username to the Discord account.

<hr>

### Cape

Use `/cape <id>` command in the selected channel to set any cape from the `capes` folder.

<hr>

### Cape caching

The `cached_capes` folder is only a cache for downloaded capes.
You can clear it using `/cache` command in your Discord server.

## Problem solving

If something doesn't work open cmd and type:

    ipconfig /flushdns

Have fun with my custom optifine capes system!
https://github.com/alfabeta420
