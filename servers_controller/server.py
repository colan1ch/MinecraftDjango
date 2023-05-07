import asyncio
import os
from threading import Thread
from fastapi import FastAPI, WebSocket, HTTPException, status, Request
import servers_manager

app = FastAPI()
app.last_id = servers_manager.get_last_server_id() + 1

AUTH_KEY = os.environ.get('AUTH_KEY', 'fc390cc01bcbe4583154c8316e4f953f')
# а это папка уже в докере
BASE_DIR = os.getcwd()


def check_key(key):
    if key != AUTH_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
        )


@app.get('/create_server/')
def create_server(key, request: Request):
    check_key(key)
    params = dict(request.query_params)
    print(params)
    server_id = servers_manager.create_server(app.last_id, params)
    app.last_id += 1
    return server_id


@app.get('/start_server/{server_id}')
def start_server(server_id: str, key):
    check_key(key)
    thread = Thread(
        target=servers_manager.start_container_by_id, args=(server_id,))
    thread.start()
    return 'Success'


@app.get('/stop_server/{server_id}')
def stop_server(server_id: str, key):
    check_key(key)
    thread = Thread(target=servers_manager.stop_container_by_id,
                    args=(server_id,))
    thread.start()
    return 'Success'


@app.get('/restart_server/{server_id}')
def restart_server(server_id: str, key):
    check_key(key)
    thread = Thread(
        target=servers_manager.restart_container_by_id, args=(server_id,))
    thread.start()
    return 'Success'


@app.get('/delete_server/{server_id}')
def delete_server(server_id: str, key):
    check_key(key)
    response = servers_manager.delete_container_by_id(server_id)
    if response == 0:
        return 'Success'
    return 'Error'


@app.get('/run_command/{server_id}')
def run_command(server_id: str, command: str, key):
    check_key(key)
    response = servers_manager.run_command_on_server(server_id, command)
    return response


@app.get('/edit_server/{server_id}')
def edit_server(server_id, key, request: Request):
    check_key(key)
    params = dict(request.query_params)
    return servers_manager.edit_server(server_id, params)


@app.websocket('/ws/log/{server_id}')
async def websocket_endpoint(websocket: WebSocket, server_id):
    await websocket.accept()
    try:
        while True:
            logs = await all_log_reader(server_id)
            await websocket.send_text(logs)
            await asyncio.sleep(0.1)  # без этого сервер падает (почему - это не ко мне)
    except Exception as exception:
        print(exception)
    finally:
        await websocket.close()


async def all_log_reader(server_id):
    log_lines = []
    file_path = f'{BASE_DIR}/servers_data/' \
                f'{servers_manager.get_container_name(server_id)}/logs/latest.log'
    try:
        with open(file_path, encoding='utf-8') as file:
            for line in file.readlines():
                log_lines.append(f"<p>{line}</p>")
    except:
        pass
    return log_lines
