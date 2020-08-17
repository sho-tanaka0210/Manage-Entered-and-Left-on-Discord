# Discord's VC entry/exit notification tool
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

:jp: [日本語](./README.ja.md)

NOTE: This README has been translated using [DeepL](https://www.deepl.com/translator).

In the Discord server where this BOT is installed, the Posting a user name to the specified channel when Entering and exiting to voice chat.  
![Example](https://raw.github.com/wiki/mizukichi0210/Manage-Entered-and-Left-on-Discord/example_gif.gif)  
There are so many members who are voice chatting, you can't tell who's in and who's out!  
I can't be bothered to tell you I'm in! Why don't you try to introduce it when you have a problem?

## How to use

There are several patterns of usage.  
There are two patterns, one using [heroku](#Operation-in-heroku) and the other using [local execution](#local-execution).

### Operation in heroku

#### Assumptions

If you want to keep the BOT running 24 hours a day, you will need to register a credit card with heroku.  
However, because it fits into the free frame as long as you don't run paid add-ons and other applications at the same time, you can use it.  
If you follow the steps below, there is no charge.

For more information on rates, please visit [official page](https://heroku.com/pricing).  
FYI: The author's 70-person server is fully covered by Free

### Implementation Procedure

#### Assumptions
- You must have a GitHub account
- Must have an approved Heroku account.
- Discord server administrator privileges
- Discord's developer mode

The above steps are skipped.

#### Procedure
There are ways to use the Heroku CLI and deploy using Container Registory, but  
The following describes how to deploy using the GitHub repository.

1. Clone the repository  
`git clone https://github.com/Mizukichi0210/Manage-Entered-and-Left-on-Discord.git`.

2. Create a new repository in your account

I recommend that you make it a private repository.

3. Push rewriting the information of the remote repository

```bash
# Remote repository information immediately after git clone
$ git remote -v
origin https://github.com/Mizukichi0210/Manage-Entered-and-Left-on-Discord.git (fetch)
origin https://github.com/Mizukichi0210/Manage-Entered-and-Left-on-Discord.git (push)

# Set up the newly created repository to origin
$ git remote set-url origin https://github.com/UserName/RipositoryName.git
$ git remote -v
origin https://github.com/UserName/RipositoryName.git (fetch)
origin https://github.com/UserName/RipositoryName.git (push)

# Pushing to the newly created repository
$ git push origin -u master
Counting objects: 100% (187/187), done.
Counting objects: 100% (187/187), done.
Delta compression using up to 16 threads
Compressing objects: 100% (126/126), done.
Writing objects: 100% (187/187), 34.71 KiB | 8.68 MiB/s, done.
Total 187 (delta 82), reused 134 (delta 55)
remote: Resolving deltas: 100% (82/82), done.
To https://github.com/UserName/RipositoryName.git
 * [new branch] master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

4. Set up the app on the Heroku side

You should be able to complete the configuration by following the steps below.

- Log in to [Heroku](https://id.heroku.com/login)
- Go to [Dashboard - Apps List](https://dashboard.heroku.com/apps)
- Choose `New` -> `Create new app`.
- Enter the `App name`.
- Select `Choose a region`, then `Create app`.  
Either is acceptable as there are only `United States` or `Europe`.
- Select the `Deployment method` and the repository as shown in the following image

<img width="1281" alt="Screenshot 2020-06-03 3 02 55" src="https://user-images.githubusercontent.com/37664176/83553813-c0d99480-a546-11ea-92d6-30500db4eddd.png">

In `App connected to GitHub`, you can press the `Search` button and your repository will be shown.  
Therefore, please select the new repository that you created in 2.

5. Environment variable settings

For this BOT, it is necessary to set some environment variables in the execution.

Here is an overview of the environment variables required for execution

Environment variable name | Summary
POST_CHANNEL_ID | :--:
POST_CHANNEL_ID | ID of the channel to post access to the room.
TOKEN | TOKEN to start the BOT

How to set environment variables in Heroku

- Go to `https://dashboard.heroku.com/apps/AppName/settings`.
- Add the above environment variable names (KEY) and necessary information (VALUE) in `Config Vars`.

This completes the setup.

If it doesn't start, please create an Issue.

### Running on local execution

**DEPRECATED**

Use the following procedure.

```bash
# git clone
$ git clone git@github.com:Mizukichi0210/Manage-Entered-and-Left-on-Discord.git

$ cd Manage-Entered-and-Left-on-Discord

# Set the information required for the ENV of the Dockerfile.
## Configuration Parameters
## {SERVER_TOKEN}: server token
## {POST_CHANNEL_ID}: Message posting channel

# Creating an execution environment
$ docker build . . -t bot-run-image

# Execution
$ docker run --rm --name bot-run-container -v $(pwd):/discord_bot -it bot-run-image /bin/ash
```

If the configuration is successful, BOT will be activated and messages will be posted to the designated channel when entering/exiting any voice chat.

# Version

I'll update from time to time.

Item | version
-- | --
Python | 3.7.5
[discord.py](https://discordpy.readthedocs.io/en/latest/) | 1.2.5

# Usage

This program assumes operation with heroku.  
Please clone the source code.

## How to use

```bash
# git clone
$ git clone git@github.com:Mizukichi0210/Manage-Entered-and-Left-on-Discord.git

$ cd Manage-Entered-and-Left-on-Discord

# Create config.ini
# Set token and channel id
$ cp -p config_example.ini config.ini

# Generate docker image
$ docker build . -t bot-run-image

# Run
$ docker run --rm --name bot-run-container -v $(pwd):/discord_bot -it bot-run-image /bin/ash
```

# Reference
[dockerで簡易にpython3の環境を作ってみる](https://qiita.com/reflet/items/4b3f91661a54ec70a7dc)

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

[Compose file version 3 reference](https://docs.docker.com/compose/compose-file/)

[Discordで通話時間を測定するBotを作ってみた](https://qiita.com/tokkq/items/311aa297175b9cf7f946)

# LICENSE
MIT

-----

Translated with www.DeepL.com/Translator (free version)
