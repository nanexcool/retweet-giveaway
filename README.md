# retweet-giveaway

Get API keys at https://developer.twitter.com/en/portal/dashboard

Add your credentials to a `.env` file in the root directory

```
CONSUMER_KEY=your key
CONSUMER_SECRET=your secret
ACCESS_TOKEN=your access token
ACCESS_TOKEN_SECRET=your access token secret
```

These are instructions for Python 3 on Ubuntu.

Install dependencies with `python3`

```
pip3 install python-decouple
pip3 install tweepy
```

Modify `main.py` line `10` with your tweet `id`

Run with command

```
python3 main.py
```

You'll get a list of at most 100 usernames that retweeted.

If you want to choose a random amount you can pipe the output to `shuf`

```
python3 main.py | shuf -n 5 # gives you 5 winners
```
