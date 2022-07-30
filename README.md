
# Discord Stalker
 Stalk anyone's Discord activity
## How to use
1. Download and unzip the repo
2. Create a webhook in the channel you want the activity posted
3. Configure config.json, remember the UserID(s) is an array of ints. Refer to https://www.androidauthority.com/get-discord-token-3149920/ if you need assistance getting your token.
4. Install all needed libraries by running the following command:
```
pip install os-sys discord discord.py-self requests colorama asyncio
```
5. Now finally run the script with `py stalk.py`

## Disclaimer
This script automates Discord actions, which is against Discord's Terms of Service and may lead to account termination. In any case, I am not responsible for however you use this script.  This script was strictly created for educational purposes and should not be used for any other purpose.
