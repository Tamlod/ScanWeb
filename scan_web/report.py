import json

async def generate_report(results, args):
    if args.format == "html":
        await create_html_report(results)
    elif args.format == "text":
        await create_text_report(results)
    elif args.format == "json":
        await create_json_report(results)

async def create_html_report(results):
    report_template = """
    <html>
        <head>
            <title>Отчет сканирования уязвимостей</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f4f4f9; color: #333; }
                h1 { color: #333; text-align: center; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
                th { background-color: #4CAF50; color: white; }
                tr:nth-child(even) { background-color: #f2f2f2; }
                tr:hover { background-color: #ddd; }
            </style>
        </head>
        <body>
            <h1>Отчет сканирования уязвимостей</h1>
            <table>
                <thead>
                    <tr>
                        <th>Проверка</th>
                        <th>Результат</th>
                    </tr>
                </thead>
                <tbody>
    """
    for test, result in results.items():
        report_template += f"<tr><td>{test}</td><td>{result}</td></tr>"
    report_template += """
                </tbody>
            </table>
        </body>
    </html>
    """
    with open("scan_report.html", 'w') as file:
        file.write(report_template)
    print("HTML отчет сохранен в scan_report.html")

async def create_text_report(results):
    with open("scan_report.txt", 'w') as file:
        for test, result in results.items():
            file.write(f"{test}: {result}\n")
    print("Текстовый отчет сохранен в scan_report.txt")

async def create_json_report(results):
    with open("scan_report.json", 'w') as file:
        json.dump(results, file, indent=4)
    print("JSON отчет сохранен в scan_report.json")
