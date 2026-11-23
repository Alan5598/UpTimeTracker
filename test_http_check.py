import asyncio

from app.checks.http_check import HTTPCheck


async def main():
    check = HTTPCheck(
        monitor_id="test-monitor-1",
        target="https://example.com",
        method="GET",
        expected_status_codes=[200],
        keyword="Example Domain",
        timeout_seconds=30,
    )

    result = await check.run()

    print(f"Status:        {result.status}")
    print(f"Response time: {result.response_time_ms}ms")
    print(f"Checked at:    {result.checked_at}")
    print(f"Error:         {result.error_message}")


asyncio.run(main())
