
import streamlit as st

st.set_page_config(
    page_title="AI Affiliate Studio",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ AI AFFILIATE STUDIO")
st.caption("Shopee + TikTok Affiliate")

st.metric("Sasaran Komisen Harian", "RM100")

platform = st.selectbox(
    "Pilih platform",
    ["Shopee Affiliate", "TikTok Affiliate"]
)

product = st.text_input(
    "Nama produk",
    placeholder="Contoh: Lampu sensor automatik"
)

price = st.text_input(
    "Harga produk (RM)",
    placeholder="Contoh: 29.90"
)

if st.button("JANA SKRIP VIDEO"):
    if product:
        st.subheader("Skrip Promosi")

        st.write(f"""
        🎬 HOOK:
        Tengah cari {product}?

        🛍️ REVIEW:
        Produk {product} ini boleh dijadikan
        pilihan untuk kegunaan harian.
        Semak spesifikasi dan ulasan pembeli
        sebelum membuat keputusan.

        🔥 CTA:
        Klik pautan affiliate untuk lihat
        harga dan maklumat produk.
        """)

        st.success("Skrip berjaya dijana!")
    else:
        st.warning("Masukkan nama produk dahulu.")

st.divider()
st.subheader("Platform Affiliate")
st.write("Shopee: Sedia untuk dihubungkan")
st.write("TikTok: Sedia untuk dihubungkan")
