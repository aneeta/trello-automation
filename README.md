# trello-automation
Scripts to organise study boards.

Shifts cards to appropriate lists based on due date.

## Board Setup
Requires the board to have the following lists:
- Today
- Tomorrow
- This Week
- Backlog
- Classes
- lists for individual classes (corresponsing to the cards in Classes list)

Order unimportant.

## Run
Example:
```console
(base) AnetasMacBook2:trello-automation anetaswianiewicz$ python clean.py --key="[YOUR KEY]" --token="[YOUR TOKEN]" --board="[YOUR BOARD ID]"
```
### Get key and token
Can be found <a href="https://trello.com/app-key">here</a>.
### Get board ID
Your board ID will be the given in the board URL. 
```
https://trello.com/b/jiYHdSjp/sample-board
```
The board ID for <b>Sample Board</b> is <b>jiYHdSjp</b>
