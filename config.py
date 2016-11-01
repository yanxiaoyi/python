from soa.config_manager import register
from component.resource_comp import FlightResource
# rest api setting
base_url = 'base_url'

# soa setting
soa_base_url = 'service_url'
flight_resource = {
    'base_url': soa_base_url,
    'service_url': 'soa_base_url',
    "account_id": "33800a57-edd3-427f-979d-83095b8b11fd",
    'version': '1.0.0.0',
    'component_version': '201204261002',
    'method_version': 1
}
register(flight_resource, FlightResource)
