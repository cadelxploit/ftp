GNU nano 8.2   ftp.py
import ftplib

def check_ftp_login(host, username, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(username, password)
        ftp.quit()
        return f"[SUCCESS] Logged in to {host} with {username}"
    except ftplib.error_perm as e:
        return f"[FAILED] Could not login to {host} with {username}: {e}"
    except Exception as e:
        return f"[ERROR] Error occurred for {host}: {e}"

def process_login_list(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            try:
                # Memisahkan berdasarkan tanda titik dua ":"
                host, username, password = line.strip().split(':')
                result = check_ftp_login(host, username, password)
                print(result)  # Output ke konsol
                outfile.write(result + '\n')  # Menyimpan hasil ke file
            except ValueError:
                outfile.write("[ERROR] Invalid format in line: " + line)
                print("[ERROR] Invalid format in line:", line)

# Contoh penggunaan
input_file = 'list.txt'   # File dengan daftar login FTP
output_file = 'result.txt'  # File untuk menyimpan hasil

process_login_list(input_file, output_file)