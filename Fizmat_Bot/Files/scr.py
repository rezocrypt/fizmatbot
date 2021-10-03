import random
import asyncio
from pyppeteer import launch
def get(url):
    async def main():
        path = f"weatherphoto{random.randint(1000000,99999999)}.png"
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        await page.screenshot({'path': path, 'fullPage': 'true'})
        await browser.close()
        return path
    
    asyncio.get_event_loop().run_until_complete(main())
