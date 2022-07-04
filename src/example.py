from dotenv import load_dotenv
import os
import applio

load_dotenv()

def main():
    token = os.environ.get('TOKEN')

    client = applio.ApplioClient(token)

    # Get all devices
    devices = applio.devices(client)
    print(devices[0].id)
    print(devices[0].name)

    # Get the latest sensor data from the provided device 
    device_latest = applio.device_latest(client, devices[0].id)
    print(device_latest)

    # Get a list of all the measurements the for the given device
    measurements = applio.device_measurement_list(client, devices[0].id)
    print(device_latest)

if __name__ == '__main__':
    main()