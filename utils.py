import tldextract
import validators
import socket
import os
from datetime import datetime

class Utils:
    @staticmethod
    def is_valid_url(url):
        """Kiểm tra xem URL người dùng nhập có đúng định dạng không"""
        if not url:
            return False
        # validators giúp kiểm tra URL cực nhanh và chuẩn
        return validators.url(url)

    @staticmethod
    def get_domain_info(url):
        """Tách thông tin domain chuyên nghiệp bằng tldextract"""
        # tldextract xử lý tốt các domain phức tạp như .co.uk, .com.vn
        extracted = tldextract.extract(url)
        domain = f"{extracted.domain}.{extracted.suffix}"
        subdomain = extracted.subdomain
        full_domain = f"{subdomain}.{domain}" if subdomain else domain
        return full_domain, domain

    @staticmethod
    def get_ip_address(domain):
        """Chuyển đổi tên miền sang địa chỉ IP"""
        try:
            return socket.gethostbyname(domain)
        except socket.gaierror:
            return None

    @staticmethod
    def save_report_to_file(content):
        """Lưu báo cáo ra file txt"""
        # Tạo thư mục reports nếu chưa có
        if not os.path.exists("reports"):
            os.makedirs("reports")
            
        filename = f"reports/Sentinel_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            return filename
        except Exception as e:
            return None
