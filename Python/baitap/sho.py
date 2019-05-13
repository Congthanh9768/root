import shodan

SHODAN_API_KEY = "M2Qw35dw379AMRxggSkxUlwFTM4ECRV2"

api = shodan.Shodan(SHODAN_API_KEY)

host = api.host('189.1.240.225')

# Print general info
print("""
        IP: {}
        Organization: {}
        Operating System: {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

# Print all banners
for item in host['data']:
    print("""
                Port: {}
                Banner: {}

        """.format(item['port'], item['data']))
