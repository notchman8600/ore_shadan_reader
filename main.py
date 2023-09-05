# Standard Library
import socket

try:
    sock = socket.create_connection(("koukoku.shadan.open.ad.jp", 23))
    while True:
        chunk = sock.recv(2)
        if not chunk:
            break
        try:
            print(chunk.decode("cp932"), end="")
        except Exception:
            # 文字化けした場合は握り潰す
            pass
except socket.error as e:
    print(f"Socket error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # ソケットを閉じる
    sock.close()
