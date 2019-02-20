#!/usr/bin/python
"""
This script retrieves and prints the temperature history data for
a sensor over a specified range.
To use it, run:
./examples/sensors_history --t <TEMP_TYPE> --b <BEGIN_TIME> --i <INCREMENT> --e<END_TIME>,
passing in sensor ID, begin time, increment size, and end time.
Next steps: 
1. print the data to a csv.
2. process temp type arg to determine temperature type (probe or ambient)
"""
from datetime import datetime
import calendar
import click
import samsara
from samsara.apis import SamsaraClient


@click.command()
@click.option('--t', type=str, required=True) #sensor ID
@click.option('--b', type=int, required=True) #begin time
@click.option('--i', type=int, required=True) #increment size
@click.option('--e', type=int, required=True) #end time


def get_sensors_history(t, b, i, e):
    # Create an instance of the SamsaraClient.
    client = SamsaraClient()
    # Get a sensor's temperature history at specified range 
	# Values are multiplied by 1000 to get in ms
    end_ms = e*1000 
    step_ms = i
    start_ms = b*1000
    sensor_id = 212014918225862
    group_id = 25328
    series = [{"widgetId": sensor_id, "field": "probeTemperature"}]
    fill_missing = "withNull"
	
    params = samsara.HistoryParam(group_id, start_ms, end_ms, step_ms, series, fill_missing)
	access_token = "dYmy4DpauFvADRPpwUxXA57HlvzsvM"
    history = client.get_sensors_history(access_token, params)
    for result in history.results:
        print '\ntimestamp: {}, series: {}'.format(result.time_ms, result.series)


if __name__ == "__main__":
    get_sensors_history()

