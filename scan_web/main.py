import asyncio
from scan_web.utils import parse_args
from scan_web.report import generate_report
from scan_web.scanner import scan_domains

async def main():
    args = parse_args()
    results = await scan_domains(args)
    await generate_report(results, args)

if __name__ == "__main__":
    asyncio.run(main())
