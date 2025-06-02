import streamlit as st
import strategy_core
import alert_engine

st.title("📈 Fx Bot2.0 - TradingView Strategy Assistant")

st.markdown("### Paste Webhook Data (JSON from TradingView)")
webhook_data = st.text_area("Webhook JSON", height=300)

if st.button("Analyze Setup"):
    if webhook_data:
        signal = strategy_core.analyze_webhook(webhook_data)
        if signal:
            st.success(f"✅ Trade Setup Found: {signal}")
            alert_engine.send_alert(signal)
        else:
            st.warning("⚠️ No valid setup detected.")
    else:
        st.error("❌ Please paste some webhook data.")