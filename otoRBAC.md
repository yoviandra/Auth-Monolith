```mermaid
graph TD
    A["Request Masuk dari User"] --> B{"Apakah User Sudah Login?"}
    B -- Belum --> C["Redirect ke Halaman Login"]
    B -- Sudah --> D{"Apakah Memiliki Role yang Sesuai?"}
    D -- Tidak --> E["Tampilkan Error 403 Forbidden"]
    D -- Ya --> F["Akses Diberikan (Lanjut ke Controller)"]