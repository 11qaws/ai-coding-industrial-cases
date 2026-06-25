#!/bin/bash
CRON_JOB="0 5 * * * cd /home/qumin/discord/deep-analyzer && python3 main.py >> /home/qumin/discord/deep-analyzer/output/cron.log 2>&1"
(crontab -l 2>/dev/null | grep -v "deep-analyzer"; echo "$CRON_JOB") | crontab -
echo "Cron job registered: daily at 5:00 AM"
