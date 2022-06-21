# Time Sync Server
Flask server responsible for managing all the clients publishing time to it, randomly picks a client master, and publishing the master time to all client every second.

In the even of the master not sending its time for 1 minute, the server will randomly pick a new master client and will publish it's time to all remaining clients.

## *Deply*
In order to deploy the server with different `host` and `port`, edit the [config.json](./config.json), then run:
```
python3 server.py
```

## *Implemented API*

```js
POST /time/
```
### parameters:
```json
{
    "client_ip": str,
    "client_time": str,
    "client_port": int
}
```

## *Logging*
All logs will be saved to [log.txt](./log.txt), the log file will be overwrite in every server restart.
