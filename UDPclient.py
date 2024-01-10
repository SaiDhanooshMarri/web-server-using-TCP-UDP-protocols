import socket
def udp_c(Siri_dhanoosh):
    uspssd_sc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:   
        uspssd_sc.sendto(b"request", Siri_dhanoosh)
        bffsz_s = 8192
        fcdsn,_ = uspssd_sc.recvfrom(bffsz_s)
        sdt,_ = uspssd_sc.recvfrom(bffsz_s)
        fcdsn=str(fcdsn)
        fcdsn=fcdsn.split("'")
        with open(f"C_files/{fcdsn[1]}", "wb") as dimf:   
            dimf.write(sdt)
        print(f"Saved the received image as '{fcdsn[1]}'")
    finally:
        uspssd_sc.close()
if __name__ == "__main__":
    Siri_dhanoosh = ("localhost", 8080)  
    udp_c(Siri_dhanoosh)
