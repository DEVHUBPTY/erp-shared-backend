from fastapi.responses import JSONResponse
from shared.schemas.api import ResponseAPI
from typing import Any, Literal
from fastapi import Request, Response
import httpx

def json_response(
    status_code: int,
    *,
    status: Literal["success", "error"],
    data: Any = None,
    message: str = None,
    error: str = None,
    response: Response = None
) -> Response:
    content = ResponseAPI(
        status=status,
        data=data,
        message=message,
        error=error
    ).model_dump(mode="json")

    if response:
        response.status_code = status_code
        response.media_type = "application/json"
        response.body = JSONResponse(content=content).body
        return response

    return JSONResponse(status_code=status_code, content=content)

async def proxy_request(
    request: Request,
    target_base_url: str,
    sub_path: str
) -> Response:
    try:
        url = f"{target_base_url.rstrip('/')}/{sub_path.lstrip('/')}"
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=request.method,
                url=url,
                headers=dict(request.headers),
                params=dict(request.query_params),
                content=await request.body(),
            )
        return Response(
            status_code=response.status_code,
            content=response.content,
            headers=dict(response.headers)
        )
    except httpx.RequestError as e:
        return JSONResponse(
            status_code=502,
            content={"error": f"Gateway error: {str(e)}"}
        )