import socket
import json
import setup as setup
from shared.logger import logger
import shared.defaultFunctions as defaultFunctions

def split_ip_port(ip_port_str):
    settings = setup.readJson("configuration/settings.json")
    # Split the input string into IP address and port using the colon as the delimiter
    parts = ip_port_str.split(':')
    
    # If there are two parts, assume the first part is the IP address and the second part is the port
    if len(parts) == 2:
        ip_address = parts[0]
        port = int(parts[1])
    else:
        # Otherwise, use the input as the IP address and 1234 as the port
        ip_address = ip_port_str
        port = settings["async"]["network"]["client"]["port"]
    
    return ip_address, port

def start_client_connection_handler(activeThreadStopper):  
    settings = setup.readJson("configuration/settings.json")
    logger.info('Starting client connection handler...')

    server_ip, server_port = split_ip_port(settings["async"]["network"]["client"]["host"])

    tries = 0
    while not activeThreadStopper.stopped:
        tries += 1
        try:
            # Create a client socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((server_ip, server_port))
            tries = 0
            logger.info(f'Sucesfully connected to {defaultFunctions.hide_ip_address(server_ip)}:{server_port} after {tries} tries')
            # Define a function to send messages to the server
            def send_message():
                try:
                    # Ask the user for the message and recipient
                    message = input("Enter the message: ")

                    # Send the message to the server
                    message_data = {"message": message}
                    try:
                        client_socket.send(json.dumps(message_data).encode())
                    except ConnectionResetError as e:
                        logger.debug(f'ConnectionResetError: {e}\nTrying to reconnect...')
                except ValueError as e:
                    logger.error(f'ValueError: {e}\nProbably already exited...')

            while True:
                send_message()

                try:
                    # Check for any incoming messages from the server
                    message = client_socket.recv(1024).decode()
                    if message:
                        print(message)
                except ConnectionResetError as e:
                    logger.debug(f'ConnectionResetError: {e}\nTrying to reconnect...')
                    break
        except ConnectionRefusedError as e:
            if tries >= settings["async"]["network"]["client"]["retries"]:
                logger.error(f'ConnectionRefusedError: {e}\nMaximum retries reached: \'{tries}\', exiting...')
                break
            else:
                logger.debug(f'ConnectionRefusedError: {e}\nTried \'{tries}\' times, Trying again...')

        

        
