# ScanWeb

**ScanWeb** is a web vulnerability scanning tool written in Python. It performs basic checks for SSL certificates, HTTP security headers, CORS policy, and redirects. This tool is useful for developers, security testers, and administrators who want a quick analysis of key security aspects of their web applications.

## Features

- 🔒 **SSL Certificate Check**: Validity and expiration of the SSL certificate.
- 🛡️ **HTTP Security Header Check**: Checks headers such as `Content-Security-Policy`, `X-Content-Type-Options`, `Strict-Transport-Security`, and others.
- 🔗 **CORS Policy Check**: Determines if the resource is accessible from other domains.
- 🚦 **Redirect Check**: Analyzes redirect chains and measures response time.

---

## Installation

### 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/Tamlod/ScanWeb.git
cd ScanWeb
2. Install Python and Dependencies
Installing Python 3 and pip
First, ensure you have Python 3 and the pip package manager installed.

Ubuntu/Debian (APT):

bash
Копировать код
sudo apt update
sudo apt install python3 python3-pip -y
Arch Linux (Pacman):

bash
Копировать код
sudo pacman -Sy python python-pip
Install Dependencies from requirements.txt
After installing Python and pip, run the following command to install project dependencies:

bash
Копировать код
pip install -r requirements.txt
3. Set Up a Virtual Environment (Recommended)
To isolate dependencies, you can create a virtual environment:

bash
Копировать код
python3 -m venv .venv
source .venv/bin/activate  # Activate the virtual environment
pip install -r requirements.txt  # Install dependencies in the virtual environment
To deactivate the virtual environment, run:

bash
Копировать код
deactivate
Usage
Run ScanWeb
Once installed, you can run a scan using the following command:

bash
Копировать код
python3 -m scan_web.main -d example.com,anotherdomain.com -f html --detailed-report
Command Line Arguments
-d or --domains: List of domains separated by commas, e.g., example.com,anotherdomain.com.
-f or --format: Report format (html, text, or json). Defaults to html.
-t or --timeout: Timeout for requests in seconds. Defaults to 10 seconds.
--no-progress: Disables the progress bar.
--detailed-report: Enables a detailed report.
Examples
Scan a single domain with an HTML report:

bash
Копировать код
python3 -m scan_web.main -d example.com -f html
Scan multiple domains with a JSON report and a 15-second timeout:

bash
Копировать код
python3 -m scan_web.main -d example.com,anotherdomain.com -f json -t 15
Scan without showing the progress bar:

bash
Копировать код
python3 -m scan_web.main -d example.com -f text --no-progress
Additional Dependencies for Linux (Optional)
If you encounter errors related to missing libraries, install additional dependencies for Python and networking libraries.

Ubuntu/Debian:

bash
Копировать код
sudo apt install build-essential libssl-dev libffi-dev python3-dev
Arch Linux:

bash
Копировать код
sudo pacman -Sy base-devel openssl
Uninstallation
To remove all installed components, simply delete the project folder and virtual environment (if used):

bash
Копировать код
cd ..
rm -rf ScanWeb
License
This project is licensed under the MIT License, meaning you are free to use, modify, and distribute it. For more details, see the LICENSE file.

css
Копировать код
