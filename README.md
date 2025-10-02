<div align="center" style="margin-bottom:30px;">
  <img width="450" alt="tor_plus_google_organic_results" src="https://github.com/user-attachments/assets/697d926c-c8ac-4ba9-8662-f56abd4b99e4" />
</div>

<br><br> <!-- add more <br> if you need more space -->



# Google Organic Results with Tor

This project demonstrates how to fetch **Google organic search results** using the **Tor network** for anonymity and privacy.  
The script leverages the [`torpy`](https://github.com/torpyorg/torpy) library to route requests through Tor relays, mimicking natural browsing behavior and avoiding detection.  
It also uses **multiprocessing** to run several parallel processes for faster query attempts.

---

## Features
- Sends Google search queries through the Tor network.
- Automatically handles cookies between requests to maintain session persistence.
- Uses custom request headers to emulate a real browser.
- Runs multiple processes simultaneously to increase efficiency.
- Displays status codes and successful attempts in color-coded output.

---

## Dependencies
Install the required Python libraries:

```bash
pip install requests torpy termcolor beautifulsoup4
```

---

## Code Overview

### 1. `getCookies(cookie_jar, domain)`
Extracts cookies from the current session and returns them in a valid HTTP `Cookie` header format.

### 2. HTTP Headers
Two sets of headers (`headers` and `headers1`) are defined to imitate a browser.  
- `headers` is used initially.  
- `headers1` is updated with real cookies after the first successful request.

### 3. `get_google_results(i, headers, headers1)`
The main worker function:
- Builds a Google search URL (default keyword: **"stripe"**).  
- Opens a Tor session and sends requests with rotating cookies.  
- On a successful response (`200`), it logs success and updates cookies.  
- If blocked or error occurs, retries with a new Tor circuit.

### 4. Multiprocessing
- The script spawns **10 processes** by default.  
- Each process runs `get_google_results`, simulating multiple independent clients.  
- Results are tracked in a multiprocessing manager list (`mangaerlist`).

---

## Usage
Run the script directly:

```bash
python google_response_tor.py
```

You should see colored logs showing which processes succeeded in retrieving results.

---

## Notes
- Google frequently challenges Tor traffic with CAPTCHAs, so not every request will succeed.  
- Excessive parallel requests may trigger temporary IP blocks.  
- Adjust `number_processes` to control concurrency.  
- The keyword is hardcoded (`"stripe"`); you can modify it inside the `get_google_results` function.  

---

## Disclaimer
This script is for **educational and research purposes only**. Scraping Google search results may violate Google’s Terms of Service. Use responsibly and at your own risk.
