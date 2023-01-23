import argparse
import datetime
import time

import dns.resolver


def monitor_dns(hostname: str, interval: int, substring: str):
    while True:
        try:
            answers = dns.resolver.resolve(hostname, 'TXT')
            for rdata in answers:
                for txt_string in rdata.strings:
                    if substring in txt_string:
                        print(f'{datetime.datetime.now()} - Substring found in TXT record: {txt_string}')
        except dns.resolver.NXDOMAIN:
            print(f'{datetime.datetime.now()} - {hostname} does not exist')
        except dns.resolver.NoAnswer:
            print(f'{datetime.datetime.now()} - {hostname} does not have any TXT records')
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Monitor DNS TXT records')
    parser.add_argument('--hostname', type=str, default='futurestay.com', help='The hostname to monitor')
    parser.add_argument('--interval', type=int, default=5, help='The interval in seconds between DNS queries')
    parser.add_argument('--substring', type=str, default='google-site',
                        help='The substring to search for in the TXT records')

    args = parser.parse_args()

    monitor_dns(hostname=args.hostname, interval=args.interval, substring=args.substring)
