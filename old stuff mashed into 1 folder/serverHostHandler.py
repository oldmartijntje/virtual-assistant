def start_server_host_handler(activeThreadStopper):
    import socket
    import select
    import json
    import random
    import setup
    import shared.defaultFunctions as defaultFunctions
    from shared.logger import logger

    logger.info('Starting server host handler...')
    settings = setup.readJson("configuration/settings.json")
    PORT = settings["async"]["network"]["server"]["port"]
    IP = socket.gethostbyname(socket.gethostname())

    # create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind the socket to a public host and port
    server_socket.bind((IP, PORT))

    # listen for incoming connections
    server_socket.listen(5)

    # list of sockets for select.select()
    sockets_list = [server_socket]

    # dictionary to keep track of connected clients and their data
    clients = {}

    # count the number of messages received
    message_count = 0

    print(f"Listening for connections on {IP}:{PORT}...\n")

    while not activeThreadStopper.stopped:
        # select.select() returns a list of sockets that are ready to be read from
        read_sockets, _, _ = select.select(sockets_list, [], [])

        for notified_socket in read_sockets:
            # if a new connection is received, accept it and add it to the list of sockets
            if notified_socket == server_socket:
                client_socket, client_address = server_socket.accept()
                sockets_list.append(client_socket)
                clients[client_socket] = client_address
                print(f"Accepted new connection from {defaultFunctions.hide_ip_address(client_address)}")

            # if an existing client has sent data, receive it and process it
            else:
                try:
                    # receive data from the client
                    data = notified_socket.recv(1024)
                    if data:
                        # parse the JSON data
                        message = json.loads(data.decode('utf-8'))
                        print(f"Received message from {defaultFunctions.hide_ip_address(clients[notified_socket])}: {message['message']}")
                        message_count += 1

                        # send a response back to the client
                        response = {"message": "message accepted"}
                        notified_socket.send(json.dumps(response).encode('utf-8'))

                        # if we have received 5 messages, send a message to a random client
                        if message_count == 5:
                            message_count = 0
                            random_socket = random.choice(sockets_list[1:])
                            response = {"message": "yeee"}
                            random_socket.send(json.dumps(response).encode('utf-8'))
                            print("Sent yeee to a random client")

                    else:
                        # if no data is received, remove the socket from the list of sockets
                        sockets_list.remove(notified_socket)
                        del clients[notified_socket]
                        print(f"Connection closed from {defaultFunctions.hide_ip_address(client_address)}")

                except:
                    # if an error occurs, remove the socket from the list of sockets
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    print(f"Connection closed from {defaultFunctions.hide_ip_address(client_address)}")
