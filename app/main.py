from dotenv import load_dotenv

load_dotenv()

from app.server import mcp

if __name__ == "__main__":
    mcp.run()