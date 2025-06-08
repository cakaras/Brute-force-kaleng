`README.md`
```md
# Brute Force Hidden Path Finder

A simple and powerful command-line pentest tool written in Python to discover hidden paths and directories on websites by brute forcing URL paths from a given wordlist. Ideal for penetration testers and security researchers to enumerate hidden resources quickly and efficiently.

---

## Features

- Multithreaded directory and file brute forcing for speed.
- Supports HTTPS and HTTP targets with disabled SSL warnings for invalid certs.
- Reports valid URLs with HTTP status codes below 400.
- Optional verbose mode to show all attempted paths and errors.
- Works out-of-the-box on Linux terminals with Python 3.
- Easy CLI interface with clear options.

---

## Screenshot

```
$ python3 bruteforce_path_finder.py -u https://example.com -w wordlist.txt -t 20
[+] Starting scan on https://example.com with 20 threads...
[+] Loaded 1000 paths from wordlist
[+] Found: https://example.com/admin (Status: 200)
[+] Found: https://example.com/login (Status: 200)
...
[+] Scan completed.
[+] Valid paths found:
  https://example.com/admin (Status: 200)
  https://example.com/login (Status: 200)
```

---

## Installation

1. Make sure you have Python 3 installed on your Linux system.
2. Clone this repository or download the `bruteforce_path_finder.py` script.
3. Prepare a wordlist text file with potential directory and file names, one per line. (e.g., `common.txt`, `rockyou.txt` or custom lists)

---

## Usage

```sh
python3 bruteforce_path_finder.py -u <target_url> -w <wordlist_file> [-t <threads>] [-v]
```

### Arguments

| Flag        | Description                                      | Default   |
|-------------|------------------------------------------------|-----------|
| `-u`, `--url`     | Base target URL (with http:// or https://)      | Required  |
| `-w`, `--wordlist`| Path to a wordlist file with paths to brute force | Required  |
| `-t`, `--threads` | Number of concurrent threads to use             | 10        |
| `-v`, `--verbose` | Show all attempts (including failed paths)      | False     |

### Example

```sh
python3 bruteforce_path_finder.py -u https://example.com -w wordlists/common.txt -t 15
```

---

## Notes

- Paths in the wordlist should be relative (e.g., `admin`, `login.php`, `secret/`), no leading slashes required.
- This tool does not handle login/authentication. For authenticated scans, consider tunneling through proxies or modifying the code accordingly.
- Use responsibly and only against systems you have permission to test.

---

## Contribution

Feel free to submit issues or pull requests for improvements like adding support for proxies, authentication, rate limiting, or file extensions enumeration.

---

## License

This project is licensed under the MIT License.

---

## Contact

Created by a passionate security enthusiast. For questions or collaborations, open an issue or reach out on GitHub.


```
