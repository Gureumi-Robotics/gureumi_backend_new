from json import JSONDecodeError

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from pydantic import ValidationError

from app.robot.schemas import JetsonHeartbeat
from app.robot.service import RobotSignalState

router = APIRouter()


@router.websocket("/ws/robot")
async def receive_robot_signal(websocket: WebSocket) -> None:
    state: RobotSignalState = websocket.app.state.robot_signal
    await websocket.accept()

    try:
        while True:
            try:
                data = await websocket.receive_json()
                signal = JetsonHeartbeat.model_validate(data)
            except (JSONDecodeError, KeyError, ValidationError):
                continue

            state.record(signal)
    except WebSocketDisconnect:
        return
