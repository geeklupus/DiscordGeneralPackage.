import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="CV - Muhammad Patel", page_icon=":briefcase:", layout="centered")

# --- MAIN CONTENT AREA ---
col1, col2 = st.columns([1, 2])  # Adjust column ratio as needed for profile and experience

# --- LEFT COLUMN (PROFILE & CONTACT INFORMATION) ---
with col1:
    # Profile Picture
    st.image("data/11zon_cropped.png", width=130)  # Replace with the correct path to your image
    
    st.write("---")
    # Profile Summary
    st.write("## Profil")
    st.write("""
    Ilmu Pengetahuan Sosial (IPS) merupakan disiplin ilmu yang mempelajari fenomena sosial di masyarakat. IPS menggabungkan berbagai cabang ilmu seperti sosiologi, antropologi, sejarah, geografi, ekonomi, dan ilmu politik untuk memahami kompleksitas hubungan manusia dalam berbagai konteks sosial dan budaya.
    """)
    
    # Education
    st.write("## Edukasi")
    st.markdown("""
    **Mardi Yuana Sukabumi**  
    Sekolah Menengah Atas (2019-2022)
    """)

    # Contact Information
    st.markdown("""
    - 📞 **Telepon:** +62-857-2385-5483
    - 📧 **Email:** febrianlupus15@gmail.com
    - 📍 **Alamat:** Indonesia, Jawa Barat, Sukabumi, Nagrak
    """)

# --- RIGHT COLUMN (NAME, TITLE & EXPERIENCE) ---
with col2:
    # Name and Title
    st.title("Lukas Febrian Laufra")
    st.subheader("Ilmu Pengetahuan Sosial")

    st.write("---")
    # Work Experience
    st.write("## Pengalaman")
    st.markdown("""
    - **Observasi Lingkungan Sekitar**  
      IPS (8 Agustus - 9 September 2019)
    
    - **Wawancara dengan Anggota Komunitas**  
      IPS (19 September - 10 Desember 2020)
    
    - **Mengikuti Diskusi atau Webinar tentang Isu Sosial**  
      IPS (1 Januari - 4 April 2021)
    """)
    
    # Languages
    st.write("## Bahasa")
    st.markdown("""
    - **Indonesia**
    """)

    # Hobbies
    st.write("## Hobi")
    st.markdown("""
    - **🎮 Game:**
                Free Fire  dan 
                Mobile Legends
    - **🎵 Music:**
                Pop,
                Dangdut,  dan  
                Hiphop
    - **🏊 Swim:**
                Teknik Mengapung  dan  
                Gaya Bebas

    """)

# --- FOOTER ---
st.write("---")
st.markdown("Made with ❤️ using Streamlit")
