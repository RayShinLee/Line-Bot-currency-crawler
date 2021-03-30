
# Line-bot-currency-crawler

## install Line-bot-SDK
```
pip install line-bot-sdk
```

## 
Reference code - [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python), will be using [Heroku](https://www.heroku.com/) to set up environment.

## Files

|File name|purpose|
|-|-|
|app.py|Linebot main file, Flask main code|
|Procfile|The execution file. Heroku will execute the command `python app.py` written in this file to execute the main file|
|requirements.txt|environment requirements|
|readme.md|description file|
|.gitignore|Lists the files that you don't want to be recorded by git|

## Environment requirements

1. Install line-bot-sdk `pip install line-bot-sdk`
2. Install [Git](https://git-scm.com/)
3. Create a [Heroku] account(https://dashboard.heroku.com/) and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
4. Create a Line developers account [LineDevelopers](https://developers.line.me/en/), and create a channel.
5. Enable Webhook and obtain Channel Secret and Access Token.
6. Enter Channel Secret and Access Token to the location specified in the app.py file.
7. Deploy project to Heroku.

### 1. Install Git

Git website - [Git Official website](https://git-scm.com/) download and install Git.

enter commands below in Terminal after Git is installed：
```
git config --global color.ui true
git config --global user.name 
git config --global user.email 
```

### 2. Sign up to Heroku and install Heroku CLI

1. Go to [Heroku](https://dashboard.heroku.com/) and create an account.
2. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
3. Open Terminal and enter `heroku login` to login Heroku.

### 3. Sign up to Line developers, and create a channel for your line bot.

1. Go to [Line developers](https://developers.line.me/en/), select *Start using messaging API* and use Line account to login.
2. create or choose a Provider.
3. create a channel and enter all relevant info.

### 4. Enable Webhook and obatin Channel Secret and Access Token
1. Select your line bot account and go to Basic settings.
2. In basic settings, you would see Channel Secret，and Access Token in Messaging API.
3. Enter Channel Secret and Access Token to the location specified in the app.py file.
4. Enable Use webhooks, rewrite the Webhook URL to `your-heroku-project-name.herokuapp.com/callback`

## Deploy project to Heroku

### 1. Create a Heroku app

Go to [Heroku Dashboard](https://dashboard.heroku.com/apps) and select the upper rightcorner new -> Create new app.

### 2. Use git to deploy project to Heroku

In the project folder, open Terminal and enter the following commands：

```
git init
git add .
git commit -m "initial commit"
heroku git:remote -a Project-name-on-heroku
git push heroku master
```

## Update project to Heroku.

```
git add .
git commit -m "comment on changes made"
git push heroku master
```
