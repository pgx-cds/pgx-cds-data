import json
import urllib.request

patient_ids = ['smart-1288992', 'smart-1032702', 'smart-1081332',
    'smart-1098667', 'smart-1134281', 'smart-1137192', 'smart-1157764',
    'smart-1186747', 'smart-1213208', 'smart-1272431', 'smart-1291938',
    'smart-1482713', 'smart-1520204', 'smart-1540505', 'smart-1551992',
    'smart-1557780', 'smart-1577780', 'smart-1614502', 'smart-1627321',
    'smart-1642068', 'smart-1685497', 'smart-1768562', 'smart-1796238',
    'smart-1869612', 'smart-1951076', 'smart-2004454', 'smart-2042917',
    'smart-2080416', 'smart-2081539', 'smart-2113340', 'smart-2169591']

patients = []
for id in patient_ids:
    patients.append({'resourceType': 'Patient', 'id': id})

for patient in patients:
    url = ('http://pgx-fhir.smarthealthit.org:8080/baseDstu2/' +
           patient['resourceType'] + '/' +
           patient['id'])
    req = urllib.request.Request(url=url,
    data=json.dumps(patient).encode('utf-8'),
    headers={'Content-Type': 'application/json'}, method='PUT')
    with urllib.request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
    print(f.status)
    print(f.reason)
