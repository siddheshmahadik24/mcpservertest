from mcp.server import FastMCP
import uvicorn

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    # For public access, we need to use uvicorn directly with host="0.0.0.0"
    # This allows external connections to reach the server
    app = mcp.get_app()
    uvicorn.run(app, host="0.0.0.0", port=8000)
