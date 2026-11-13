from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.robot.config import ROBOT_SIGNAL_TIMEOUT_SECONDS
from app.robot.jetson_router import router as jetson_router
from app.robot.service import RobotSignalState
from app.robot.status_router import router as status_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.robot_signal = RobotSignalState(
        timeout_seconds=ROBOT_SIGNAL_TIMEOUT_SECONDS
    )
    yield


app = FastAPI(title="Gureumi Backend", lifespan=lifespan)
app.include_router(jetson_router)
app.include_router(status_router)
