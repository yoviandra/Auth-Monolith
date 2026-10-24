```mermaid
sequenceDiagram
    autonumber
    participant Browser as Browser (Client)
    participant Server as Server (Laravel)
    participant Store as Session Store

    Browser->>Server: POST /login (email, password)
    activate Server
    Server->>Server: Verifikasi Kredensial
    Server->>Store: Simpan session (user_id)
    Store-->>Server: Session ID
    Server-->>Browser: Set-Cookie: session_id=xxx + Response Login Berhasil
    deactivate Server

    Note over Browser,Server: Request Halaman yang Dilindungi (Protected Route)

    Browser->>Server: GET /dashboard (Cookie: session_id=xxx)
    activate Server
    Server->>Store: Verifikasi session_id
    Store-->>Server: User ditemukan
    Server-->>Browser: Halaman Dashboard
    deactivate Server