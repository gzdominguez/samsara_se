#!/usr/bin/python
"""
This script retrieves and prints the temperature history data for
a sensor over a specified range.
To use it, run:
python sens_hist.py --b <BEGIN_TIME> --i <INCREMENT> --e<END_TIME>,
passing in sensor ID, begin time, increment size, and end time.
"""
from datetime import datetime
import calendar
import click
import samsara
import csv
from samsara.apis import SamsaraClient


@click.command()
@click.option('--b', type=int, required=True) #begin time
@click.option('--i', type=int, required=True) #increment size
@click.option('--e', type=int, required=True) #end time


def get_sensors_history(b, i, e):
    # Create an instance of the SamsaraClient.
    client = SamsaraClient()
    # Get a sensor's temperature history at specified range 
    # Values are multiplied by 1000 to get in ms
    end_ms = e*1000 
    step_ms = i
    start_ms = b*1000
    sensor_id = 212014918225862
    group_id = 25328
    series = [{"widgetId": sensor_id, "field": "ambientTemperature"}]
    fill_missing = "withNull"
    params = samsara.HistoryParam(group_id, start_ms, end_ms, step_ms, series, fill_missing)
    access_token = "dYmy4DpauFvADRPpwUxXA57HlvzsvM"
    history = client.get_sensors_history(access_token, params)
    #write results to csv
    with open('<path to csv folder should match M query>', mode='w') as temp_csv:
       temp_writer = csv.writer(temp_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
       for result in history.results:
            temp_writer.writerow([result.time_ms, result.series])


if __name__ == "__main__":
    get_sensors_history()
