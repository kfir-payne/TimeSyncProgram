# Time Sync Client
Flask server that sends his time every minute to the time sync server, and receives the master time from the server, if provided.

## *Deply*
In order to deploy the client a `host` and `port` must be provided via argument variables, for example:
```
python3 client.py 127.0.0.1 5001
```

## *Implemented API*

```js
POST /time/
```
### parameters:
```json
{
    "master_time": str,
    "master_ip": str
}
```

## *Logging*
All logs will be saved to [log.txt](./log.txt), the log file will be overwrite in every client restart.
