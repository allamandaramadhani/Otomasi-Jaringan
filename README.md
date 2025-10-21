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

