# Otomasi-Jaringan
Script Python untuk menonaktifkan network interface yang tidak diperlukan secara otomatis.
# Auto Disable Unused Network Interfaces

Script Python untuk **menonaktifkan network interface yang tidak diperlukan secara otomatis** di sistem Linux.

---

## ⚙️ Fitur
- Mengecek semua interface menggunakan `ip -br link`
- Melewati interface penting (`lo`, dan yang `UP`)
- Menampilkan daftar interface yang akan dinonaktifkan
- Meminta konfirmasi sebelum eksekusi
- Menonaktifkan interface `DOWN` atau `UNKNOWN` secara otomatis

## Cara menggunakan:
1. Simpan file dengan nama: nano auto_disable_with_preview.py
2. Beri izin eksekusi: chmod +x auto_disable_with_preview.py
3. Jalankan dengan hak akses root: sudo python3 auto_disable_with_preview.py

## COntoh outputnya:
🔍 Mengecek status network interface...

✅ Interface aktif (dibiarkan):
   - enp0s3 (UP)

⚠️  Interface yang terdeteksi tidak aktif / tidak diperlukan:
   - dummy0 (UNKNOWN)

Apakah kamu ingin menonaktifkan interface di atas? (y/n): y

🚧 Menonaktifkan interface yang tidak diperlukan...

🔴 Interface 'dummy0' telah dinonaktifkan.

✅ Semua interface tidak diperlukan telah dinonaktifkan.
