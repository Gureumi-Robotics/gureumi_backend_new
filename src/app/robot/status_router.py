import asyncio

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from app.robot.config import STATUS_SEND_INTERVAL_SECONDS
from app.robot.schemas import RobotConnectionStatus
from app.robot.service import RobotSignalState

router = APIRouter()


@router.websocket("/ws/robot-status")
async def provide_robot_status(websocket: WebSocket) -> None:
    state: RobotSignalState = websocket.app.state.robot_signal
    await websocket.accept()

    try:
        while True:
            message = RobotConnectionStatus(jetson_status=state.current_status())
            await websocket.send_json(message.model_dump())

            try:
                async with asyncio.timeout(STATUS_SEND_INTERVAL_SECONDS):
                    while True:
                        event = await websocket.receive()
                        if event["type"] == "websocket.disconnect":
                            return
            except TimeoutError:
                continue
    except (WebSocketDisconnect, OSError):
        return
