from typing import Literal

from pydantic import BaseModel, Field


class JetsonHeartbeat(BaseModel):
    jetson_status: int = Field(strict=True, ge=1, le=1)


class RobotConnectionStatus(BaseModel):
    jetson_status: Literal[0, 1]
