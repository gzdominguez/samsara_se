"""
current_param.py retreives real-time sensor data 
and refreshes every 4 seconds until the user 
stops the script by pressing CTRL+C
The user may request sensor temperature or humidity
The script is ran in the following format:
python current_param --p <PARAMETER>
where <PARAMETER> argument can be replaced with 'temp' , 'hum'
input temp for temperature
input hum for humidity
"""
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
import click

#process command args
@click.command()
@click.option('--p', type=str, required=True)
def get_params(p):
	print("{}\n".format(p))
	temp_sensor_id = [212014918225862]
	door_sensor_id = [212014918374028]
	group_id = 25328
	access_token = "dYmy4DpauFvADRPpwUxXA57HlvzsvM"
	api_instance = samsara.SensorsApi()
	t = 'temp'
	h = 'hum'
	#plot temperature
	if p == t:
		sensor_id = temp_sensor_id
		sensor_param = samsara.SensorParam(group_id, sensor_id)
		while True:
			try:
				api_response = api_instance.get_sensors_temperature(access_token, sensor_param)
				pprint(api_response.sensors)
				time.sleep(4)
			except ApiException as e:
				print("Exception: %{}\n".format(e))
	if p == h:
		sensor_id = temp_sensor_id
		sensor_param = samsara.SensorParam(group_id, sensor_id)
		while True:
			try:
				api_response = api_instance.get_sensors_humidity(access_token, sensor_param)
				pprint(api_response.sensors)
				time.sleep(4)
			except ApiException as e:
				print("Exception: %{}\n".format(e))
		
if __name__ == "__main__":
    get_params()
