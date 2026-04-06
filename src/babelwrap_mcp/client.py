from __future__ import annotations

import os
from typing import Any

import httpx


class StandaloneBackend:
    """MCP backend that calls the BabelWrap REST API over HTTP."""

    def __init__(self) -> None:
        self._base_url = os.environ.get("BABELWRAP_API_URL", "https://api.babelwrap.com/v1")
        self._api_key = os.environ.get("BABELWRAP_API_KEY", "")
        self._client: httpx.AsyncClient | None = None

    def _get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=self._base_url,
                headers={"Authorization": f"Bearer {self._api_key}"},
                timeout=60.0,
            )
        return self._client

    async def _request(self, method: str, path: str, json: dict | None = None) -> dict[str, Any]:
        client = self._get_client()
        resp = await client.request(method, path, json=json)
        resp.raise_for_status()
        return resp.json()

    async def new_session(self, metadata: dict | None = None) -> dict[str, Any]:
        body = {}
        if metadata:
            body["metadata"] = metadata
        data = await self._request("POST", "/sessions", json=body)
        return {"session_id": data["session_id"]}

    async def close_session(self, session_id: str) -> dict[str, Any]:
        data = await self._request("DELETE", f"/sessions/{session_id}")
        return {"success": data.get("success", True)}

    async def navigate(self, session_id: str, url: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/navigate"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={"url": url})
        return data.get("snapshot", data)

    async def snapshot(self, session_id: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/snapshot"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={})
        return data.get("snapshot", data)

    async def click(self, session_id: str, target: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/click"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={"target": target})
        return data.get("snapshot", data)

    async def fill(
        self, session_id: str, target: str, value: str, compact: bool = False
    ) -> dict[str, Any]:
        path = f"/sessions/{session_id}/fill"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={"target": target, "value": value})
        return data.get("snapshot", data)

    async def submit(
        self, session_id: str, target: str | None = None, compact: bool = False
    ) -> dict[str, Any]:
        body = {}
        if target:
            body["target"] = target
        path = f"/sessions/{session_id}/submit"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json=body)
        return data.get("snapshot", data)

    async def extract(self, session_id: str, query: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/extract"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={"query": query})
        return {"data": data.get("data", []), "snapshot": data.get("snapshot", {})}

    async def screenshot(self, session_id: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/screenshot"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={})
        return {"image": data.get("image", ""), "snapshot": data.get("snapshot", {})}

    async def press(self, session_id: str, key: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/press"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={"key": key})
        return data.get("snapshot", data)

    async def upload(
        self, session_id: str, target: str, file_base64: str, filename: str, compact: bool = False
    ) -> dict[str, Any]:
        path = f"/sessions/{session_id}/upload"
        if compact:
            path += "?compact=true"
        data = await self._request(
            "POST",
            path,
            json={"target": target, "file_base64": file_base64, "filename": filename},
        )
        return data.get("snapshot", data)

    async def hover(self, session_id: str, target: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/hover"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={"target": target})
        return data.get("snapshot", data)

    async def back(self, session_id: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/back"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={})
        return data.get("snapshot", data)

    async def forward(self, session_id: str, compact: bool = False) -> dict[str, Any]:
        path = f"/sessions/{session_id}/forward"
        if compact:
            path += "?compact=true"
        data = await self._request("POST", path, json={})
        return data.get("snapshot", data)

    async def scroll(
        self, session_id: str, direction: str = "down", amount: str = "page", compact: bool = False
    ) -> dict[str, Any]:
        path = f"/sessions/{session_id}/scroll"
        if compact:
            path += "?compact=true"
        data = await self._request(
            "POST",
            path,
            json={"direction": direction, "amount": amount},
        )
        return data.get("snapshot", data)

    async def wait_for(
        self,
        session_id: str,
        text: str | None = None,
        selector: str | None = None,
        url_contains: str | None = None,
        timeout_ms: int = 10000,
        compact: bool = False,
    ) -> dict[str, Any]:
        body: dict[str, Any] = {"timeout_ms": timeout_ms}
        if text:
            body["text"] = text
        if selector:
            body["selector"] = selector
        if url_contains:
            body["url_contains"] = url_contains
        path = f"/sessions/{session_id}/wait_for"
        if compact:
            path += "?compact=true"
        data = await self._request(
            "POST",
            path,
            json=body,
        )
        return data

    async def list_pages(self, session_id: str) -> dict[str, Any]:
        data = await self._request("GET", f"/sessions/{session_id}/pages")
        return data

    async def switch_page(
        self, session_id: str, index: int, compact: bool = False
    ) -> dict[str, Any]:
        path = f"/sessions/{session_id}/switch_page"
        if compact:
            path += "?compact=true"
        data = await self._request(
            "POST",
            path,
            json={"index": index},
        )
        return data.get("snapshot", data)
