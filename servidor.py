#!/usr/bin/env python3
import http.server
import socketserver
import json
import os
import socket

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(DIRECTORY, "historic.json")

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

class PlantRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Permetre connexió CORS des de qualsevol dispositiu de la xarxa
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        if self.path == '/api/history':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            
            if os.path.exists(DATA_FILE):
                try:
                    with open(DATA_FILE, 'r', encoding='utf-8') as f:
                        data = f.read()
                    self.wfile.write(data.encode('utf-8'))
                except Exception as e:
                    self.wfile.write(json.dumps({}).encode('utf-8'))
            else:
                self.wfile.write(json.dumps({}).encode('utf-8'))
            return
        
        # Redirigir l'arrel a index.html
        if self.path == '/' or self.path == '':
            self.path = '/index.html'

        return super().do_GET()

    def do_POST(self):
        if self.path == '/api/history':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                body = self.rfile.read(content_length).decode('utf-8')
                parsed_json = json.loads(body)

                with open(DATA_FILE, 'w', encoding='utf-8') as f:
                    json.dump(parsed_json, f, indent=2, ensure_ascii=False)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "ok", "message": "Guardat correctament"}).encode('utf-8'))
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json; charset=utf-8')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()

def main():
    local_ip = get_local_ip()
    hostname = socket.gethostname()
    
    print("\n" + "="*60)
    print("🌿 SERVIDOR LOCAL DEL JARDÍ ENGEGAT CORRECTAMENT")
    print("="*60)
    print(f"\n📱 DES DEL MÒBIL O TAULETA (Connectat al Wi-Fi de casa):")
    print(f"👉 http://{local_ip}:{PORT}")
    if ".local" not in hostname:
        print(f"👉 http://{hostname}.local:{PORT}")
    else:
        print(f"👉 http://{hostname}:{PORT}")
    print(f"\n💻 DES D'AQUEST MAC:")
    print(f"👉 http://localhost:{PORT}")
    print("\n" + "-"*60)
    print("Prem Ctrl + C per aturar el servidor quan vulguis.")
    print("="*60 + "\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), PlantRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor aturat.")

if __name__ == "__main__":
    main()
