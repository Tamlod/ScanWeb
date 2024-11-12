from time import time
import aiohttp
import ssl
import socket
from tqdm import tqdm


async def check_ssl_certificate(domain):
    result = f"Проверка SSL-сертификата для {domain}: "
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=domain) as s:
            s.connect((domain, 443))
            cert = s.getpeercert()
        result += f"действителен до: {cert['notAfter']}, выдан: {cert['issuer'][0][0][1]}"
    except Exception as e:
        result += f"Ошибка: {e}"
    return result


async def check_security_headers(session, url):
    headers_to_check = [
        "Content-Security-Policy", "X-Content-Type-Options", "X-Frame-Options",
        "Strict-Transport-Security", "Referrer-Policy", "Permissions-Policy", "X-XSS-Protection"
    ]
    result = f"Проверка заголовков безопасности для {url}: "
    async with session.get(url) as response:
        missing_headers = [header for header in headers_to_check if header not in response.headers]
        if missing_headers:
            result += f"Отсутствуют: {', '.join(missing_headers)}"
        else:
            result += "Все важные заголовки присутствуют."
    return result


async def check_cors_policy(session, url):
    result = "Проверка политики CORS: "
    try:
        async with session.options(url) as response:
            if "Access-Control-Allow-Origin" in response.headers:
                result += f"CORS разрешен: {response.headers['Access-Control-Allow-Origin']}"
            else:
                result += "CORS не настроен."
    except Exception as e:
        result += f"Ошибка: {e}"
    return result


async def check_redirects_and_response_time(session, url):
    start_time = time()
    async with session.get(url, allow_redirects=True) as response:
        response_time = round(time() - start_time, 2)
        if response.history:
            redirects = " -> ".join([resp.url for resp in response.history]) + f" -> {response.url}"
            result = f"Редиректы: {redirects}. Время ответа: {response_time} секунд."
        else:
            result = f"Нет редиректов. Время ответа: {response_time} секунд."
    return result


async def scan_domains(args):
    domains = args.domains.split(",")
    results = {}
    timeout = aiohttp.ClientTimeout(total=args.timeout)

    if args.no_progress:
        async with aiohttp.ClientSession(timeout=timeout) as session:
            for domain in domains:
                results[domain] = await scan_domain(session, domain.strip())
    else:
        with tqdm(total=len(domains), desc="Сканирование доменов", unit="домен") as pbar:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                for domain in domains:
                    results[domain] = await scan_domain(session, domain.strip())
                    pbar.update(1)
    return results


async def scan_domain(session, domain):
    url = f"https://{domain}"
    return {
        'SSL': await check_ssl_certificate(domain),
        'Headers': await check_security_headers(session, url),
        'CORS': await check_cors_policy(session, url),
        'Redirects and Response Time': await check_redirects_and_response_time(session, url),
    }
