#!/bin/sh
cd /root/kuaishou_server || exit

# shellcheck disable=SC2161

while [ 1 ]
do
        sleep 3600
        # shellcheck disable=SC2043
        for name in manage.py
        do
                # shellcheck disable=SC2009
                # shellcheck disable=SC2126
                count=$(ps -ef|grep $name|grep -v grep|wc -l)
                time=$(date "+%Y-%m-%d %H:%M:%S")

                if [ "$count" -eq 0 ]
                then
                        echo "${time}"    $name start process.....  >> /root/kuaishou_server/logs/run.log
                        nohup /usr/bin/python3  /root/kuaishou_server/$name >/dev/null 2>&1 &
                else
                        echo "${time}"    $name runing.....  >> /root/kuaishou_server/logs/run.log
                fi
        done

done