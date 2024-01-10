import socket
import os
def tcp_s():
    dhanoosh_t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Siri_dhanoosh = ('localhost', 8080)
    dhanoosh_t.bind(Siri_dhanoosh)
    dhanoosh_t.listen(1)
    print("Listening TCP Server on port 8080...")
    while True:
        csdf_s, cadd_dfs = dhanoosh_t.accept()
        print(f"Connection as been accepted from {cadd_dfs[0]}:{cadd_dfs[1]}")
        try:
            cdfms_dadd = f"image_{cadd_dfs[1]}.jpg"
            csdf_s.send(cdfms_dadd.encode())
            with open("S_files/g.jpg", "rb") as dimf:
                imsd_ft = dimf.read()
            csdf_s.send(imsd_ft)
            print(f"Sent the file from '{cdfms_dadd}' to {cadd_dfs[0]}:{cadd_dfs[1]}")
        except Exception as sd:
            print(f"Error: {sd}")
        finally:
            csdf_s.close()

if __name__ == "__main__":
    tcp_s()
