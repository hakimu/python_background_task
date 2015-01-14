This is a script I used to instrument a background job using the Python agent
-----------------------------------------------------------------------------

The key part is making sure to add the `startup_timeout` setting in the `newrelic.ini` config file under the `[newrelic]` section.

I ran the script with the following command:

```
python test.py
```
