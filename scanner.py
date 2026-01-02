import socket
import threading
import requests
from core.utils import Utils
import time

class SentinelScanner:
    def __init__(self, target_url, log_callback, progress_callback):
        self.target_url = target_url
        self.log_callback = log_callback
        self.progress_callback = progress_callback # Hàm cập nhật thanh tiến trình
        
        self.full_domain, self.base_domain = Utils.get_domain_info(target_url)
        self.ip = Utils.get_ip_address(self.full_domain)
        self.stop_event = False

    def log(self, message):
        if self.log_callback: self.log_callback(message)

    def update_prog(self, value):
        if self.progress_callback: self.progress_callback(value)

    # --- 1. INFO GATHERING (10% - 30%) ---
    def scan_recon(self):
        self.log(f"\n[PHASE 1] RECONNAISSANCE & INFO GATHERING...")
        
        # Check robots.txt
        try:
            robots_url = f"{self.target_url.rstrip('/')}/robots.txt"
            res = requests.get(robots_url, timeout=3)
            if res.status_code == 200:
                self.log(f"[INFO] Tìm thấy robots.txt. Đang phân tích...")
                disallowed = [line for line in res.text.split('\n') if 'Disallow' in line]
                if disallowed:
                    self.log(f"   -> {len(disallowed)} đường dẫn bị ẩn khỏi Google (Nơi nhạy cảm).")
            else:
                self.log("[INFO] Không tìm thấy robots.txt")
        except: pass
        
        self.update_prog(0.2) # 20%

    # --- 2. NETWORK SCAN & BANNER GRABBING (30% - 60%) ---
    def scan_network(self):
        if not self.ip: return
        self.log(f"\n[PHASE 2] NETWORK SCANNING & SERVICE DETECTION...")
        
        ports = [21, 22, 25, 53, 80, 443, 3306, 8080]
        step = 0.3 / len(ports) # Tính % cho mỗi port
        current_prog = 0.3

        for port in ports:
            if self.stop_event: break
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                res = s.connect_ex((self.ip, port))
                if res == 0:
                    # Banner Grabbing: Thử nhận tin nhắn chào từ server
                    try:
                        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                        banner = s.recv(1024).decode().strip().split('\n')[0]
                    except:
                        banner = "Unknown Service"
                    
                    self.log(f"[+] OPEN PORT {port}: {banner}")
                s.close()
            except: pass
            
            current_prog += step
            self.update_prog(current_prog)

    # --- 3. WEB VULNERABILITY (60% - 90%) ---
    def scan_web_vulns(self):
        self.log(f"\n[PHASE 3] WEB VULNERABILITY ASSESSMENT...")
        
        # Header Checks
        try:
            res = requests.get(self.target_url, timeout=3)
            headers = res.headers
            if 'X-Powered-By' in headers:
                self.log(f"[WARN] Lộ thông tin công nghệ: {headers['X-Powered-By']}")
            if 'Server' in headers:
                self.log(f"[WARN] Lộ thông tin Server: {headers['Server']}")
        except: pass
        self.update_prog(0.7)

        # Advanced SQLi Check (Time-based Blind simulation)
        self.log("[*] Đang kiểm tra SQL Injection nâng cao...")
        sqli_patterns = ["'", '"', " OR 1=1", "' OR '1'='1"]
        vuln_found = False
        if "=" in self.target_url:
            for p in sqli_patterns:
                try:
                    # Test đơn giản bằng phản hồi lỗi
                    r = requests.get(f"{self.target_url}{p}", timeout=2)
                    if "mysql" in r.text.lower() or "syntax" in r.text.lower():
                        self.log(f"[CRITICAL] SQL INJECTION DETECTED: {p}")
                        vuln_found = True
                        break
                except: pass
        
        if not vuln_found: self.log("[OK] Không tìm thấy lỗi SQLi cơ bản.")
        self.update_prog(0.85)

        # XSS Check
        self.log("[*] Đang kiểm tra XSS Reflected...")
        xss_payload = "<script>console.log('Sentinel')</script>"
        try:
            r = requests.get(f"{self.target_url}{xss_payload}", timeout=2)
            if xss_payload in r.text:
                self.log(f"[HIGH] XSS FOUND: Payload được phản hồi nguyên vẹn.")
            else:
                self.log("[OK] An toàn trước XSS Reflected cơ bản.")
        except: pass
        self.update_prog(0.95)

    def start_full_scan(self):
        self.log(f"[*] KHỞI ĐỘNG SENTINEL V3.0 - TARGET: {self.full_domain}")
        self.update_prog(0.05) # Bắt đầu

        # Chạy tuần tự các pha
        self.scan_recon()
        self.scan_network()
        self.scan_web_vulns()

        self.update_prog(1.0) # 100%
        self.log("\n=== [COMPLETED] QUÁ TRÌNH QUÉT HOÀN TẤT ===")