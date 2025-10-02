def tinh_ROI(doanh_thu, chi_phi):
    if chi_phi == 0:
        return None  # Tránh chia cho 0
    roi = (doanh_thu - chi_phi) / chi_phi
    return roi

# --- Chương trình chính ---
doanh_thu = float(input("Nhập Doanh thu: "))
chi_phi = float(input("Nhập Chi phí: "))

roi = tinh_ROI(doanh_thu, chi_phi)

if roi is None:
    print("⚠️ Chi phí không thể bằng 0.")
else:
    print(f"\n📊 ROI = {roi:.2f}")
    if roi >= 0.75:
        print("✅ Nên đầu tư (ROI đạt yêu cầu).")
    else:
        print("❌ Không nên đầu tư (ROI thấp hơn mức yêu cầu).")
