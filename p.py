import sys

def replace_delimiter(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            data = file.read()

        # Replace '|' with ':'
        modified_data = data.replace('|', ':')

        # Save to output file
        with open(output_file, 'w') as file:
            file.write(modified_data)

        print(f"File '{input_file}' telah diproses dan disimpan ke '{output_file}' dengan format yang diubah.")

    except FileNotFoundError:
        print(f"File '{input_file}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 p.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        replace_delimiter(input_file, output_file)