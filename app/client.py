from typing import Optional

from PySide2.QtWidgets import QMainWindow, QApplication
from app.design import Ui_MainWindow
import asyncio
from asyncio import transports
from asyncqt import QEventLoop


class ClientProtocol(asyncio.Protocol):
    transport: transports.Transport
    window: 'Chat'

    def __init__(self, chat):
        self.window = chat

    def data_received(self, data: bytes):
        decoded = data.decode()
        self.window.plainTextEdit.appendPlainText("Connect Succses, go login:YOUR_LOGIN")


    def connection_made(self, transport: transports.Transport):
        self.window.plainTextEdit.appendPlainText("Connect Succses, go login:YOUR_LOGIN")
        self.transport = transport

    def connection_lost(self, exception):
        self.window.plainTextEdit.appendPlainText("You disconnected!")


class Chat(QMainWindow, Ui_MainWindow):
    protocol: ClientProtocol

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.send_massage)

    def send_massage(self):
        message = self.lineEdit.text()
        self.lineEdit.clear()
        self.protocol.transport.write(message.encode())

    def create_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    async def start(self):
        self.show()
        loop = asyncio.get_running_loop()

        coroutine = loop.create_connection(
            self.create_protocol,
            "127.0.0.1",
            8888
        )

        await asyncio.wait_for(coroutine, 1000)


app = QApplication()
loop = QEventLoop(app)

asyncio.set_event_loop(loop)

window = Chat()

loop.create_task(window.start())
loop.run_forever()


