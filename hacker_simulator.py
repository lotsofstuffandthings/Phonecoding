#!/usr/bin/env python3
"""
HACKER SIMULATOR
Hollywood-style hacking simulation - totally fake but looks AMAZING!
Perfect for impressing kids (and adults)!
"""

import time
import random
import sys
import os

# ANSI color codes for terminal
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BLINK = '\033[5m'

def clear_screen():
    """Clear the terminal screen"""
    os.system('clear' if os.name != 'nt' else 'cls')

def type_text(text, delay=0.03, color=Colors.GREEN):
    """Simulate typing effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fast_type(text, delay=0.01, color=Colors.GREEN):
    """Faster typing for bulk text"""
    for char in text:
        sys.stdout.write(color + char + Colors.END)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_slow(text, delay=0.5, color=Colors.GREEN):
    """Print with delay after"""
    print(color + text + Colors.END)
    time.sleep(delay)

def generate_ip():
    """Generate random IP address"""
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def progress_bar(total=50, label="Progress", color=Colors.CYAN):
    """Animated progress bar"""
    sys.stdout.write(color + f"{label}: [" + Colors.END)
    for i in range(total):
        sys.stdout.write(color + "█" + Colors.END)
        sys.stdout.flush()
        time.sleep(random.uniform(0.02, 0.08))
    sys.stdout.write(color + "] 100%\n" + Colors.END)
    time.sleep(0.3)

def scanning_animation(items, label="Scanning"):
    """Show scanning animation"""
    for item in items:
        status = random.choice(["OK", "OK", "OK", "SECURE", "OPEN"])
        color = Colors.GREEN if status == "OK" or status == "OPEN" else Colors.YELLOW
        print(f"{Colors.CYAN}[SCAN]{Colors.END} {label}: {item} ... {color}[{status}]{Colors.END}")
        time.sleep(random.uniform(0.1, 0.3))

def intro_sequence():
    """Dramatic intro"""
    clear_screen()
    print()
    type_text("=" * 70, delay=0.01, color=Colors.RED)
    type_text("    █▀▀▀▀▀█ CYBER INTRUSION TOOLKIT v3.7.2 █▀▀▀▀▀█", delay=0.02, color=Colors.RED)
    type_text("=" * 70, delay=0.01, color=Colors.RED)
    print()
    time.sleep(0.5)
    print_slow(f"{Colors.YELLOW}⚠️  WARNING: Unauthorized access prohibited ⚠️{Colors.END}", 0.3)
    print()
    time.sleep(0.5)

def initialize_system():
    """System initialization"""
    type_text("[SYSTEM] Initializing quantum encryption bypass...", delay=0.02, color=Colors.CYAN)
    time.sleep(0.4)
    print_slow(f"{Colors.GREEN}[✓] Encryption bypass loaded{Colors.END}", 0.2)

    type_text("[SYSTEM] Loading neural network AI...", delay=0.02, color=Colors.CYAN)
    time.sleep(0.3)
    print_slow(f"{Colors.GREEN}[✓] AI core online{Colors.END}", 0.2)

    type_text("[SYSTEM] Establishing anonymous connection...", delay=0.02, color=Colors.CYAN)
    time.sleep(0.5)
    print_slow(f"{Colors.GREEN}[✓] Connection secured via TOR network{Colors.END}", 0.3)
    print()

def scan_network():
    """Network scanning sequence"""
    print_slow(f"\n{Colors.BOLD}{Colors.YELLOW}[PHASE 1] NETWORK RECONNAISSANCE{Colors.END}", 0.5)
    print_slow(f"{Colors.CYAN}{'=' * 50}{Colors.END}\n", 0.3)

    type_text("Scanning local network for targets...", delay=0.02, color=Colors.WHITE)
    time.sleep(0.5)

    # Generate random IPs
    ips = [generate_ip() for _ in range(8)]
    scanning_animation(ips, "IP Address")

    print()
    target_ip = random.choice(ips)
    type_text(f"[!] High-value target identified: {target_ip}", delay=0.02, color=Colors.YELLOW)
    type_text(f"[!] Target: SECURE_SERVER_MAINFRAME", delay=0.02, color=Colors.YELLOW)
    print()
    time.sleep(0.5)

    return target_ip

def port_scan(target_ip):
    """Port scanning sequence"""
    print_slow(f"\n{Colors.BOLD}{Colors.YELLOW}[PHASE 2] PORT SCANNING{Colors.END}", 0.5)
    print_slow(f"{Colors.CYAN}{'=' * 50}{Colors.END}\n", 0.3)

    type_text(f"Initiating deep port scan on {target_ip}...", delay=0.02, color=Colors.WHITE)
    print()
    time.sleep(0.3)

    ports = [21, 22, 23, 80, 443, 3306, 8080, 3389]
    port_names = ["FTP", "SSH", "TELNET", "HTTP", "HTTPS", "MySQL", "HTTP-Alt", "RDP"]

    for port, name in zip(ports, port_names):
        status = random.choice(["OPEN", "CLOSED", "OPEN", "FILTERED"])
        if status == "OPEN":
            color = Colors.GREEN
        elif status == "CLOSED":
            color = Colors.RED
        else:
            color = Colors.YELLOW

        print(f"{Colors.CYAN}[SCAN]{Colors.END} Port {port:5d} ({name:10s}) ... {color}[{status}]{Colors.END}")
        time.sleep(random.uniform(0.15, 0.35))

    print()
    print_slow(f"{Colors.GREEN}[✓] Vulnerability found: Port 22 (SSH) - Weak encryption{Colors.END}", 0.5)
    print()

def crack_password():
    """Password cracking sequence"""
    print_slow(f"\n{Colors.BOLD}{Colors.YELLOW}[PHASE 3] CREDENTIAL BREACH{Colors.END}", 0.5)
    print_slow(f"{Colors.CYAN}{'=' * 50}{Colors.END}\n", 0.3)

    type_text("Deploying brute-force algorithm...", delay=0.02, color=Colors.WHITE)
    print()
    time.sleep(0.3)

    passwords = [
        "admin123", "password", "qwerty", "letmein", "welcome",
        "monkey", "dragon", "master", "trustno1", "shadow"
    ]

    for pwd in passwords:
        print(f"{Colors.RED}[ATTEMPT]{Colors.END} Trying password: {Colors.YELLOW}{pwd}{Colors.END}", end="")
        time.sleep(random.uniform(0.3, 0.6))
        print(f" ... {Colors.RED}[FAILED]{Colors.END}")

    print()
    type_text("Brute force inefficient. Switching to dictionary attack...", delay=0.02, color=Colors.YELLOW)
    print()
    time.sleep(0.5)

    progress_bar(40, "Analyzing hash patterns", Colors.MAGENTA)

    print()
    type_text("Password hash cracked!", delay=0.02, color=Colors.GREEN)
    time.sleep(0.3)
    print_slow(f"{Colors.GREEN}[✓] Credentials obtained: admin / Sup3rS3cr3t2024{Colors.END}", 0.5)
    print()

def bypass_firewall():
    """Firewall bypass sequence"""
    print_slow(f"\n{Colors.BOLD}{Colors.YELLOW}[PHASE 4] FIREWALL PENETRATION{Colors.END}", 0.5)
    print_slow(f"{Colors.CYAN}{'=' * 50}{Colors.END}\n", 0.3)

    type_text("Analyzing firewall architecture...", delay=0.02, color=Colors.WHITE)
    time.sleep(0.5)
    print_slow(f"{Colors.YELLOW}[!] Detected: Military-grade firewall (Level 5){Colors.END}", 0.3)
    print()

    type_text("Injecting polymorphic payload...", delay=0.02, color=Colors.CYAN)
    time.sleep(0.4)

    progress_bar(35, "Payload injection", Colors.RED)

    print()
    type_text("Exploiting zero-day vulnerability CVE-2024-9999...", delay=0.02, color=Colors.YELLOW)
    time.sleep(0.6)

    print()
    print_slow(f"{Colors.GREEN}[✓] Firewall bypassed successfully!{Colors.END}", 0.5)
    print()

def extract_data():
    """Data extraction sequence"""
    print_slow(f"\n{Colors.BOLD}{Colors.YELLOW}[PHASE 5] DATA EXFILTRATION{Colors.END}", 0.5)
    print_slow(f"{Colors.CYAN}{'=' * 50}{Colors.END}\n", 0.3)

    type_text("Establishing backdoor connection...", delay=0.02, color=Colors.WHITE)
    time.sleep(0.4)
    print_slow(f"{Colors.GREEN}[✓] Backdoor active{Colors.END}", 0.3)
    print()

    files = [
        "classified_documents.zip",
        "user_database.sql",
        "financial_records.xlsx",
        "encryption_keys.pem",
        "server_config.json",
        "admin_passwords.txt"
    ]

    type_text("Locating sensitive files...", delay=0.02, color=Colors.WHITE)
    print()
    time.sleep(0.3)

    for file in files:
        size = random.randint(100, 9999)
        print(f"{Colors.CYAN}[FOUND]{Colors.END} {file} ({size} KB)")
        time.sleep(0.2)

    print()
    progress_bar(50, "Downloading files", Colors.GREEN)

    print()
    print_slow(f"{Colors.GREEN}[✓] Exfiltration complete - 6 files downloaded{Colors.END}", 0.5)
    print()

def cover_tracks():
    """Cover tracks sequence"""
    print_slow(f"\n{Colors.BOLD}{Colors.YELLOW}[PHASE 6] COVERING TRACKS{Colors.END}", 0.5)
    print_slow(f"{Colors.CYAN}{'=' * 50}{Colors.END}\n", 0.3)

    type_text("Erasing access logs...", delay=0.02, color=Colors.WHITE)
    time.sleep(0.5)
    print_slow(f"{Colors.GREEN}[✓] Logs cleared{Colors.END}", 0.2)

    type_text("Removing backdoor traces...", delay=0.02, color=Colors.WHITE)
    time.sleep(0.4)
    print_slow(f"{Colors.GREEN}[✓] Backdoor removed{Colors.END}", 0.2)

    type_text("Spoofing connection origin...", delay=0.02, color=Colors.WHITE)
    time.sleep(0.5)
    print_slow(f"{Colors.GREEN}[✓] Trail obfuscated{Colors.END}", 0.3)
    print()

def finale():
    """Dramatic finale"""
    print()
    time.sleep(0.5)
    print("=" * 70)
    time.sleep(0.2)

    # Big dramatic "ACCESS GRANTED" message
    print()
    type_text("    ███████╗██╗   ██╗ ██████╗ ██████╗███████╗███████╗███████╗", delay=0.005, color=Colors.GREEN)
    type_text("    ██╔════╝██║   ██║██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝", delay=0.005, color=Colors.GREEN)
    type_text("    ███████╗██║   ██║██║     ██║     █████╗  ███████╗███████╗", delay=0.005, color=Colors.GREEN)
    type_text("    ╚════██║██║   ██║██║     ██║     ██╔══╝  ╚════██║╚════██║", delay=0.005, color=Colors.GREEN)
    type_text("    ███████║╚██████╔╝╚██████╗╚██████╗███████╗███████║███████║", delay=0.005, color=Colors.GREEN)
    type_text("    ╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝", delay=0.005, color=Colors.GREEN)
    print()

    time.sleep(0.3)
    print_slow(f"{Colors.BOLD}{Colors.GREEN}[✓] MISSION ACCOMPLISHED{Colors.END}", 0.3)
    print_slow(f"{Colors.CYAN}[✓] Full system access granted{Colors.END}", 0.2)
    print_slow(f"{Colors.CYAN}[✓] All data extracted successfully{Colors.END}", 0.2)
    print_slow(f"{Colors.CYAN}[✓] No traces left behind{Colors.END}", 0.2)

    print()
    print("=" * 70)
    print()

    time.sleep(0.5)
    print_slow(f"{Colors.YELLOW}Disconnecting...{Colors.END}", 0.5)
    print()
    print_slow(f"{Colors.WHITE}You're in. 😎{Colors.END}", 0.3)
    print()

def quick_mode():
    """Quick version with just the highlights"""
    clear_screen()
    print()
    type_text("=" * 60, delay=0.005, color=Colors.RED)
    type_text("    ⚡ QUICK HACK MODE ⚡", delay=0.01, color=Colors.RED)
    type_text("=" * 60, delay=0.005, color=Colors.RED)
    print()

    target = generate_ip()
    type_text(f"Target acquired: {target}", delay=0.01, color=Colors.YELLOW)
    print()

    progress_bar(30, "Scanning", Colors.CYAN)
    progress_bar(30, "Exploiting", Colors.MAGENTA)
    progress_bar(30, "Cracking", Colors.RED)
    progress_bar(30, "Accessing", Colors.GREEN)

    print()
    type_text("    █████╗  ██████╗ ██████╗███████╗███████╗███████╗", delay=0.003, color=Colors.GREEN)
    type_text("   ██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝", delay=0.003, color=Colors.GREEN)
    type_text("   ███████║██║     ██║     █████╗  ███████╗███████╗", delay=0.003, color=Colors.GREEN)
    type_text("   ██╔══██║██║     ██║     ██╔══╝  ╚════██║╚════██║", delay=0.003, color=Colors.GREEN)
    type_text("   ██║  ██║╚██████╗╚██████╗███████╗███████║███████║", delay=0.003, color=Colors.GREEN)
    type_text("   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝╚══════╝╚══════╝╚══════╝", delay=0.003, color=Colors.GREEN)
    print()
    print_slow(f"{Colors.BOLD}{Colors.GREEN}[✓] GRANTED{Colors.END}", 0.3)
    print()

def main():
    """Main program"""
    print()
    print(f"{Colors.BOLD}Select mode:{Colors.END}")
    print(f"  1. {Colors.CYAN}Full Simulation{Colors.END} (60 seconds - maximum drama!)")
    print(f"  2. {Colors.YELLOW}Quick Hack{Colors.END} (15 seconds - rapid fire)")
    print()

    choice = input(f"{Colors.WHITE}Enter choice (1 or 2): {Colors.END}").strip()

    if choice == "2":
        quick_mode()
    else:
        intro_sequence()
        initialize_system()
        target = scan_network()
        port_scan(target)
        crack_password()
        bypass_firewall()
        extract_data()
        cover_tracks()
        finale()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}[!] Operation aborted by user{Colors.END}\n")
        sys.exit(0)
