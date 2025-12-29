import streamlit as st
import pandas as pd

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Dashboard Dosen - E Learning",
    layout="wide",
    page_icon="🎓"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 E-Learning")
st.sidebar.markdown("**Role:** Dosen")

menu = st.sidebar.radio(
    "Menu",
    [
        "Dashboard",
        "Kursus Saya",
        "Tugas & Penilaian",
        "Jadwal Mengajar",
        "Mahasiswa",
        "Pengaturan"
    ]
)

# ---------------- DATA DUMMY ----------------
kursus = pd.DataFrame({
    "Mata Kuliah": ["Cloud Computing", "AI Dasar", "Jaringan Komputer"],
    "Mahasiswa": [45, 38, 42],
    "Status": ["Aktif", "Aktif", "Aktif"]
})

tugas = pd.DataFrame({
    "Tugas": ["UTS", "Proyek Akhir", "Quiz 1"],
    "Deadline": ["2025-03-10", "2025-04-20", "2025-02-25"],
    "Sudah Dinilai": [30, 12, 40]
})

jadwal = pd.DataFrame({
    "Hari": ["Senin", "Rabu", "Jumat"],
    "Mata Kuliah": ["Cloud Computing", "AI Dasar", "Jaringan"],
    "Jam": ["08:00 - 10:00", "10:00 - 12:00", "13:00 - 15:00"]
})

# ---------------- DASHBOARD ----------------
if menu == "Dashboard":
    st.title("Dashboard Dosen")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Kursus", "3")
    col2.metric("Total Mahasiswa", "125")
    col3.metric("Tugas Aktif", "5")

    st.subheader("Kursus Aktif")
    st.dataframe(kursus, use_container_width=True)

# ---------------- KURSUS ----------------
elif menu == "Kursus Saya":
    st.title("Kursus Saya")
    st.dataframe(kursus, use_container_width=True)

    st.subheader("Tambah Kursus")
    with st.form("tambah_kursus"):
        nama = st.text_input("Nama Mata Kuliah")
        submit = st.form_submit_button("Simpan")
        if submit:
            st.success("Kursus berhasil ditambahkan (dummy)")

# ---------------- TUGAS ----------------
elif menu == "Tugas & Penilaian":
    st.title("Tugas & Penilaian")
    st.dataframe(tugas, use_container_width=True)

    st.subheader("Upload Nilai")
    st.file_uploader("Upload file nilai (.csv)", type=["csv"])

# ---------------- JADWAL ----------------
elif menu == "Jadwal Mengajar":
    st.title("Jadwal Mengajar")
    st.table(jadwal)

# ---------------- MAHASISWA ----------------
elif menu == "Mahasiswa":
    st.title("👥 Mahasiswa Terdaftar")
    st.write("Fitur detail mahasiswa (dummy)")
    st.dataframe(
        pd.DataFrame({
            "Nama": ["Andi", "Budi", "Citra"],
            "NIM": ["123", "124", "125"],
            "Status": ["Aktif", "Aktif", "Aktif"]
        }),
        use_container_width=True
    )

# ---------------- PENGATURAN ----------------
elif menu == "Pengaturan":
    st.title("⚙️ Pengaturan Akun Dosen")
    st.text_input("Nama")
    st.text_input("Email")
    st.button("Simpan Perubahan")
