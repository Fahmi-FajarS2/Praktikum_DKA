# Input
celsius = float(input("Masukkan suhu dalam Celsius: "))

# Rumus Konversi suhu
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Output
print("\n===== HASIL KONVERSI SUHU =====")
print(f"Suhu dalam Fahrenheit : {fahrenheit:.2f} F")
print(f"Suhu dalam Kelvin : {kelvin:.2f} K")