from mcp.server import FastMCP

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name} from Azure VM!"

if __name__ == "__main__":
    # This version will run on Azure VM
    # Note: FastMCP binds to localhost by default
    # You'll need to use SSH port forwarding or configure Azure firewall
    print("Starting server on Azure VM...")
    print("Server will be accessible at http://127.0.0.1:8000 locally on the VM")
    print("For external access, you'll need SSH port forwarding")
    mcp.run(transport="streamable-http")
