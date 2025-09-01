import argparse
import requests

server_url = "https://sendify-server.onrender.com/"

def main():
    parser = argparse.ArgumentParser(description="A basic CLI interface for sending messages.")
    parser.add_argument("name", help="Function to be called")
    parser.add_argument("--msg", type=str, help="Message to send", default=None)
    parser.add_argument("--token", type=str, help="Access token", default=None)

    args = parser.parse_args()

    if args.name == 'send':
        send(args.msg)
    
    if args.name == 'receive':
        receive(args.token)

def send(msg):
    response = requests.post(server_url+'/api/send_msg', json={'message':msg})
    if not response:
        raise "No response from the server"

    print(f"Access token generated: {response.json().get('response', None)}")

def receive(access_token):
    response = requests.post(server_url+f'/api/receive/{access_token}', json={'access_token':access_token})
    if not response:
        raise "No response from the server"
    
    if not response.json():
        print('Access token not found.')
    else:
        print(response.json()[0][1])


if __name__ == "__main__":
    main()
