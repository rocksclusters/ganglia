#!/bin/bash
#
# Runs the ganglia news cooker at startup. If we leave it
# for once-daily, the link will be broken on first boot.

/etc/cron.hourly/ganglia-news
