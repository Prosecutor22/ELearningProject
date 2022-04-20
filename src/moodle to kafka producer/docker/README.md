Run:
```bash
docker-compose build --no-cache && docker-compose up -d
```

Open Docker Desktop and check if `web` and `client` service is running. Sometimes they can't find Kafka brokers on first start.

## Moodle

1. Login to `localhost` with default username `user` and password `bitnami`
2. Go to [install plugins page](http://localhost/admin/tool/installaddon/index.php)
3. Use plugin zip file from [here](https://github.com/iceghost/moodle-logstore_xapi/releases/tag/v5.0.0-beta) and "continue" everything.
4. A settings site should show up. Setup the following on the settings page of that plugin:

   - Your LRS endpoint for the xAPI: `kafka:9092`
   - Send statements by scheduled task?: No
   - Maximum batch size: 0
   
   And save changes

5. Go to [Manage log stores](http://localhost/admin/settings.php?section=managelogging) and enable xAPI log store.