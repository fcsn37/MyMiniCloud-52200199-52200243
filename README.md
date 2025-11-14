BÁO CÁO CUỐI KỲ CLOUDCOMPUTING

**Các thành phần chính:**
| Tên Dịch vụ | Công nghệ/Chức năng | Vai trò |
| :--- | :--- | :--- |
| **`api-gateway-proxy-server`** | Nginx | Cổng giao tiếp chính, Cân bằng tải |
| **`application-backend-server`** | Python | Xử lý logic nghiệp vụ chính (Core API) |
| **`web-frontend-server`** | HTML/Static Web | Giao diện người dùng Web |
| **`relational-database-server`** | MySQL/PostgreSQL (DB Relational) | Lưu trữ dữ liệu quan hệ |
| **`object-storage-server`** | Minio (dự đoán) | Lưu trữ đối tượng (ví dụ: ảnh, video) |
| **`internal-dns-server`** | DNS Server | Phân giải tên miền nội bộ giữa các dịch vụ |
| **`monitoring-prometheus-server`** | Prometheus | Giám sát các chỉ số sức khỏe của các dịch vụ |

## Yêu Cầu và Cài Đặt
Để chạy dự án này, cần cài đặt:
1. [**Docker Desktop**](https://www.docker.com/products/docker-desktop/)
2. **Git Bash** 
\

### Cách Khởi chạy
Chạy các lệnh sau tại thư mục gốc của dự án (`/Minicloud_52200243_52200199`):
1.  Clone repository này về máy cục bộ:
    ```bash
    git clone [https://github.com/fcsn27/MyMiniCloud-52200199-52200243.git](https://github.com/fcsn27/MyMiniCloud-52200199-52200243.git)
    cd MyMiniCloud-52200199-52200243
    ```
2.  Build các Images Tùy chỉnh (Web/App):
    ```bash
    docker compose build --no-cache
    ```
3.  Khởi động Toàn bộ Containers:
    ```bash
    docker compose up -d
    ```
4.  Kiểm tra trạng thái (Chắc chắn 10 Services đều UP):
    ```bash
    docker compose ps
    ```
