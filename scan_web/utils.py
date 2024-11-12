import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Сканер веб-безопасности")
    parser.add_argument("-d", "--domains", type=str, required=True, help="Список доменов через запятую")
    parser.add_argument("-f", "--format", type=str, choices=["html", "text", "json"], default="html", help="Формат отчета")
    parser.add_argument("-t", "--timeout", type=int, default=10, help="Тайм-аут для запросов в секундах")
    parser.add_argument("--no-progress", action="store_true", help="Отключить прогресс-бар")
    parser.add_argument("--detailed-report", action="store_true", help="Включить детализированный отчёт")
    return parser.parse_args()
