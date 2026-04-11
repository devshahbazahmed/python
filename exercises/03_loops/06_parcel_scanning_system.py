# This function will be tested automatically.
# Do not change the function name or parameters.
def scan_parcels(parcel_codes: list[str]) -> list[str]:
    scan_messages = []
    for barcode in parcel_codes:
        if barcode == "DAMAGED":
            scan_messages.append(f"Skipped damaged parcel")
            continue
        if barcode == "STOP":
            scan_messages.append(f"Critical error: Stopping scan")
            break
        scan_messages.append(f"Scanned parcel: {barcode}")
    
    else:
        scan_messages.append(f"All parcels scanned successfully")
    return scan_messages

print(scan_parcels(["DAMAGED", "GOOD", "GOOD", "STOP"]))