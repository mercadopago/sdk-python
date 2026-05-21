"""
    Tests package
"""
import time


def api_call_with_retry(fn, expected_status, retries=3, delay=5):
    """Call fn() up to `retries` times, returning the response once it matches
    expected_status. Returns the last response if all attempts are exhausted."""
    response = fn()
    for _ in range(retries - 1):
        if response.get("status") == expected_status:
            return response
        time.sleep(delay)
        response = fn()
    return response
