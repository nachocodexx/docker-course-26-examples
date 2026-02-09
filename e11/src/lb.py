import uvicorn
import httpx
from fastapi import FastAPI, Response
# from itertools import cycle

app = FastAPI()

# Internal Docker DNS names
# BACKENDS = [
#     "http://bar-service:5000",
#     "http://box-service:5000",
#     "http://hist-service:5000"
# ]
BACKENDS = {
    "bar": "http://bar-service:5000",
    "box": "http://box-service:5000",
    "hist": "http://hist-service:5000"
}

# backend_pool = cycle(BACKENDS)

@app.get("/{plot_type}")
async def proxy_request(plot_type: str):
    # 1. Pick next service (Round Robin)
    # target_service = next(backend_pool)
    target_service = BACKENDS.get(plot_type,"bar")
    print(f"Redirecting traffic to: {target_service}", flush=True)

    try:
        # 2. Async HTTP request to the worker
        async with httpx.AsyncClient() as client:
            resp = await client.get(target_service)
        
        # 3. Stream response back to user
        return Response(content=resp.content, media_type="image/png")
    
    except httpx.RequestError:
        return Response(content=f"Error connecting to {target_service}", status_code=502)

if __name__ == '__main__':
    # Load Balancer runs on port 80
    uvicorn.run(app, host="0.0.0.0", port=80)