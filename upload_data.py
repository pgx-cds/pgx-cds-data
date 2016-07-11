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

# Upload performer data
performer_path = ('/Users/gafiore/code/pgx-cds/examples/organizations/'
                  'acme-lab.json')
with open(performer_path, 'r') as f:
    performer = json.load(f)
performer_url = ('http://pgx-fhir.smarthealthit.org:8080/baseDstu2/' +
                 performer['resourceType'] + '/' +
                 performer['id'])
performer_req = urllib.request.Request(url=performer_url,
    data=json.dumps(performer).encode('utf-8'),
    headers={'Content-Type': 'application/json'}, method='PUT')
with urllib.request.urlopen(performer_req) as f:
    print(f.read().decode('utf-8'))
print(f.status)
print(f.reason)

patients = []
genotypes = []
phenotypes = []
tpmt_path = '/Users/gafiore/code/pgx-cds/examples/tpmt/'
for id in patient_ids:
    patients.append({'resourceType': 'Patient', 'id': id})
    genotype_path = tpmt_path + 'Observation-tpmtgenotype-' + id[6:] + '.json'
    with open(genotype_path, 'r') as f:
        genotypes.append(json.load(f))
    phenotype_path = tpmt_path + 'Observation-tpmtphenotype-' + id[6:] + '.json'
    with open(phenotype_path, 'r') as f:
        phenotypes.append(json.load(f))

for patient, genotype, phenotype in zip(patients, genotypes, phenotypes):
    patient_url = ('http://pgx-fhir.smarthealthit.org:8080/baseDstu2/' +
                   patient['resourceType'] + '/' +
                   patient['id'])
    patient_req = urllib.request.Request(url=patient_url,
        data=json.dumps(patient).encode('utf-8'),
        headers={'Content-Type': 'application/json'}, method='PUT')
    with urllib.request.urlopen(patient_req) as f:
        print(f.read().decode('utf-8'))
    print(f.status)
    print(f.reason)
    genotype_url = ('http://pgx-fhir.smarthealthit.org:8080/baseDstu2/' +
                    genotype['resourceType'] + '/' +
                    genotype['id'])
    genotype_req = urllib.request.Request(url=genotype_url,
        data=json.dumps(genotype).encode('utf-8'),
        headers={'Content-Type': 'application/json'}, method='PUT')
    with urllib.request.urlopen(genotype_req) as f:
        print(f.read().decode('utf-8'))
    print(f.status)
    print(f.reason)
    phenotype_url = ('http://pgx-fhir.smarthealthit.org:8080/baseDstu2/' +
                     phenotype['resourceType'] + '/' +
                     phenotype['id'])
    phenotype_req = urllib.request.Request(url=phenotype_url,
        data=json.dumps(phenotype).encode('utf-8'),
        headers={'Content-Type': 'application/json'}, method='PUT')
    with urllib.request.urlopen(phenotype_req) as f:
        print(f.read().decode('utf-8'))
    print(f.status)
    print(f.reason)
