# LaBoum
## <#>-------------<=======[ Description ]=======>-------------<#>

English:  
    LaBoum is a One Piece themed dice-rolling bot for Discord.  
    Its main function is to roll dice. (even hit dice and coin flip are available)  
    The bot will start in english language by default.  
    The rest of the README.md is only available in english language for the time being.  

Deutsch:  
    LaBoum ist ein, an One Piece thematisch angepasster Würfel-Bot für Discord.  
    Seine Hauptfunktion ist es zu würfeln. (auch Trefferwürfel und Münzwurf sind verfügbar)  
    Der Bot startet aktuell in englischer Sprache.  
    Mit "/language de" lässt sich die Sprache auf deutsch umstellen.  
    Der Rest der README.md ist vorerst nur in englisch verfügbar.  


## <#>-------------<=======[ Disclaimer ]=======>-------------<#>

This bot is NOT a simple plug-and-play installation.  
There is no invite-link for just joining on a discord server.  
You need to set it up yourself!  

To create a bot you first have to create an application in the 'Discord Developer Portal' and then add a bot to your application.
Next you need to add the bot to your server. Simply replace the '##################' with your application ID.
(Bot invite link: https://discord.com/oauth2/authorize?client_id=##################&scope=bot)  
Now you need a place to host the bot. If you need it running 24/7 you should consider hosting it on a onw or rented server. For short time use you can also run it in an IDE or in a terminal.  
Optional: You can give your bot a role for better rights management.  

## <#>-------------<=======[ Commands ]=======>-------------<#> 
    All listed bot commands are in need of a "/" (slash) as first character of the command.  
    (Note: You are able to change the "/" in the language txt files)  
    
  
### Help:

| Command | Description |
| --- | ---|
/help      | displays the necessary commands for any player
/helpmaster| displays the necessary commands for the gamemaster (including all from player)

  
### Language:

| Command | Description |
| --- | ---|
/lang(uage)| displays the currently chosen language and other available languages   
/lang(uage) xx| changes the language to xx [currently available: en, de]

  
### Dice:  
  
To roll dice you have to follow the following input-pattern:
| Command | Explanation |
| --- | --- |
/XdY{#Z}| / is needed to be recogniced as a command
/<b>4</b>d2+6| X is the amount of dice
/4d<b>2</b>+6| Y is the kind of dice
/4d2<b>+</b>6| # is the operand (+, -, *, /)
/4d2+<b>6</b>| Z is the value
/4d2<b>+6</b>| {} from pattern means it is optional input
/4d2| here is the example without the optional input operation

The output for the last example would get an output like this:   
Rolled: 4x d2 +6: 1 + 2 + 1 + 1 = 5 + 6 = 11 @name  
Rolled: 4x d2: 1 + 2 + 1 + 1 = 5 @name

  
### Simplyfied throws:

| Command (short) | Command (actual) | Description |
| --- | --- | --- |
/1 or /2 or /3 | rolls 1, 2 or 3 d20's | simplyfied d20's
/4 or higher   | rolls 1d4 or higher   | simplyfied single dice throw
/d2 or higher  | rolls 1d2 or higher   | simplyfied single dice throw (alternative)

As with the normal dice you can optional add an 'operand' and a 'value'.
| Example | Command (actual) |
| --- | ---|
/2-5      | rolls 2d20-5
/10/2     | rolls 1d10/2
/d13-2    | rolls 1d13-2

  
### Other dice:

| Command | Description |
| --- | ---|
/coin     | delivers exactly 'high (head)' or 'low (tail)'
/hit      | rolls where a character gets hit
/adv      | rolls with advantage: 2d20, higher one counts
/dis      | rolls with disadvantage: 2d20, lower one counts

  
### Other useful commands:

| Command | Description |
| --- | ---|
/credits  | information about the contributors
/cut text | creates a seperator with 'text' as heading
/exit0    | shuts the bot down - you have to manually start it again afterwards
/status   | pings the bot to see if it is ready to be used
/version  | displays the current version of the bot
/wiki     | sends a link to onepiece.fandom and opwiki

  
### Bonus:
There are currently two commands that are intentional not listed here.   
Those two commands are eastereggs and do also need a '/' to get triggered.

  
## <#>-------------<=======[ Configurations ]=======>-------------<#>

Currently there are three easy configurations, you can change if you want.  
For doing this you do not have to know anything about programming.  
As this is an open source project you are free to edit the code yourself.

1. ### Hit body dice configuration:
    You are able to change the values of the bodyparts of the hit dice:

    ```
    line    code            comment
    ------------------------------------------------------------
    275     arm = 3         # (consider: it's the value per arm)
    276     leg = 3         # (consider: it's the value per leg)
    277     head = 2
    278     back = 2
    279     chest = 4
    ```
    In this case the chance to hit the left arm is 3 out of 20  
    (arm +arm +leg +leg +head +back +chest = 20)  
    The sum (here 20) does not have to be exactly 20!

      
2. ### Token configration:
    
    ```
    435     token = "mytoken" # here you are able to replace the word <mytoken> with your 59 character token (not recommended)
    ```
    If you want to store your bot-token in the code you have to replace the word 'mytoken' but it is recommended not to store the token in the code. Read more about the token in chapter 'Token safety'.

      
3. ### Language output configuration:
    You can change the output texts of the bot in the txt-files of the languages-folder.  
  
## <#>-------------<=======[ Token safety ]=======>-------------<#>
The token of a discord bot is unique and should not be readable to others.  

To clarify:  
Someone who is able to get the token of your discord bot will not be able to access your sourcecode or be able to gain immediate access to your server or computer.
Someone who is able to get the token of your discord bot will be able to controll your bot from writing text messages up to deleting content, channels and even banning people from the server. This is due to the fact that any owner of the token can write own code - most times with malicious intentions - to be executed by your bot.  

The token is most likely like a password. Anyone who sees your password (=token) can use it to controll the corresponding account/Device. So do not leak it!

**If your token ever gets leaked, head immediately to the 'Discord Developer Portal' to change the token.**  

This is the reason the token should not be visible in the code, so you are not in danger of accedently revealing it to someone or even uploade it.
The first time you use LaBoum, it will automaticly ask you for the token to get saved locally in a file named 'token.txt'.

In case you want to code with this bot and use git the token.txt is also listed in the .gitignore.

  
## <#>-------------<=======[ Other ]=======>-------------<#>

If you have any suggestions, improvements, bugs, misbehaviours or questions feel free to contribute, open issues or contact me:  
https://github.com/swalbart  
https://github.com/swalbart/LaBoum