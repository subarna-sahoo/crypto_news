# Crypto News

A Django website that shows **live cryptocurrency prices** and the **latest crypto news**, and lets you look up any coin by its symbol.

Data comes from the [CryptoCompare API](https://min-api.cryptocompare.com/).

## Features

- **Home page**: USD prices for the top coins (BTC, ETH, XRP, BCH, EOS, LTC, XLM, ADA, USDT, …) plus a news feed
- **Price lookup**: enter one or more symbols (for example `BTC,DOGE`) to see full market data

## Screenshots

**Home page**

![home](https://user-images.githubusercontent.com/48875593/75289077-8f647500-5843-11ea-80da-f6c7555eb587.png)

**Latest news**

![news](https://user-images.githubusercontent.com/48875593/75289090-94c1bf80-5843-11ea-8e4f-93481e6f2094.png)

**Price lookup**

![query](https://user-images.githubusercontent.com/48875593/75289085-925f6580-5843-11ea-9ad3-c4653e6068e4.png)

## Running locally

```bash
cd mysite
python -m venv venv && source venv/bin/activate
pip install django requests
python manage.py migrate
python manage.py runserver        # http://localhost:8000
```

`requirements.txt` pins Django 3.0 and includes `pkg-resources==0.0.0`, which is an Ubuntu artifact that pip can't install. Remove that line before running `pip install -r requirements.txt`.

## Routes

| Path | Description |
|---|---|
| `/` | Prices + news |
| `/prices/` | Look up by symbol (POST form) |

## Tech stack

Python · Django · requests · Bootstrap
