from __future__ import annotations

from typing import Any

from fastmcp import FastMCP

from babelwrap_mcp.client import StandaloneBackend

mcp = FastMCP("BabelWrap")

_backend = StandaloneBackend()


@mcp.tool()
async def babelwrap_new_session(metadata: dict | None = None) -> dict[str, Any]:
    """Create a new browser session for web interaction.

    Args:
        metadata: Optional labels or tags for this session.

    Returns:
        Dictionary with session_id string.

    Metadata:
        tier: core
        frequency: high
    """
    return await _backend.new_session(metadata)


@mcp.tool()
async def babelwrap_close_session(session_id: str) -> dict[str, Any]:
    """Close and clean up a browser session.

    Args:
        session_id: The session ID to close.

    Returns:
        Dictionary with success boolean.

    Metadata:
        tier: core
        frequency: high
    """
    return await _backend.close_session(session_id)


@mcp.tool()
async def babelwrap_navigate(session_id: str, url: str, compact: bool = False) -> dict[str, Any]:
    """Navigate to a URL and get a structured snapshot of the page.

    Args:
        session_id: The active session ID.
        url: The URL to navigate to.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the loaded page.

    Metadata:
        tier: core
        frequency: high
    """
    return await _backend.navigate(session_id, url, compact=compact)


@mcp.tool()
async def babelwrap_snapshot(session_id: str, compact: bool = False) -> dict[str, Any]:
    """Get the current page state as a structured snapshot without taking any action.

    Args:
        session_id: The active session ID.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the current page.

    Metadata:
        tier: standard
        frequency: medium
    """
    return await _backend.snapshot(session_id, compact=compact)


@mcp.tool()
async def babelwrap_click(session_id: str, target: str, compact: bool = False) -> dict[str, Any]:
    """Click an element on the page using a natural language description.

    Args:
        session_id: The active session ID.
        target: Natural language description of the element to click (e.g. "the Login button", "first search result"). TIP: Pass an element ID from a previous snapshot (e.g. "btn-login", "input-email") to bypass LLM resolution entirely for instant, deterministic targeting.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the page after clicking.

    Metadata:
        tier: core
        frequency: high
    """
    return await _backend.click(session_id, target, compact=compact)


@mcp.tool()
async def babelwrap_fill(
    session_id: str, target: str, value: str, compact: bool = False
) -> dict[str, Any]:
    """Fill an input field with a value.

    Args:
        session_id: The active session ID.
        target: Natural language description of the input field (e.g. "Email address field"). TIP: Pass an element ID from a previous snapshot (e.g. "input-email") to bypass LLM resolution entirely for instant, deterministic targeting.
        value: The value to fill in.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the page after filling.

    Metadata:
        tier: core
        frequency: high
    """
    return await _backend.fill(session_id, target, value, compact=compact)


@mcp.tool()
async def babelwrap_submit(
    session_id: str, target: str | None = None, compact: bool = False
) -> dict[str, Any]:
    """Submit a form on the current page.

    Args:
        session_id: The active session ID.
        target: Optional natural language description of which form to submit. If omitted, submits the most prominent form. TIP: Pass an element ID from a previous snapshot (e.g. "btn-submit") to bypass LLM resolution entirely for instant, deterministic targeting.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the resulting page.

    Metadata:
        tier: standard
        frequency: medium
    """
    return await _backend.submit(session_id, target, compact=compact)


@mcp.tool()
async def babelwrap_extract(session_id: str, query: str, compact: bool = False) -> dict[str, Any]:
    """Extract structured data from the current page using a natural language query.

    Args:
        session_id: The active session ID.
        query: Natural language description of what data to extract (e.g. "all product names and prices").
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Extracted data as a structured array plus page snapshot.

    Metadata:
        tier: core
        frequency: medium
    """
    return await _backend.extract(session_id, query, compact=compact)


@mcp.tool()
async def babelwrap_screenshot(session_id: str, compact: bool = False) -> dict[str, Any]:
    """Take a screenshot of the current page (for debugging).

    Args:
        session_id: The active session ID.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Base64-encoded PNG image of the current page.

    Metadata:
        tier: standard
        frequency: low
    """
    return await _backend.screenshot(session_id, compact=compact)


@mcp.tool()
async def babelwrap_press(session_id: str, key: str, compact: bool = False) -> dict[str, Any]:
    """Press a keyboard key on the current page.

    Args:
        session_id: The active session ID.
        key: The key to press (e.g. "Enter", "Tab", "Escape", "ArrowDown").
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the page after pressing the key.

    Metadata:
        tier: standard
        frequency: medium
    """
    return await _backend.press(session_id, key, compact=compact)


@mcp.tool()
async def babelwrap_upload(
    session_id: str, target: str, file_base64: str, filename: str, compact: bool = False
) -> dict[str, Any]:
    """Upload a file to a file input element on the page.

    Args:
        session_id: The active session ID.
        target: Natural language description of the file input element. TIP: Pass an element ID from a previous snapshot to bypass LLM resolution entirely for instant, deterministic targeting.
        file_base64: Base64-encoded file content.
        filename: The filename to use for the upload.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the page after uploading.

    Metadata:
        tier: advanced
        frequency: low
    """
    return await _backend.upload(session_id, target, file_base64, filename, compact=compact)


@mcp.tool()
async def babelwrap_hover(session_id: str, target: str, compact: bool = False) -> dict[str, Any]:
    """Hover over an element on the page.

    Args:
        session_id: The active session ID.
        target: Natural language description of the element to hover over. TIP: Pass an element ID from a previous snapshot to bypass LLM resolution entirely for instant, deterministic targeting.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the page after hovering.

    Metadata:
        tier: standard
        frequency: low
    """
    return await _backend.hover(session_id, target, compact=compact)


@mcp.tool()
async def babelwrap_back(session_id: str, compact: bool = False) -> dict[str, Any]:
    """Navigate back in the browser history.

    Args:
        session_id: The active session ID.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the page after going back.

    Metadata:
        tier: advanced
        frequency: low
    """
    return await _backend.back(session_id, compact=compact)


@mcp.tool()
async def babelwrap_forward(session_id: str, compact: bool = False) -> dict[str, Any]:
    """Navigate forward in the browser history.

    Args:
        session_id: The active session ID.
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the page after going forward.

    Metadata:
        tier: advanced
        frequency: low
    """
    return await _backend.forward(session_id, compact=compact)


@mcp.tool()
async def babelwrap_scroll(
    session_id: str, direction: str = "down", amount: str = "page", compact: bool = False
) -> dict[str, Any]:
    """Scroll the page up or down.

    Args:
        session_id: The active session ID.
        direction: "up" or "down" (default: "down").
        amount: "page" (full viewport), "half" (half viewport), or pixel count as string (default: "page").
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Structured snapshot of the page after scrolling.

    Metadata:
        tier: standard
        frequency: medium
    """
    return await _backend.scroll(session_id, direction, amount, compact=compact)


@mcp.tool()
async def babelwrap_wait_for(
    session_id: str,
    text: str | None = None,
    selector: str | None = None,
    url_contains: str | None = None,
    timeout_ms: int = 10000,
    compact: bool = False,
) -> dict[str, Any]:
    """Wait for a condition on the page before proceeding.

    Useful after clicking a button that triggers async loading, SPA navigation,
    or any action where you need to wait for specific content to appear.

    Args:
        session_id: The active session ID.
        text: Wait until this text appears on the page.
        selector: Wait until this CSS selector matches a visible element.
        url_contains: Wait until the URL contains this string.
        timeout_ms: Maximum time to wait in milliseconds (default: 10000, max: 30000).
        compact: If True, return a compact snapshot with minimal whitespace.

    Returns:
        Snapshot of the page plus a timed_out boolean indicating if the wait expired.

    Metadata:
        tier: advanced
        frequency: low
    """
    return await _backend.wait_for(
        session_id, text, selector, url_contains, timeout_ms, compact=compact
    )


@mcp.tool()
async def babelwrap_list_pages(session_id: str) -> dict[str, Any]:
    """List all open pages (tabs/popups) in this browser session.

    Use this to discover tabs opened by popups or target="_blank" links,
    then switch to them with babelwrap_switch_page.

    Args:
        session_id: The active session ID.

    Returns:
        Dictionary with pages list (index, url, title) and active_index.

    Metadata:
        tier: advanced
        frequency: low
    """
    return await _backend.list_pages(session_id)


@mcp.tool()
async def babelwrap_switch_page(
    session_id: str, index: int, compact: bool = False
) -> dict[str, Any]:
    """Switch to a different page (tab/popup) within this session.

    Use babelwrap_list_pages first to see available pages and their indices.

    Args:
        session_id: The active session ID.
        index: The page index to switch to (from babelwrap_list_pages).
        compact: If True, return a compact snapshot with reduced token usage.

    Returns:
        Structured snapshot of the newly active page.

    Metadata:
        tier: advanced
        frequency: low
    """
    return await _backend.switch_page(session_id, index, compact=compact)


def main() -> None:
    """Entry point for standalone MCP server (stdio transport)."""
    mcp.run()


if __name__ == "__main__":
    main()
