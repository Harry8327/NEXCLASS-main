import streamlit as st

def subject_card(name,code,section,stats=None,footer_callback=None):
    html=f"""
    <div style="background:white; border-left:6px solid #EB459E;padding:30px 30px 30px 24px; border-radius:20px; border:1px solid black; margin-bottom:25px">
    <h3 style="margin:0; color: #1e293b; font-size:1.5 rem; ">{name}</h3>
    <p style="color:#64748b;margin:10px 0;">Code :<span style="background: #E0E3FF; color: #5865F2;padding: 2px 8px; border_radius:5px;"> {code} </span> | Section : {section}</p>
    
    """
    if stats:
        html+=f"""
        <div style="display:flex;gap:12px; flex-wrap:wrap; margin-top:18px">
        """
        for icon,label,value in stats:
            html+=f'<div style="background:#EB459E10; padding:8px 14px;border-radius:12px; font-size:0.9rem">{icon} <b>{value}</b> {label} </div>'
        html+='</div>'
    st.html(html)

    if footer_callback:
        footer_callback()