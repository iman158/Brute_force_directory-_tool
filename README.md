Directory Brute-Force Tool
Overview

This Python script is a simple yet effective directory brute-force tool designed for web application penetration testing. Using a provided wordlist, it systematically checks a target URL for the existence of directories and files, helping identify hidden paths and potential security vulnerabilities.
Features

    Customizable Wordlist: Utilize a wordlist of your choice to tailor the brute-force attack to your target's potential directory and file structure.
    HTTP Requests: Sends HTTP requests to the specified URL with appended directories, checking for valid responses.
    User-Agent Spoofing: Sets a custom User-Agent in the HTTP requests to mimic different client environments.
    URL Schema Check: Ensures the target URL contains a valid schema (http or https).
    Interactive Console: Provides clear feedback on the progress of the brute-force operation, displaying URLs with non-404 responses.
