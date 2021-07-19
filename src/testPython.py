import paramiko

from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# please, change this!
token = INFLUX_TOKEN
org = INFLUX_ORG
bucket = INFLUX_BUCKET
client = InfluxDBClient(url="http://localhost:8086", token=token)

def getlinux(ssh):
    # executing command
    stdin, stdout, stderr = ssh.exec_command(r"free |awk 'NR==2{print (1-($7/$2))*100}'")
    err = stderr.readlines()
    if len(err) > 0:
        return err
    else:
        stdout_content = stdout.readlines()
    result = stdout_content
    if len(result) == 0:
        print("there is something wrong when executing free -m")
    else:
        return round(float(result[0].strip()),2)

if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # please, change here!
    ssh.connect(hostname='000.000.000.000', username = 'centos', key_filename='test.pem')
    result = getlinux(ssh)

    write_api = client.write_api(write_options=SYNCHRONOUS)    
    point = Point("mem")\
        .tag("host", "test-host")\
        .field("memory", result)\
        .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)
    ssh.close()
    print(str(result)+"% used")