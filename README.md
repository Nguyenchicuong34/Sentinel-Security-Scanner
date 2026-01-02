# Sentinel-Security-Scanner
Advanced Python Vulnerability Scanner with GUI &amp; Multithreading (Project at HUIT)
#  Sentinel - Advanced Vulnerability Scanner

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

**Sentinel** là một công cụ kiểm thử bảo mật tự động (Automated Penetration Testing Tool) được phát triển nhằm hỗ trợ quản trị viên hệ thống rà soát lỗ hổng bảo mật Web và Mạng.

Project này được xây dựng bằng **Python** với giao diện đồ họa hiện đại (GUI) sử dụng **CustomTkinter**, áp dụng kỹ thuật đa luồng (Multithreading) để tối ưu hiệu suất.

##  Tính năng nổi bật

* ** Reconnaissance:** Tự động thu thập thông tin server, phân tích `robots.txt`, nhận diện công nghệ (Banner Grabbing).
* ** Network Scanning:** Quét các cổng mở (Open Ports) và dịch vụ đang chạy (Service Detection).
* **website Vulnerability Scan:**
    * Phát hiện lỗi **SQL Injection** (Time-based & Error-based).
    * Phát hiện lỗi **XSS Reflected**.
    * Kiểm tra các **Security Headers** (X-Frame-Options, CSP...).
* ** Directory Busting:** Tự động tìm kiếm các thư mục ẩn, file backup, trang admin nhạy cảm.
* ** Reporting:** Xuất báo cáo chi tiết dạng `.txt` với thời gian thực.
* ** Performance:** Sử dụng Multithreading để đảm bảo giao diện mượt mà, không bị treo khi quét.

##  Giao diện (Screenshots)

*(demo_dashboard.jpg)*

##  Cài đặt & Sử dụng

1.  **Clone dự án:**
    ```bash
    git clone [https://github.com/NguyenChiCuong-HUIT/Sentinel-Scanner.git](https://github.com/NguyenChiCuong-HUIT/Sentinel-Scanner.git)
    cd Sentinel-Scanner
    ```

2.  **Cài đặt thư viện:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Chạy chương trình:**
    ```bash
    python main.py
    ```

##  Disclaimer (Miễn trừ trách nhiệm)

Công cụ này được phát triển cho mục đích **học tập và nghiên cứu An toàn thông tin**. Tác giả không chịu trách nhiệm cho bất kỳ hành vi sử dụng trái phép nào vào các hệ thống không thuộc quyền sở hữu của người dùng.

---
**Developed by Nguyen Chi Cuong (HUIT - Information Security)**
