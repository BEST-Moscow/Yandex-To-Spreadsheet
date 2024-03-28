## **Hello, Yandex Forms user!**

If you've ever had problems with non-existent auto-updated tables for yandex form answers like Google Spreadsheet for
Google Forms, this script
will be **very** helpful!

## **API**:

**URL**: http://`URL_of_your_host_machine`:5000/

**Method**: POST

**Body**: Json data

**Head**: Content-Type: application/json

## Requirements

1. Something you can **host** this script on to **receive requests** for it
2. Spreadsheet ID
3. Google API OAuth 2.0 **token**
4. The name of the List in your Sheet
5. `Integration` in your Yandex Form

# Let's start point by point

## What you need to use this script

### Host-machine

For example, it could be your PC, or for a more advanced level, a cloud service, but the main function this machine
should have is the ability to `receive requests`

---
### Spreadsheet ID

A spreadsheet ID can be extracted from its URL

For example, the Spreadsheet ID in the URL https://docs.google.com/spreadsheets/d/abc1234567/edit#gid=0 is `abc1234567`

---
### Google API OAuth 2.0 token

All tokens for the Google API must be stored in the `tokens` directory

You must have `token.json` from Google API OAuth 2.0

Your can create and download this token at https://console.cloud.google.com/

On the credentials page, create an **OAuth** token for the `Desktop version`, and then download it

Then rename this file to `token.json` and put it in the `tokens` directory (_don't forget to remove the_ `test-token.json`)

---
### The name of the List in your Sheet

Just look at the name of the sheet in your table

### `Integration` in your Yandex Form

1. Go to the `Integration` page of Form
2. Add `Request by specified method` to your `Action Group`
3. Fill in the fields, according to the API above
4. To get **all** answers in one json you can use yandex variable - `Answers to questions` with answer
   formatting - `JSON`

   [Read more about yandex variables](https://yandex.cloud/en/docs/forms/vars?utm_referrer=https%3A%2F%2Fwww.google.ru%2F])

---
## Download and setup

1. To fast download _(you probably know that)_  you can use:

```git
git clone <url_of_this_repository>
```

2. Then go to the repository main directory

3. Write your variables in `.env`, like in an example below

```.dotenv
SPREADSHEET_ID=<ID_OF_YOUR_SHEET>

LAST_LETTER_OF_COL=M

FIRST_LETTER_OF_COL=A

SHEET_LIST_NAME=Sheet1
```

4. Please update your `package-manager` and install all requirements from `requirements.txt`

```commandline
For Python 3.4 or later:
python -m pip install --upgrade pip

pip install -r requirements.txt
```

5. If you have `token.json` in the `tokens` directory, run `service.py` in **scripts/googleApi**, to create
   an `api-token.json` for Google Api OAuth operations _(this will
   be our final token)_


6. Check the number in the `id.txt` file, this is the line number to which the data will be added


7. If you want to use the **wsgi** server, run:

```commandline
gunicorn -b 0.0.0.0:5000 wsgi:app
```

8. If not, run in the `scripts` directory:

```commandline
flask run
```

### Excellent! Our app should work!
 If not, please create a new issue in Issues of our GitHub repository
