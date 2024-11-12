# ScanWeb

ScanWeb — это инструмент для сканирования веб-сайтов на уязвимости, написанный на Python. Он позволяет выполнять базовые проверки на наличие SSL-сертификатов, безопасность HTTP-заголовков, политику CORS и перенаправления. Инструмент полезен для разработчиков, тестировщиков безопасности и администраторов, которые хотят быстро проанализировать основные аспекты безопасности своих веб-приложений.

## Возможности

- 🔒 **Проверка SSL-сертификатов**: проверка валидности и срока действия SSL-сертификата.
- 🛡️ **Проверка HTTP-заголовков безопасности**: анализ заголовков безопасности, таких как `Content-Security-Policy`, `X-Content-Type-Options`, `Strict-Transport-Security` и других.
- 🔗 **Проверка политики CORS**: определяет, разрешен ли доступ к ресурсу через другие домены.
- 🚦 **Проверка редиректов**: анализирует цепочки перенаправлений и измеряет время отклика.

## Установка

1. **Клонирование репозитория**

   Клонируйте репозиторий с GitHub:

   ```bash
   git clone https://github.com/Tamlod/ScanWeb.git
   cd ScanWeb
### 2. Установка Python и зависимостей

#### Установка Python 3 и pip

Убедитесь, что у вас установлен Python 3 и менеджер пакетов `pip`.

- **Ubuntu/Debian (APT)**:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip -y
- **Arch Linux (Pacman)**:
  ```bash
  sudo pacman -Sy python python-pip

#### Установка зависимостей из `requirements.txt`

После установки Python и pip выполните следующую команду для установки зависимостей проекта:

```bash
pip install -r requirements.txt

#### Использование

### Запуск ScanWeb

После установки вы можете запустить сканирование с помощью команды:

```bash
python3 -m scan_web.main -d example.com,anotherdomain.com -f html --detailed-report

