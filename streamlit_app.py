import streamlit as st
import pandas as pd

# Inisialisasi session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "form_data" not in st.session_state:
    st.session_state.form_data = {}

# Fungsi navigasi
def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

# Halaman 1: Umum
if st.session_state.step == 1:
    st.title("Pelaporan Limbah Industri - Halaman 1")
    
    st.session_state.form_data["tanggal"] = st.date_input("Tanggal Pelaporan")
    st.session_state.form_data["jenis_limbah"] = st.selectbox("Jenis Limbah", ["Cair", "Padat", "Gas"])
    
    if st.button("Lanjut"):
        next_step()

# Halaman 2: Berdasarkan jenis limbah
elif st.session_state.step == 2:
    st.title("Input Limbah - Halaman 2")
    jenis = st.session_state.form_data.get("jenis_limbah")

    if jenis == "Cair":
        st.session_state.form_data["teknologi_pengolahan"] = st.text_input("Jenis Pengolahan")
        st.session_state.form_data["proses_pengolahan"] = st.selectbox("Proses Pengolahan", ["Primer", "Sekunder", "Tersier"])
        st.session_state.form_data["kapasitas_ipal"] = st.number_input("Kapasitas IPAL (m³/hari)")
        st.session_state.form_data["debit_limbah"] = st.number_input("Debit Limbah yang Diolah (m³/detik)")

    elif jenis == "Padat":
        st.session_state.form_data["jenis_limbah_padat"] = st.selectbox("Jenis Limbah Padat", ["B3", "Non B3"])
        st.session_state.form_data["cara_pengolahan"] = st.text_input("Cara Pengolahan")
        st.session_state.form_data["volume_per_minggu"] = st.number_input("Volume Limbah /minggu (kg)")
        st.session_state.form_data["lokasi_penyimpanan"] = st.text_input("Lokasi Penyimpanan Sementara")

    elif jenis == "Gas":
        st.session_state.form_data["teknologi_pengendalian"] = st.text_input("Teknologi Pengendalian Emisi")
        st.session_state.form_data["jenis_gas"] = st.text_input("Jenis Gas yang Ditangani")

    st.button("Kembali", on_click=prev_step)
    st.button("Lanjut", on_click=next_step)

# Halaman 3: Pengawasan
elif st.session_state.step == 3:
    st.title("Pengawasan - Halaman 3")
    jenis = st.session_state.form_data.get("jenis_limbah")

    if jenis == "Cair":
        st.session_state.form_data["ph"] = st.number_input("pH")
        st.session_state.form_data["suhu"] = st.number_input("Suhu (°C)")
        st.session_state.form_data["parameter_uji"] = st.text_area("Parameter Uji")
        st.session_state.form_data["cara_pengawetan"] = st.text_input("Cara Pengawetan")
        st.session_state.form_data["expired"] = st.date_input("Tanggal Kadaluwarsa")

    elif jenis == "Padat":
        st.session_state.form_data["pengawasan_uji"] = st.multiselect(
            "Pilihan Uji", ["Kandungan Bahan Berbahaya", "Uji TCLP", "Kadar Air & Bahan Organik"]
        )

    elif jenis == "Gas":
        st.session_state.form_data["konsentrasi_gas"] = st.number_input("Konsentrasi Gas Buang")
        st.session_state.form_data["parameter_gas"] = st.text_input("Parameter")

    st.button("Kembali", on_click=prev_step)
    if st.button("Simpan dan Tampilkan Data"):
        next_step()

# Halaman 4: Tabel Rekap
elif st.session_state.step == 4:
    st.title("Rekap Pelaporan Limbah Industri")
    df = pd.DataFrame([st.session_state.form_data])
    st.dataframe(df)

    if st.button("Mulai Ulang"):
        st.session_state.step = 1
        st.session_state.form_data = {}

import streamlit as st

# CSS untuk background warna
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    </style>
""", unsafe_allow_html=True)
