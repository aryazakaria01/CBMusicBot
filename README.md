<h2 align="centre">🎶 Cyber Music Bot 🎶</h2>

### Cyber Music is a telegram bot project that's allow you to play music on telegram voice chat group.

<p align="center"><a href="https://t.me/CyberMusicBot"><img src="https://telegra.ph/file/a884f8f101263a935b154.jpg" width="300"></a></p>
<p align="center">
    <a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Made%20with-Python-black.svg?style=flat-square&logo=python&logoColor=blue&color=red" /></a>
    <a href="https://github.com/aryazakaria01/CBMusicBot/graphs/commit-activity" alt="Maintenance"> <img src="https://img.shields.io/badge/Maintained%3F-yes-red.svg?style=flat-square" /></a>
    <a href="https://app.codacy.com/gh/aryazakaria01/CBMusicBot/dashboard"> <img src="https://img.shields.io/codacy/grade/a723cb464d5a4d25be3152b5d71de82d?color=red&logo=codacy&style=flat-square" alt="Codacy" /></a><br>
    <a href="https://github.com/aryazakaria01/CBMusicBot"> <img src="https://img.shields.io/github/repo-size/aryazakaria01/CBMusicBot?color=red&logo=github&logoColor=blue&style=flat-square" /></a>
    <a href="https://github.com/aryazakaria01/CBMusicBot/commits/main"> <img src="https://img.shields.io/github/last-commit/aryazakaria01/CBMusicBot?color=red&logo=github&logoColor=blue&style=flat-square" /></a>
    <a href="https://github.com/aryazakaria01/CBMusicBot/issues"> <img src="https://img.shields.io/github/issues/aryazakaria01/CBMusicBot?color=red&logo=github&logoColor=blue&style=flat-square" /></a>
    <a href="https://github.com/aryazakaria01/CBMusicBot/network/members"> <img src="https://img.shields.io/github/forks/aryazakaria01/CBMusicBot?color=red&logo=github&logoColor=blue&style=flat-square" /></a>  
    <a href="https://github.com/aryazakaria01/CBMusicBot/network/members"> <img src="https://img.shields.io/github/stars/aryazakaria01/CBMusicBot?color=red&logo=github&logoColor=blue&style=flat-square" /></a>  
</p>

<h3>Requirements 📝</h3>

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.8+ or 3.7
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)
- [MongoDB](https://cloud.mongodb.com/)

🧪 Get STRING_SESSION from below:

TAP THIS: [![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@Arya01/PyrogramMusicString#main.py)

🎖 History
- [![Mentioned in Awesome Python](https://awesome.re/mentioned-badge.svg)](https://github.com/aryazakaria01/CBMusicBot)

## Features 🔮

- Thumbnail Support
- Playlist Support
- Showing track names when skipping
- Youtube, Local playback support
- Settings panel
- Control with buttons
- Userbot auto join
- Channel Music Play
- Keyboard selection support for youtube play
- Lyrics Scrapper
- Unlimited Queue
- Broadcast Bot
- Statistic Collector
- Group Tools (ban/unban/mute/unmute)
- Block / Unblock (restrict user for using your bot)

## Commands 🛠

- `/play <song name>` - play song you requested
- `/playlist` - Show now playing list
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details
- `/vsong <song name>` - download videos you want quickly
- `/lyric <song name>` - lyrics scrapper
- `/vk <song name>` - generate song without download

#### Admins Only 👷‍♂️
- `/player` - open music player settings panel
- `/pause` - pause song play
- `/resume` - resume song play
- `/skip` - play next song
- `/end` - stop music play
- `/musicplayer on` - to disable music player in your group
- `/musicplayer off` - to enable music player in your group
- `/userbotjoin` - invite assistant to your chat
- `/userbotleave` - remove assistant from your chat
- `/reload` - Refresh admin list
- `/uptime` - check the bot uptime status
- `/ping` - check the bot ping status
- `/auth` - authorized people to access the admin commands
- `/deauth` - deauthorized people to access the admin commands
- `/control` - open the music player control panel

### Sudo User 🧙‍♂️
- `/stats` - see the bot statistic
- `/pmpermit on | off` turn on/off the assistant pmpermit
- `/userbotleaveall` - order the assistant to leave all groups
- `/gcast` - send a broadcast message from the assistant

### Owner Only 👨🏻‍✈️
- `/broadcast` - send a broadcast message from the bot
- `/block` - block people for using your bot
- `/unblock` - unblock people you blocked for using your bot
- `/blocklist` - show the list of all people who's blocked for using your bot

### pm-permit 💬
- `.yes` - approve user for sending message to assistant
- `.no` - disapprove user for sending message to assistant

## 🔎 Support Inline Search

## Heroku Deployment 💜
The easy way to host this bot, deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/aryazakaria01/CBMusicBot)

## Railway Deployment 🚄
For deployment on railway you can see the full of [Necessary Variables Here](https://github.com/aryazakaria01/CBMusicBot/blob/main/example.env), make sure you fill all of it.

[![Deploy+on+Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/aryazakaria01/CBMusicBot&envs=SESSION_NAME,BOT_TOKEN,BOT_USERNAME,BOT_NAME,GROUP_SUPPORT,ASSISTANT_NAME,OWNER_NAME,OWNER_ID,DATABASE_URL,LOG_CHANNEL,BROADCAST_AS_COPY,BG_IMAGE,UPDATES_CHANNEL,API_ID,API_HASH,PMPERMIT,SUDO_USERS,DURATION_LIMIT,THUMB_IMG)

## Deploy On VPS 💜

- `sudo apt update && apt upgrade -y`
- `sudo apt install git curl python3-pip ffmpeg -y`
- `pip3 install -U pip`
- `curl -sL https://deb.nodesource.com/setup_16.x | bash -`
- `sudo apt-get install -y nodejs`
- `npm i -g npm`
- `git clone https://github.com/aryazakaria01/CBMusicBot` # Clone your repo.
- `cd CBMusicBot`
- `pip3 install -U -r requirements.txt`
- `cp example.env .env` #Use vim to edit ENVs
- `vim .env` #Fill up your ENVs ( Steps press `i` to enter in insert mode then edit the file. Press `Esc` to exit the editing mode then type `:wq!` and press `Enter` key to save the file.)
- `python3 main.py` # Run the bot

### Special Credits 💖
- [Arya Zakaria](https://github.com/aryazakaria01): Dev
- [Laky](https://github.com/Laky-64) & [Andrew](https://github.com/AndrewLaneX): PyTgCalls
- [Original Repo](https://github.com/callsmusic/callsmusic) CallsMusic
- [Cyber Music Bot](https://t.me/CyberMusikBot) Our Music Bot
- [RojSerBest](https://github.com/rojserbest) CallsMusic Developer
- [TeamDaisyX](https://github.com/TeamDaisyX) for base code

### Support & Updates 🎑
<a href="https://t.me/CyberSupportGroup"><img src="https://img.shields.io/badge/Join-Group%20Support-blue.svg?style=for-the-badge&logo=Telegram"></a> <a href="https://t.me/CyberMusicProject"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
