import socket
import os
def udp_s():
    uspssd_sc,Siri_dhanoosh = socket.socket(socket.AF_INET, socket.SOCK_DGRAM),('localhost', 8080)
    uspssd_sc.bind(Siri_dhanoosh)
    print("Listening UDP Server on port 8080...")
    while True:
        sdt, cadd_dfs = uspssd_sc.recvfrom(1024)
        if sdt:
            cdfms_dadd = f"image_{cadd_dfs[1]}.jpg"
            uspssd_sc.sendto(cdfms_dadd.encode(), (cadd_dfs[0], cadd_dfs[1]))
            with open("S_files/test.jpg", "rb") as dimf:
                imsd_ft = dimf.read()
            uspssd_sc.sendto(imsd_ft,(cadd_dfs[0], cadd_dfs[1]))
            print(f"Sent t file from '{cdfms_dadd}' to {cadd_dfs[0]}:{cadd_dfs[1]}")
if __name__ == "__main__":
    udp_s()
