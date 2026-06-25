#!/bin/bash
CRON_JOB="0 3 * * * cd /home/qumin/discord/data-collector && python3 main.py >> /home/qumin/discord/data-collector/output/cron.log 2>&1"
(crontab -l 2>/dev/null | grep -v "data-collector"; echo "$CRON_JOB") | crontab -
echo "Cron job registered: daily at 3:00 AM"
