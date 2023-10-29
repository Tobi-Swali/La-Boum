import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

language = "en"
langPath = "languages/"+language+".txt"
print("Greetings, The bot boots with its default language: "+language+".")

# useful shortcut and markdown as variables for coding
rt = "\n"       # rt = return
cb = "```"      # cb = codeblock
#ii = "*"        # ii = italics
bb = "**"       # bb = bold
#ib = "***"      # ib = italics and bold
#uu = "__"       # uu = underlined
#cc = "~~"       # cc = crossed (out)

@client.event
async def on_ready():
    print('We have logged in as {self.user}.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="'/help'"))

@client.event
async def on_message(message):
    # make sure to not get triggered by own messages
    if message.author == client.user:
        return
    m= message.content
    m =m.lower()

    output = ""
    authorID = " <@" +str(message.author.id) +">"

#-----------------------------COMMANDS-----------------------------COMMANDS-----------------------------COMMANDS-----------------------------COMMANDS-----------------------------#
    
    if m.startswith(getText("cmd_sign")) or m.startswith(getTextDefault("cmd_sign")):
        m = m[-(len(m)-1):]                 # remove first charater
        # ping test: status
        if m.startswith(getText("cmd_status")) or m.startswith(getTextDefault("cmd_status")):
            output = getText("status")
        # help: commands for player and master
        elif m.startswith(getText("cmd_help_player")) or m.startswith(getTextDefault("cmd_help_player")):
            output = cb
            if m.startswith(getText("cmd_help_master1")) or m.startswith(getText("cmd_help_master2")) or m.startswith(getTextDefault("cmd_help_master1")) or m.startswith(getTextDefault("cmd_help_master2")):
                output += getText("help_master01")+rt+getText("help_master02")+rt+getText("help_master03")+rt+getText("help_master04")+rt+getText("help_master05")+rt+getText("help_master06")+rt+getText("help_master07")+rt+getText("help_master08")+rt+getText("help_master09")+rt+rt
            output += getText("help_player01")+rt+getText("help_player02")+rt+getText("help_player03")+rt+getText("help_player04")+rt+getText("help_player05")+rt+getText("help_player06")+rt+getText("help_player07")+cb
        # text commands
        elif m.startswith(getText("cmd_links")) or m.startswith(getTextDefault("cmd_links")):
            output = getText("links1")+rt+getText("links2")
        elif m.startswith(getText("cmd_theme_default")):
            if m.startswith(getText("cmd_theme_ping")):
                output = getText("ping")+rt
            output += theme()
        elif m.startswith(getText("cmd_cut")) or m.startswith(getTextDefault("cmd_cut")):
            output = seperator(m)
        elif m.startswith(getText("cmd_nani")) or m.startswith(getTextDefault("cmd_nani")):
            output = "<:sanji:725100920576147487><:nani:725100919703863407>"
        elif m.startswith(getText("cmd_beri")) or m.startswith(getTextDefault("cmd_beri")):
            output = bb+"["+bb+"<:Beri:735987151485010021>"+bb+"(O.O)"+bb+"<:Beri:735987151485010021>"+bb+"]"
        elif m.startswith(getText("cmd_credits")) or m.startswith(getTextDefault("cmd_credits")):
            output = getText("credits1")+rt+getText("credits2")+rt+getText("credits3")+rt+getText("credits4")
        elif m.startswith(getText("cmd_hit")) or m.startswith(getTextDefault("cmd_hit")):
            output = getText("hit_dice") +roll_hit() + authorID
        elif m.startswith(getText("cmd_coin")) or m.startswith(getTextDefault("cmd_coin")):
            output = getText("coin_dice") +roll_coin() + authorID
        # languages
        elif m.startswith(getText("cmd_language_list")) or m.startswith(getTextDefault("cmd_language_list")):
            output = getLangList()
        elif m.startswith(getText("cmd_language_set")) or m.startswith(getTextDefault("cmd_language_set")):
            output = changeLanguage(m)
        elif m.startswith(getText("cmd_language_get")) or m.startswith(getTextDefault("cmd_language_get")):
            output = getText("language_selected")+getText("language_now")
        # maintenance
        elif m.startswith(getText("cmd_shutdown")) or m.startswith(getTextDefault("cmd_shutdown")):
            await message.channel.send(getText("shutdown"))
            print("shutdown: "+"LaBoum will now be shut down. It will not boot up on its own!"+rt)
            exit()
        elif m.startswith(getText("cmd_version")) or m.startswith(getTextDefault("cmd_version")):
            output = "0.3.4"
        # unlisted in language-files
        elif m.startswith("dev"):
            output = getText("status")

#-----------------------------DICE---------------------------------DICE---------------------------------DICE---------------------------------DICE---------------------------------#

        # dice-command-calculation
        # inputfilter (d,w,1-9)
        if (output == "" and (len(m)>=1) and ((m[0]=="d") or (m[0]=="w") or (m[0]=="1") or (m[0]=="2") or (m[0]=="3") or (m[0]=="4") or (m[0]=="5") or (m[0]=="6") or (m[0]=="7") or (m[0]=="8") or (m[0]=="9"))):
            amountStr = ""
            valueStr = ""
            diceStr = ""
            operand = ""                # 'operand'
            amount = 0                  # 'amount' of dice
            value = 0                   # 'value' of the operand
            dice = 0                    # kind of 'dice'
            dw = "x"

            # check for 'amount'
            while ((len(m) != 0) and ((m[0] != "d") and (m[0] != "w") and (m[0] != "+") and (m[0] != "-") and (m[0] != "*") and (m[0] != "/"))):
                if(((m[0] == "0") and (amountStr !="")) or (m[0] == "1") or (m[0] == "2") or (m[0] == "3") or (m[0] == "4") or (m[0] == "5") or (m[0] == "6") or (m[0] == "7") or (m[0] == "8") or (m[0] == "9")):
                    amountStr += m[0]
                if (len(m)>1):
                    m = m[-(len(m)-1):]
                else:
                    m = ""
            # edgecase: no amount
            if amountStr == "":
                amountStr = "1"
            # convert 'amount'
            amount = int(amountStr)

            # if m is still a message go on
            if len(m) !=0:
                if ((m[0] == "d") or (m[0] == "w")):
                    dw = m[0]
                    m = m[-(len(m)-1):]

                # check 'dice'
                while ((len(m) != 0) and ((m[0] != "+") and (m[0] != "-") and (m[0] != "*") and (m[0] != "/"))):
                    if(((m[0] == "0") and (diceStr !="")) or (m[0] == "1") or (m[0] == "2") or (m[0] == "3") or (m[0] == "4") or (m[0] == "5") or (m[0] == "6") or (m[0] == "7") or (m[0] == "8") or (m[0] == "9")):
                        diceStr += m[0]
                    if (len(m)>1):
                        m = m[-(len(m)-1):] 
                    else:
                        m = "+"
                # convert 'dice'
                if diceStr !="":
                    dice = int(diceStr)

                # check 'operand'
                if len(m) >1:
                    operand = m[0]
                    m= m[-(len(m)-1):]

                    # check 'value'
                    while (len(m) != 0):
                        if(((m[0] == "0") and (valueStr !="")) or (m[0] == "1") or (m[0] == "2") or (m[0] == "3") or (m[0] == "4") or (m[0] == "5") or (m[0] == "6") or (m[0] == "7") or (m[0] == "8") or (m[0] == "9")):
                            valueStr += m[0]
                        if (len(m)>1):
                            m = m[-(len(m)-1):] 
                        else:
                            m = "" 
                    # convert 'value'
                    value = int(valueStr)
            
            # short throws (/X)
            if dw == "x":
                # short throw (/1 /2 /3 = 1d20 2d20 3d20)
                if amount <= 3:
                    dice =20
                    diceStr ="20"
                # short throw (/X =1dX)
                else:
                    dice = amount
                    diceStr = amountStr
                    amount = 1
                    amountStr = "1"
                dw = "d"

            # roll the dice
            if  (dice>0):
                if(value>0):
                    output = "Rolled: " +amountStr +"x " +dw +diceStr +" " +operand +valueStr +":   " +roll(amount, dice, operand, value) +authorID
                else:
                    output = "Rolled: " +amountStr +"x " +dw +diceStr +":   " +roll(amount, dice, operand, value) +authorID
            else:
                output = "Command failed"
                # for debugging
                print(output+": <"+m+"> (["+amountStr+";"+str(amount)+"]["+dw+"]["+diceStr+";"+str(dice)+"]["+operand+"]["+valueStr+"]["+str(value)+"])")

        # check if any 'output' available
        if output == "":
            # No 'output' means incorrect command
            output = getText("general_error_input")
        # send the 'output' to discord
        await message.channel.send(output)

#-----------------------------LANGUAGE-----------------------------LANGUAGE-----------------------------LANGUAGE-----------------------------LANGUAGE-----------------------------#

# get current language
def getLanguage():
    return language

# get all available languages
def getLangList():
    fileList = ""
    for file in os.listdir("languages"):
        fileList += str(file[:-4])+rt # deletes the last 4 characters: '.txt'
    return fileList

# set new language 'lang'
def setLanguage(lang):                  
    global language
    global langPath
    selectedLanguage = language
    language = lang
    langPath = "languages/"+language+".txt"
    output = getText("language_change_success")+" "+getText("language_now")
    if selectedLanguage == lang:
        output = getText("language_change_error_same_lang")
    return output

def changeLanguage(m):
    output = ""
    mArray = m.split()
    printLangInfo = True
    print("mArray:   "+str(mArray))
    if len(mArray) == 2:                    # allwos two arguments (2nd arguement is language string)
        langArr = getLangList().split(rt)
        for entry in langArr:
            if (mArray[1] == entry):        # check if input language string is valid
                output = setLanguage(mArray[1])
                printLangInfo = False
        if output == "":                    # non-valid language: error
            output += getText("language_error_unknown")+" ("+mArray[1]+")"+rt
    elif len(mArray) > 2:                   # too many arguments: error
        output += getText("language_error_too_many_arguments")+rt
    if printLangInfo:                       # adds info about 'lang' command
        output += getText("language_selected")+getLanguage()+rt
        output += getText("language_change_text")
        output += " "+bb+getText("cmd")+getText("cmd_language_set")+" xx"+bb+rt
        output += getText("language_replace_text")+rt+str(getLangList())
    return output

def getText(name):                  # returns the 'value' assignet to the 'name'
    path = langPath
    return getText2(name, path)
    
# gets the string from the language file of the currently chosen language
def getText2(name, path):
    with open(path) as f:
        lines =f.readlines()
        for line in lines:
            if line.startswith(name):
                # shorten 'line' by the length of 'name' from the front:
                value =line[(len(name)):]
                value =value.lstrip()        # erase leading whitespaces
                if value.startswith("."):       # replace first '.' with a whitespace
                    value =value[-(len(value)-1):]
                    value =" "+value
        return value[:-1]

# gets the string from the default language: en
def getTextDefault(name):
    return getText2(name, "languages/en.txt")

#-----------------------------METHODS------------------------------METHODS------------------------------METHODS------------------------------METHODS------------------------------#

# seperator line with custom text
def seperator(m):
    output1 = "```\\\n |~==+++<<<<#####$$$$$$§§§§§§§"
    output2 = " §§§§§§§$$$$$$#####>>>>+++==~\n/```"
    messageArr = m.split()
    messageArgs = len(messageArr)
    argsCounter = 1
    message = ""
    while argsCounter<messageArgs:
        message += (" " +messageArr[argsCounter])
        argsCounter += 1
    return (output1 +message +output2)

# roll hit dice
def roll_hit():
    # frequencies of body parts (customizable:)
    # (standard DsA: 3,3,2,2,4)
    arm = 3         # (consider: it's the value per arm)
    leg = 3         # (consider: it's the value per leg)
    head = 2
    chest = 2
    back = 4
    # sum up and roll dice
    amount = (2*arm +2*leg +head +chest +back)
    result = random.randint(1, amount)
    hit = ""
    if result<=arm:
        hit = getText("hit_arm_left")
    elif result<=(2*arm):
        hit = getText("hit_arm_right")
    elif result<=(2*arm +leg):
        hit = getText("hit_leg_left")
    elif result<=(2*(arm+leg)):
        hit = getText("hit_leg_right")
    elif result<=(amount-(chest +chest)):
        hit = getText("hit_head")
    elif result<=(amount-chest):
        hit = getText("hit_back")
    elif result<=amount:
        hit = getText("hit_chest")
    else:
        hit = getText("hit_error")
    return hit
    
# flip coin
def roll_coin():
    coin = random.randint(1, 2)
    output = ""
    if coin==1:
        output = getText("coin_high")
    elif coin==2:
        output = getText("coin_low")
    else:
        output = getText("coin_error")
    return output

# roll dice
# a = amount; d = dice-sides; o = operator; v = value for operator
def roll(a, d, o, v):
    # roll the dice and sum up to total
    num = random.randint(1, d)
    total = num
    output = str(total)
    counter = a
    while counter>1:
        num = random.randint(1, d)
        total += num
        output += (" + " +str(num))
        counter -= 1
    if a != 1:
        output += (" = " +str(total))
    # calculate with operator if given
    if o != "":
        output += (" " +o +" " +str(v) +" = ")
        if o == "+":
            output += str(total+v)
        elif o == "-":
            output += str(total-v)
        elif o == "*":
            output += str(total*v)
        elif o == "/":
            output += (str(round((total/v),2))+"*")
    return output

#-----------------------------VISUALS------------------------------VISUALS------------------------------VISUALS------------------------------VISUALS------------------------------#

def theme():
    output  = "                                                OOooO°OO  °#*°o°     °o*O                                    "+rt
    output += "   °.O@@@@@@@@@@@@@@@@@@@@@@@o°#@@@@@@@@@@@@@@# *. @@   °@O@*°. oOoOO  #@. *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#"+rt
    output += " *.  .#                     #   oO.              *o*  ooo  Oo**      *o..O                              **°° "+rt
    output += " *  .  .   *O@@@@@@@@#o.   .  *##@@o @@@@o#@@#@@@@@#   o##@@@@O.    *@#.  o#####@@##o  °oOOO°         *O@@@* "+rt
    output += "     . .@@@@@@@@@@@@@@@@@@#  . #@@@@°@@@@.@@@@@#oo#@°  °@@@@#@@@O   @@@#  °@@@@@OO#@@*@@@@@@@@o    O@@@o .   "+rt
    output += "      @@@@@@O°       *@@@@@@O  o@@@@O@@@@ O@@@.     .   @@@° #@@@  .#@@o   @@@o     #@@@@*°@@@@  #@@@.       "+rt
    output += "     @@@@@o            °@@@@@# o@@@@@@@@@ o@@@          @@@. #@@@°@@@@@@@@.@@@       @@@@  @@@@.@@@@         "+rt
    output += "    @@@@@@@@@@@@@@@@@@@@@@@@@@°*@@@@@@@@@ *@@@   O      @@@  #@@@O@.O@@°O@*@@@    o .@@@@ .OOOo@@@@  #o °o.  "+rt
    output += "   O@O° ..   .           °°.*#@@@@@@@@@@@ °@@@o#@@      @@@  @@@@ O@@@@@@* @@@#O@@O °@@@@      @@@@@@@@@@@@° "+rt
    output += "   °@@@@O .@@@@o   #@@@O  @@@@@O@@@@@@@@@ °@@@  °@      @@@  @@@@ .@@@@@@  @@@   Oo °@@@@  ...°@@@@ .@@#o#@  "+rt
    output += "    @@@@@ o@@@@@  o@@@@@ O@@@@°O@@@@@@@@@ °@@@          @@@@@@@@   @@@@@O  @@@      .@@@@  @@@@o@@@.   o*#** "+rt
    output += "     @@@@@o***° o#  ****@@@@@o @@@@@@@@@@ *@@@         .@@@O°.     *@@@@°  @@@      o@@@@  @@@@ °@@@°  *o*@@#"+rt
    output += "      @@@@@@#*  *O   O@@@@@@O  @@@@*@@@@@ o@@@#    @   °@@@°        @@@.  °@@@@    O@@@@@@@@@@@   O@@#°*.*   "+rt
    output += "    .. °@@@@@@##O*O#o@@@@#O  °°@@@@o*@@@@°#@@@@@@@@@   #@@@#       .@@@o  #@@@@@@@@@o @@@@@@@#      °@#.@#o  "+rt
    output += "**    .. °O***°*° *°oo*oo  .° °°°@O. *****@###@Ooo**   ********°..o*   °°.****@OOO##.   .**.         **o*@@O "+rt
    output += " .*  *@o*oO@@@O°..°O@@@@@#o*#o .O@@@@@@@@@@@@#ooooO#@@@@@@@@@@@@#Ooo#@@@@@@@@@@@@#OooO@@@@@#@@@@@@@OoO@@@@@@o"+rt
    output += "   °o@***                    .°oooo.            .°*°o*°           ..**o*.           .°*ooo°°.°°ooo*.         "+rt
    output += "      .*                                                                                . °°**°°             "+rt
    return cb+output+cb

#-----------------------------TOKEN--------------------------------TOKEN--------------------------------TOKEN--------------------------------TOKEN--------------------------------#

#-------------------------------------------------------------------------------------------------------------------------#
# For all who rather want to paste the token here instead of saveing it to the token.txt can do it the following way.     #
# But I reccomend to not keep in the sourcecode because the key is unique and anyone can controll your bot with this key: #
#-------------------------------------------------------------------------------------------------------------------------#
token = "mytoken" # here you are able to replace the word <mytoken> with your 59 character token (not recommended)

if(len(token)<59):
    # check for token in token.txt
    token_path = 'token.txt'
    if os.path.exists(token_path):
        # token exits in token.txt
        with open(token_path, 'r') as file:
            token = file.read().replace('\n', '') 
    else:
        # no token found
        tokenInit = rt+getText("token1")+rt+getText("token2")+rt+getText("token3")+rt+getText("token4")
        token = input("Discord token:")
        with open(token_path, 'w') as file:
            file.write(token)
client.run(token)