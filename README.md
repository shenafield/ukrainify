# Ukrainify

A discord bot capable of adding an overlay (originally the outline of the ukrainian flag) to your avatar

# Usage
Make sure you know how to use the command line and have both git and python installed

First, obtain a discord bot token ([guide](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token))
Clone the repo:
```sh
git clone git@github.com:shenafield/ukrainify.git
cd ukrainify
```
Install the dependencies:
```sh
pip install -r requirements.txt
```
Start the bot:
```sh
python ukrainify.py
```

# Using in your own project
You can also add this as a cog for your existing bots. For now I haven't yet set it up properly (and I don't know if I ever will because I'm more lazy than you'd think) so just copy the file into your project, and then use:
```python
from ukrainify import UkrainifyCog
...
bot.add_cog(UkrainifyCog(bot))
...
```
