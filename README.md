# Telegram SMART Goal Bot

## Windows

```
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
python smart_goal_bot.py
```

## Mac

```
virtualenv venv
source venv\bin\activate
pip install -r requirements.txt
python smart_goal_bot.py
```

Once the application is running, open the Telegram app and search @smart_goal_bot. Then, issue the command `/start`. To evaluate your goal, send it to the bot in a message starting with `/goal`. 


## Description

The Telegram bot uses a scikit-learn ensemble classifier model to decide whether a particular goal is specific, measurable, action-oriented, or time-bound. It assumes the goal is relevant for each user.

<img width="679" alt="image" src="https://github.com/polinavishnev/SMAT-Goal-Telegram-Bot/assets/68515140/657206d7-5efb-4ff1-ad63-df23d4136a1b">

The code for the random forest classifier model can be found in `smat_classifier.py` file while the basic Telegram app is found in the `smart_goal_bot.py`. 
