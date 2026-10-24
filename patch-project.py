import json, re, sys, shutil, os

ok = True

# 1) composer.json -> autoload PSR-4 "Modules\\"
try:
    shutil.copy("composer.json", "composer.json.bak")
    with open("composer.json", encoding="utf-8") as f:
        data = json.load(f)
    psr4 = data.setdefault("autoload", {}).setdefault("psr-4", {})
    if "Modules\\" not in psr4:
        psr4["Modules\\"] = "app/Modules/"
        with open("composer.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.write("\n")
        print("  [OK] composer.json: autoload Modules\\ ditambahkan")
    else:
        print("  [OK] composer.json: autoload Modules\\ sudah ada")
except Exception as e:
    ok = False
    print("  [GAGAL] composer.json:", e)

# 2) bootstrap/app.php -> alias middleware 'role'
alias_line = "\n        $middleware->alias([\n            'role' => \\Modules\\Auth\\Middleware\\RoleMiddleware::class,\n        ]);\n"
try:
    path = "bootstrap/app.php"
    with open(path, encoding="utf-8") as f:
        src = f.read()
    if "RoleMiddleware" in src:
        print("  [OK] bootstrap/app.php: alias role sudah ada")
    else:
        shutil.copy(path, path + ".bak")
        pattern = re.compile(r"(->withMiddleware\(\s*function\s*\(\s*Middleware\s+\$middleware\s*\)[^{]*\{)")
        if pattern.search(src):
            src = pattern.sub(lambda m: m.group(1) + alias_line, src, count=1)
            with open(path, "w", encoding="utf-8") as f:
                f.write(src)
            print("  [OK] bootstrap/app.php: alias role ditambahkan")
        else:
            ok = False
            print("  [GAGAL] bootstrap/app.php: blok ->withMiddleware(...) tidak ditemukan. Tambahkan manual (lihat README).")
except Exception as e:
    ok = False
    print("  [GAGAL] bootstrap/app.php:", e)

sys.exit(0 if ok else 1)
