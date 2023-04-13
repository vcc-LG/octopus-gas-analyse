# Octopus monthly gas cost analysis

A simple python script for plotting out monthly gas cost totals where you don't have a gas smart meter.



## Installation

Install requirements:

```bash
pip3 install -r requirements.txt
```

## Usage

First you need to get the cost data (which isn't available over the octopus API) by going to:

```
https://octopus.energy/dashboard/new/accounts/<YOUR_ACCOUNT_NUMBER>/balance-history
```
and scrolling down the page to the start of your billing data. Then run the contents of `get_bill_data.js` in the console of the developer tools of the page.

Obviously this may change in the future with UI updates to this page. You'll get something like this returned:

```javascript
[{"start_date":"1 APR 2023","end_date":"8 APR 2023","value":"£37.21"},{"start_date":"30 MAR 2023","end_date":"31 MAR 2023","value":"£10.09"}...]
```

Save it as `data.json` in the repo directory and you're ready to go. I left some dummy data in the repo so you can play with it.

```bash
python3 main.py
```

And you should get something like this:


## License

[MIT](https://choosealicense.com/licenses/mit/)
