import nmap

nm = nmap.PortScanner()

# Input for the target host
target_host = input("Please enter a target host:\n")

# Takes input for default scan or custom scan
scan_Options = ''
while scan_Options not in ('1', '2'):
    scan_Options = input(
        "Choose an option:\n1 - Default Scan\n2 - Custom Scan\n")
    if (scan_Options == '1'):
        nmap_Arguments = "-p- -sS"
    elif (scan_Options == '2'):
        nmap_Arguments = input(
            "Enter your custom arguments separated by spaces:\n")
    else:
        print("Enter a valid option")

# Performs a scan with the arguments on the target host
tcp_scan = nm.scan(target_host, arguments=nmap_Arguments)
print("Beginning scan on " + target_host +
      "...\n")

# Check if any open TCP ports were found if not then performs scan with -Pn option
if tcp_scan["scan"][target_host]["tcp"]:
    print("Open TCP ports found:")
    for port in tcp_scan["scan"][target_host]["tcp"]:
        print("Port {}: {}".format(
            port, tcp_scan["scan"][target_host]["tcp"][port]["name"]))
else:
    print("No open TCP ports found. Performing scan with -Pn option.")

    # Concatenates nmap_Arguments with -Pn and performs scan
    nmap_Arguments += " -Pn"
    pn_scan = nm.scan(target_host, arguments=nmap_Arguments)

    # Print the results of the -Pn scan
    print("Scan results with -Pn option:")
    print(pn_scan["scan"][target_host])
