Bittrex unofficial Python API
==============================

# Installation
* pip install requests
# Usage Example

```python
import bittrex

bittrex.market = "eth" #This is eth by default.

js = bittrex.get_update() #This returns a list with all the values from the json. Do this to save multiple calls to api for each value.

high = bittrex.get_value("high", js) #Second argument is optional, just saves a call to the api if you've stored api json already.
last = bittrex.get_value("last") #Just an example to show that second argument isn't needed.

print("High:" + str(high))
print("Last:" + str(last))

if (last * 1.5) > high:
    print("Last is 1.5x larger than the highest in last 24 hrs. Perhaps sell?")

```
