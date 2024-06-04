print("="*15)
print("MENGHITUNG BMI")
print("="*15)


berat_badan = float(input("Masukan berat Badan Anda (kg) :"))
tinggi_badan = float(input("Masukan tinggi Badan Anda (cm) :"))

# rumus bmi
tinggi_badan = tinggi_badan/100 
bmi = berat_badan/(tinggi_badan**2)

if bmi < 18.5:
    status = "Kurang Berat Badan"
elif bmi >=18.5 and bmi <= 22.9:
    status = "Normal"
elif bmi >=23 and bmi <=24.9:
    status = "Kelebihan berat badan"
elif bmi >= 25 and bmi<= 29.9:
    status = "Obesitas tingkat 1"
elif bmi > 30:
    status = "Obesitas tingkat 2"
    
print(f"BMI = {bmi:.2f}")
print("Status =",status)
    
    