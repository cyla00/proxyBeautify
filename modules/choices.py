from termcolor import cprint

class Choices:

    def format():
        cprint(f"choose an output format", 'cyan')
        cprint(f"[1] full_format (protocol|ip|port|anonimity_score|timeout|country)", 'cyan')
        cprint(f"[2] proxychains_format (protocol|ip|port)", 'cyan')
        format_choice = input()
        return format_choice

    def ouput_format(proxychains_raw_ip, protocol, raw_ips, anonymity, timeout, country, country_code, format_choice):
        if format_choice == '1':
            cprint(f"{protocol} {raw_ips}  ==> {anonymity}|timeout({timeout})     |{country}|({country_code})", 'cyan')
        elif format_choice == '2':
            cprint(f"{protocol} {proxychains_raw_ip}", 'cyan')
        else:
            cprint(f"!!! invalid input !!!", 'cyan')
            print('')
            format(proxychains_raw_ip, protocol, raw_ips, anonymity, timeout, country, country_code)
