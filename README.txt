PAKET MODUL 4.4 - 4.11 (Autentikasi + RBAC, Modular Monolith, Laravel Breeze)

SYARAT: Breeze sudah terpasang (php artisan breeze:install blade) dan npm install sudah dijalankan.

CARA PAKAI (di terminal WSL):
1. Masuk ke root proyek Laravel (folder yang ada file "artisan"):
     cd "/mnt/c/BACKEND DEV/auth-monolith"
2. Ekstrak ZIP ke folder ini, pilih timpa (overwrite) kalau ditanya:
     unzip -o /lokasi/zip/auth-lengkap.zip -d .
3. Jalankan skrip setup:
     bash setup-auth.sh
4. Terminal 1:  npm run dev
   Terminal 2:  php artisan serve
5. Tes di browser: /register, /user/dashboard, /admin/dashboard (403 untuk user biasa),
   lalu login admin@example.com / password123 dan buka /admin/dashboard.

JIKA SKRIP GAGAL DI BAGIAN bootstrap/app.php, edit manual ->withMiddleware(...) menjadi:

    ->withMiddleware(function (Middleware $middleware): void {
        $middleware->alias([
            'role' => \Modules\Auth\Middleware\RoleMiddleware::class,
        ]);
    })

Setelah selesai, file patch-project.py, setup-auth.sh, README.txt, composer.json.bak,
dan bootstrap/app.php.bak boleh dihapus (jangan di-commit).
