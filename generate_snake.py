import asyncio
import os

try:
    import aiofiles
    import aiocsv
except ImportError:
    print("Installing required packages...")
    import subprocess
    subprocess.check_call(["pip", "install", "aiofiles", "aiocsv"])
    import aiofiles
    import aiocsv

async def main():
    """Generate the snake animation from GitHub contributions."""
    username = "ChanudiMallikaArachchi"
    
    url = f"https://ghchart.rshah.org/{username}"
    
    print(f"Access your snake graph at: {url}")
    print(f"\nTo add to your README, use this markdown:")
    print(f"![{username}'s GitHub Snake Graph]({url})")

if __name__ == "__main__":
    asyncio.run(main())
