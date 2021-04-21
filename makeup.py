
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from proxy_checker import ProxyChecker
from termcolor import cprint
from pyfiglet import figlet_format

# aesthetics in terminal
greet = "ProxyBeautify"
cprint(figlet_format(greet), "cyan")
owner = "we are all mad here"
cprint(figlet_format(owner, font="digital"), "cyan")

################################################################################

# interactive output proxy format choice
def scrap():
    cprint("choose an output format", "cyan")
    cprint("[1] full format", "cyan")
    cprint("[2] proxychains format (protocol:ip:port)", "cyan")
    print_input_format = input()
    format_choice = ['1', '2']
    if print_input_format in format_choice:
        return print_input_format
    else:
        print('')
        cprint(f"!!! choose a valid option !!!", "cyan")
        print('')
        return scrap()
        
################################################################################

# program execution.
output_format = scrap()

print('')
cprint('slaves are working, may take some time...', "cyan")
print('')

scraper = Scrapper(category='ALL', print_err_trace=False)
data = scraper.getProxies()

for result in data.proxies:
    to_scan = f'{result.ip}:{result.port}'

    checker = ProxyChecker()
    done = checker.check_proxy(to_scan)

    if done != False:
        protocol = done['protocols']
        for p in protocol:
            cleaned_protocol = p.translate({ord("["): None})
        country_code = done['country_code']

        proxy = f'{cleaned_protocol}  {result.ip}  {result.port}'
        country = done['country']
        anonymous = done['anonymity']
        timeout = done['timeout']

        full_format = f"{proxy} ====> {country}|{country_code}|{anonymous}|timeout( {timeout} )"

        if output_format == '1':
            cprint(full_format, "cyan")
        else:
            cprint(proxy, "cyan")
