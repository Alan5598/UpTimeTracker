import asyncio
import time
from datetime import datetime, timezone

from app.checks.base import BaseCheck
from app.checks.result import CheckResult


class TCPCheck(BaseCheck):
    def __init__(
        self,
        monitor_id: str,
        target: str,
        timeout_seconds: int = 30,
    ):
        self.monitor_id = monitor_id
        host, port_str = target.rsplit(":", 1)
        self.host = host
        self.port = int(port_str)
        self.timeout_seconds = timeout_seconds

    async def run(self) -> CheckResult:
        checked_at = datetime.now(timezone.utc)
        start = time.monotonic()

        try:
            _, writer = await asyncio.wait_for(
                asyncio.open_connection(self.host, self.port),
                timeout=self.timeout_seconds,
            )
            response_time_ms = int((time.monotonic() - start) * 1000)
            writer.close()
            await writer.wait_closed()
            return CheckResult(
                monitor_id=self.monitor_id,
                status="up",
                response_time_ms=response_time_ms,
                checked_at=checked_at,
            )

        except asyncio.TimeoutError:
            response_time_ms = int((time.monotonic() - start) * 1000)
            return CheckResult(
                monitor_id=self.monitor_id,
                status="down",
                response_time_ms=response_time_ms,
                checked_at=checked_at,
                error_message=f"Connection timed out after {self.timeout_seconds}s",
            )

        except OSError as e:
            response_time_ms = int((time.monotonic() - start) * 1000)
            return CheckResult(
                monitor_id=self.monitor_id,
                status="down",
                response_time_ms=response_time_ms,
                checked_at=checked_at,
                error_message=str(e),
            )
