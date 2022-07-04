# applio-python-integration
A implementation of the appli data api in python

## Install
```text
$ pip install -r requirements.txt
```

## Use

This package exports the following identifiers: `franc`, `francAll`.
There is no default export.

```python
import applio

client = applio.ApplioClient(token)
devices = applio.devices(client)
measurements = applio.device_measurement_list(client, devices[0].id)
```

## Example
```text
# Create a .env file with TOKEN='{token}' variable (replace {token} with your applio api key)
$ python3 ./example.py
```
