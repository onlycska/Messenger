"""
Серверное приложение для соединений
"""
import asyncio
from asyncio import transports


class ClientProtocol(asyncio.Protocol):
    login: str
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server
        self.login = None

    def data_received(self, data: bytes):
        decoded = data.decode()
        print(decoded)

        if self.login is None:
            if decoded.startswith("login:"):
                new_login = decoded.replace("login:", "").replace("\r\n", "")
                for client in self.server.clients:
                    if client.login == new_login:
                        self.transport.write(
                            f"Логин {new_login} занят, попробуйте другой".encode()
                        )
                        self.server.clients.remove(self)
                        break
                else:
                    self.login = new_login
                    self.transport.write(
                        f"Привет, {self.login}!".encode()
                    )
                    self.server.send_history(self.server.clients[-1])
        else:
            self.send_message(decoded)

    def send_message(self, message):
        format_string = f"<{self.login}> {message}"
        encoded = format_string.encode()
        self.server.append_new_message_to_history(new_message=encoded)
        for client in self.server.clients:
            if client.login != self.login:
                client.transport.write(encoded)

    def connection_made(self, transport: transports.Transport):
        self.transport = transport
        self.server.clients.append(self)
        print("Соединение установлено")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("Соединение разорвано")


class Server:
    clients: list
    last_messages = []

    def __init__(self):
        self.clients = []

    def create_protocol(self):
        return ClientProtocol(self)

    async def start(self):
        loop = asyncio.get_running_loop()

        coroutine = await loop.create_server(
            self.create_protocol,
            "127.0.0.1",
            8888
        )

        print("Сервер запущен ...")

        await coroutine.serve_forever()

    def append_new_message_to_history(self, new_message):
        self.last_messages.append(new_message)
        if len(self.last_messages) > 10:
            self.last_messages.pop(0)

    def send_history(self, client):
        if self.last_messages:
            client.transport.write(
                f"Последние ссобщения в чате ({len(self.last_messages)} шт.):\n".encode()
            )
            for message in self.last_messages:
                client.transport.write(message + "\n".encode())


process = Server()
try:
    asyncio.run(process.start())
except KeyboardInterrupt:
    print("Сервер остановлен вручную")
