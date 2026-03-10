import streamlit as st

st.title("Thilina Kavinda")

st.subheader("Material & Nano Science Technology Researcher")

st.write("""
Research Interests:
- Nanotechnology
- Polymer Science
- Recycling Technology
- AI & IoT
""")

st.header("Education")

st.write("""
Bachelor of Engineering Technology (Hons)
Material and Nano Science Technology
Wayamba University of Sri Lanka
""")

st.header("Projects")

st.write("• UV Based Nuclear Contamination Training Device")
st.write("• Plastic Recycling Research")
st.write("• Pipe Deformation Detection System")

st.header("Download Documents")

with open("transcript.pdf","rb") as file:
    st.download_button("Download Transcript",file)

with open("cv.pdf","rb") as file:
    st.download_button("Download CV",file)
