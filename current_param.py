"""
current_param.py retreives sensor data at the time of request
The user can request temperature, humidity or the door status
the script is ran in the following format:
python current_param --param <PARAMETER>
where <PARAMETER> argument can be replaced with 't' , 'h'
input t for temperature
input h for humidity
"""
from __future__ import print_function
import time
import samsara
from samsara.rest import ApiException
from pprint import pprint
import click


#process command args
@click.command()
@click.argument('--param', type=str, required=True)
def get_params(param):
    temp_sensor_id = [212014918225862]
    door_sensor_id = [212014918374028]
    group_id = 25328
    access_token = "dYmy4DpauFvADRPpwUxXA57HlvzsvM"
    api_instance = samsara.SensorsApi()
    
	#switch case to determine which function call
    switch_sens = {
        t: temp,
        h: humi,
    }
	#plot temperature function
    def temp():
        sensor_id = temp_sensor_id
        sensor_param = samsara.SensorParam(group_id, ensor_id)
        while True:
            try:
                api_response = api_instance.get_sensors_temperature((access_token, sensor_param)
                pprint(api_response.sensors)
                time.sleep(4)
            except ApiException as e:
                print("Exception: %{}\n".format(e))

    #plot humidity function
    def humi():
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
