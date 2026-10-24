#!/usr/bin/env bash
# Jalankan dari ROOT proyek Laravel (folder yang berisi file "artisan")
set -e

if [ ! -f artisan ]; then
  echo "ERROR: file 'artisan' tidak ditemukan. Jalankan skrip ini dari root proyek Laravel."
  exit 1
fi

echo "== 1/5 Patch composer.json dan bootstrap/app.php =="
python3 patch-project.py

echo "== 2/5 Refresh autoload =="
composer dump-autoload

echo "== 3/5 Bersihkan cache =="
php artisan optimize:clear

echo "== 4/5 Migrasi database dan seeder =="
php artisan migrate --force
php artisan db:seed --class=AdminUserSeeder --force

echo "== 5/5 Cek route =="
php artisan route:list --path=dashboard

echo ""
echo "SELESAI. Restart 'php artisan serve' lalu buka http://localhost:8000/login"
echo "Admin : admin@example.com / password123"
echo "User  : user@example.com  / password123"
