import asyncio

uid = 1

async def handle_client(reader, writer):
    global uid
    player = 1 if uid&1 else 2
    uid+=1
    addr = writer.get_extra_info('peername')
    writer.write(str(player).encode())
    print(f"New connection from {addr}")
    while True:
        data = await reader.read(100)  # Read up to 100 bytes
        if not data:
            break

        message = data.decode().strip()
        print(f"Received from {addr}: {message}")
        response = f"Echo: {message}\n".encode()
        writer.write(response)
        await writer.drain()  # Ensure the data is written to the client

    print(f"Connection from {addr} closed.")
    writer.close()
    
    uid-=1

async def main(host, port):
    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')


    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    host = '192.168.43.97'  # Change this to your desired host
    port = 5000     # Change this to your desired port
    asyncio.run(main(host, port))
