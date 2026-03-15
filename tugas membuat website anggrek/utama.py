import streamlit as st
import pandas as pd
import os

#----- STYLE CSS BINGKAI GAMBAR (ALL)(AI) -----***

st.markdown("""
    <style>
    .stImage {
        border-radius: 15px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
    }
    .stImage:hover {
        box-shadow: 0 8px 16px 0 rgba(0,0,0,0.3);
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #FFF8DC;
    }
    </style>
    """, unsafe_allow_html=True)


# Konfigurasi Halaman
st.set_page_config(page_title="Katalog Anggrek", layout="wide")

# 0. CACHE DATA (Fungsi agar pembacaan file lebih cepat)(AI)***
@st.cache_data
def muat_data():
    if os.path.exists("data_anggrek1.csv"):
        return pd.read_csv("data_anggrek1.csv")
    return None

# 1. Tampilkan Banner Canva
if os.path.exists("anggrekku.png"):
    st.image("anggrekku.png", use_container_width=True)

#{keep code} kode dari bu inung(style):
# st.title("🌸 Koleksi Anggrek Berdasarkan Kategori")

# ADJUST CSS di bagian " koleksi anggrek bedasarkan kategori(AI) " ***
# Ganti '42px' dengan angka yang lebih besar atau kecil sesuai seleramu
st.markdown(f"""
    <h1 style='text-align: left; font-size: 38px; color: #000000;'>
        🌸 Koleksi Anggrek Berdasarkan Kategori
    </h1>
    """, unsafe_allow_html=True)
st.divider()


try:
    if os.path.exists("data_anggrek1.csv"):
        df = pd.read_csv("data_anggrek1.csv")
        # Pastikan kolom 'foto' tidak kosong
        df = df.dropna(subset=['foto'])

        daftar_kategori = df['kategori'].unique()

        for kat in daftar_kategori:
            st.header(f"🌿 Anggrek Jenis {kat.capitalize()}")
            data_per_kat = df[df['kategori'] == kat]

            # Membuat grid 4 kolom
            cols = st.columns(4)

            for index, row in data_per_kat.reset_index().iterrows():
                nama_foto = str(row['foto']).strip()

                with cols[index % 4]:
                    if os.path.exists(nama_foto):
                        st.image(nama_foto, use_container_width=True)
                        st.subheader(row['nama'])
                        
                        # --- HARGA & STATUS DENGAN FONT LEBIH BESAR ---
                        #{keep code}st.markdown(f"### **Rp {row['harga']:,}**")
                        #{keep code}st.markdown(f"**Status:** {row['status']}")


                        # --- HARGA ---***
                        st.markdown(f"### **Rp {row['harga']:,}**")

                        # --- STATUS DENGAN LOGIKA WARNA (EFEK KEDUA) ---***
                        status_text = str(row['status']).strip()
                        
                        # Tentukan warna: Hijau jika Tersedia, Merah jika selain itu ***
                        warna_bg = "#2E7D32" if status_text.lower() == "tersedia" else "#C62828"

                        st.markdown(f"""
                            <div style="
                                background-color: {warna_bg}; 
                                color: white; 
                                padding: 5px 12px; 
                                border-radius: 50px; 
                                text-align: center; 
                                font-weight: bold; 
                                font-size: 13px; 
                                display: inline-block;
                                margin-bottom: 15px;
                            ">
                                {status_text.upper()}
                            </div>
                            """, unsafe_allow_html=True)
                        
                        
                    else:
                        st.warning(f"Foto {nama_foto} tidak ditemukan")
            st.divider()

    else:
        st.error("File 'data_anggrek1.csv' tidak ditemukan!")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")

# --- BAGIAN KONTAK & ALAMAT (FOOTER) ---
st.write("") # Memberi ruang kosong
st.write("")
st.divider()

st.subheader("📞 Hubungi Kami")
col_info1, col_info2 = st.columns(2)

with col_info1:
    st.markdown("""
    **Alamat Galeri:** Jl. C. Simanjuntak No.60, Terban, Kec. Gondokusuman, Kota Yogyakarta, Daerah Istimewa Yogyakarta 55223
    """)

#Jl. Anggrek Indah No. 123,  Kecamatan Bunga, Kota Flora, Jawa Barat.

with col_info2:
    # Ganti nomor HP di bawah ini dengan nomor Anda (gunakan format 62)
    no_hp = "6282134952220"
    pesan_wa = "Halo, saya tertarik memesan anggrek di katalog Anda."
    # Mengonversi spasi menjadi format URL (%20)
    link_wa = f"https://wa.me/{no_hp}?text={pesan_wa.replace(' ', '%20')}"

    st.markdown(f"**WhatsApp:**")
    st.link_button("💬 Pesan Sekarang via WhatsApp", link_wa)
    st.caption("© 2026 Toko Anggrek Digital - Semua Hak Dilindungi")

    # Cara merunning file :
    # 1. new terminal
    # 2. run and debugging
    # 3. clear terminal
    # 4. ketik di terminal ( streamlit run utama.py)
    # and finally langsung ke localhost
    # CORNGRATZZ 😎🤗
    
    