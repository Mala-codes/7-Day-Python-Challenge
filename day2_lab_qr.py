import qrcode
import time

def generate_lab_banner():
    banner = """
    =========================================
    |     BIO-LAB SAMPLE QR GENERATOR       |
    |          [🧬 DATA TRACKER]            |
    =========================================
    """
    print(banner)

def main():
    generate_lab_banner()
    
    print("Initialize Lab Protocol...")
    time.sleep(1)
    
    # Getting Bioinformatics Data
    sample_id = input("Enter Sample ID (e.g., DNA-99): ")
    patient_name = input("Enter Patient/Source Initials: ")
    sample_type = input("Enter Sample Type (e.g., Blood, DNA, Protein): ")
    
    # Combine data into a professional format
    lab_data = f"SAMPLE_ID: {sample_id}\nSOURCE: {patient_name}\nTYPE: {sample_type}\nSTATUS: Verified"
    
    print(f"\n[!] Encoding data into QR Matrix...")
    
    # Create the QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(lab_data)
    qr.make(fit=True)
    
    # Create an image (Bio-Lab Colors: Blue and White)
    img = qr.make_image(fill_color="navy", back_color="white")
    
    # Save the file
    filename = f"sample_{sample_id}.png"
    img.save(filename)
    
    print("-" * 41)
    print(f"✅ SUCCESS: QR Code saved as '{filename}'")
    print(f"Scan this with your phone to see the Sample Data!")
    print("-" * 41)

if __name__ == "__main__":
    main()
