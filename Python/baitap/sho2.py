import nmap
# Synchronous
nm = nmap.PortScanner()
# nm.scan(‘ip/range’,’port_list’)
results = nm.scan('123.30.151.72')
