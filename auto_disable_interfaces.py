#!/usr/bin/env python3
import subprocess

def run_cmd(cmd):
    """Jalankan perintah shell dan ambil output."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def get_interfaces():
    """Ambil daftar semua interface dan statusnya."""
    data = run_cmd("ip -br link")
    interfaces = []
    for line in data.splitlines():
        parts = line.split()
        if len(parts) >= 2:
            name = parts[0]
            state = parts[1]
            interfaces.append((name, state))
    return interfaces

def disable_interface(name):
    """Menonaktifkan interface dengan perintah ip."""
    cmd = f"sudo ip link set {name} down"
    subprocess.run(cmd, shell=True)
    print(f"🔴 Interface '{name}' telah dinonaktifkan.")

def main():
    print("🔍 Mengecek status network interface...\n")
    interfaces = get_interfaces()

    to_disable = []
    active = []

    for name, state in interfaces:
        if name == "lo":
            continue  # skip loopback
        if state.upper() in ["DOWN", "UNKNOWN"]:
            to_disable.append((name, state))
        else:
            active.append((name, state))

    # Tampilkan hasil pemeriksaan
    print("✅ Interface aktif (dibiarkan):")
    for name, state in active:
        print(f"   - {name} ({state})")

    print("\n⚠️  Interface yang terdeteksi tidak aktif / tidak diperlukan:")
    if to_disable:
        for name, state in to_disable:
            print(f"   - {name} ({state})")
    else:
        print("   Tidak ada interface yang perlu dinonaktifkan.")
        print("\n✅ Selesai! Semua interface dalam kondisi baik.")
        return

    # Konfirmasi sebelum menonaktifkan
    confirm = input("\nApakah kamu ingin menonaktifkan interface di atas? (y/n): ").strip().lower()
    if confirm == "y":
        print("\n🚧 Menonaktifkan interface yang tidak diperlukan...\n")
        for name, state in to_disable:
            disable_interface(name)
        print("\n✅ Semua interface tidak diperlukan telah dinonaktifkan.")
    else:
        print("\n❎ Tidak ada perubahan yang dilakukan. Interface tetap seperti semula.")

if __name__ == "__main__":
    main()
