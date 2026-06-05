# Task-2-zeghloulkacem

# Project 2: Basic Encryption & Decryption (Data Confidentiality)

## Overview
This project is the cryptographic phase of the DecodeLabs training, focusing on Data Confidentiality. It demonstrates the fundamental mechanics of obfuscating data in transit and the logical reversible process of decryption using pure mathematical logic.

## Goal
Implement a simple encryption and decryption technique (Caesar Cipher) to protect plain text data.

## Key Features
* **Input processing:** Converts alphabetical text to ASCII integer representations using `ord()`.
* **Mathematical Transformation:** Applies modular arithmetic (`% 26`) to wrap shifted characters safely within the alphabet boundaries.
* **Symmetric Execution:** Uses the same shift key to both encrypt the plaintext and reverse-engineer the ciphertext back to its original state.

## Security Concepts Applied
* **The IPO Model:** Structuring cryptographic systems into Input, Process, and Output phases.
* **Frequency Analysis Awareness:** Understanding the vulnerabilities of mono-alphabetic substitutions (like the Caesar cipher), where identical distribution shapes are preserved, allowing for pattern recognition.

## How to Run
```bash
python BE&D.py
