from dataclasses import dataclass
import requests
_base_url = "https://data.applio.tech/data"
_auth_header = "Grpc-Metadata-Authorization"

@dataclass
class ApplioClient:
    token: str

    def headers(self) -> dict:
        return {
            'Grpc-Metadata-Authorization': self.token,
            'accept': 'application/json'
            }

@dataclass
class Device:
    id: str
    name: str
    comment: str
    manufacturer: str
    model: str

def latest(client: ApplioClient) -> str:
    """returns all recent sensor data for given application"""
    res = requests.get(_base_url + '/application/latest', headers=client.headers())
    return res.json()

def devices(client: ApplioClient) -> list[Device]:
    """returns all device information for that application in an array"""
    res = requests.get(_base_url + '/application/devices',headers=client.headers())
    return [Device(**device) for device in res.json()]

def device_latest(client: ApplioClient, id: str) -> str:
    """returns all recent sensor data for given device"""
    res = requests.get(_base_url + f'/device/{id}/latest', headers=client.headers())
    return res.json()

def device_measurement_list(client: ApplioClient, id: str) -> list[str]:
    """returns an list of all measurement for given device"""
    res = requests.get(_base_url + f'/device/{id}/measurement/list', headers=client.headers())
    return res.json()