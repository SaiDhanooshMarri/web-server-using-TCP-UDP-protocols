import socket
def tcp_c(Siri_dhanoosh):
    dhanoosh_t = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        dhanoosh_t.connect(Siri_dhanoosh)
        dfms = dhanoosh_t.recv(1024).decode()
        sdt = dhanoosh_t.recv(8192)
        with open(f"C_files/{dfms}", "wb") as dimf:
            dimf.write(sdt)
        print(f"Saved the received image as '{dfms}'")
    except Exception as hd:
        print(f"Error: {hd}")
    finally:
        dhanoosh_t.close()
if __name__ == "__main__":
    Siri_dhanoosh = ("localhost", 8080) 
    tcp_c(Siri_dhanoosh)
