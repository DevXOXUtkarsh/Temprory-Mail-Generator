# Temp Email OTP Registration Script

This Python script automates the process of generating a temporary email, registering a user on a given service using that email, retrieving an OTP from the email inbox, and verifying the OTP to obtain an authentication token. It utilizes the Faker library to generate a random email and password, along with requests to interact with the service's API.

## Features
- Generate temporary email via the `temp-mail.io` API.
- Generate random password using custom function.
- Register user with the generated email and password.
- Fetch OTP from the temporary email inbox.
- Verify OTP and retrieve an authentication token.
- Save the authentication token to a file for future use.

## Prerequisites
Before running the script, ensure you have the following installed:

- Python 3.x
- The required libraries: `requests`, `faker`

### Installation
Clone the repository and navigate to the directory:

```bash
git clone https://github.com/DevXOXUtkarsh/Temprory-Mail-Generator.git
cd Temprory-Mail-Generator
