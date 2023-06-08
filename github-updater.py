import asyncio
import aiohttp
import sys

WELCOME_ART = """
 _____ _ _   _           _       _   _ _                        
|  __ (_| | | |         | |     | | | (_)                       
| |  \/_| |_| |__  _   _| |__   | | | |_  _____      _____ _ __ 
| | __| | __| '_ \| | | | '_ \  | | | | |/ _ \ \ /\ / / _ | '__|
| |_\ | | |_| | | | |_| | |_) | \ \_/ | |  __/\ V  V |  __| |   
 \____|_|\__|_| |_|\__,_|_.__/   \___/|_|\___| \_/\_/ \___|_|                                                                  
"""

async def send_request(session, url):
    """Asynchronously send a GET request to a URL."""
    async with session.get(url) as response:
        if response.status == 200:
            print("[+] Successful")


class GithubUpdate:
    """Class for GitHub Update."""
    def __init__(self):
        print(WELCOME_ART + "\n")
        self.target = input("[*] Please input your viewcount link: ")
        self.req_num = int(input("[*] Please input number of requests: "))
        self.delay = float(input("[*] Please input delay (in milliseconds): "))
        self.loop = asyncio.get_event_loop()

    async def start(self):
        """Start sending requests asynchronously."""
        tasks = [send_request(aiohttp.ClientSession(), self.target) for _ in range(self.req_num)]
        await asyncio.gather(*tasks)

    def run(self):
        """Execute the start method."""
        self.loop.run_until_complete(self.start())

    def stop(self):
        """Stop all running tasks and exit the program."""
        print("[*] Stopping...")
        for task in asyncio.Task.all_tasks():
            task.cancel()
        sys.exit(0)


def main():
    """Main function."""
    updater = GithubUpdate()
    updater.run()

    while True:
        if input() == 'S':
            updater.stop()


if __name__ == "__main__":
    main()
