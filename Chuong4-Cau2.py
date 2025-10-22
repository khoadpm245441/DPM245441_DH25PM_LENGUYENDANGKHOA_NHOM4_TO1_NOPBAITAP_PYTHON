from random import randrange

while True:
    somay = randrange(1, 101)   # Máy random số từ 1..100
    solandoan = 0
    win = False

    while solandoan < 7:
        solandoan += 1
        songuoi = int(input("Máy đã chọn [1..100], mời bạn đoán: "))
        print("👉 Bạn đoán lần thứ", solandoan)

        if songuoi == somay:
            print("🎉 Chúc mừng bạn đoán đúng! Số máy là:", somay)
            win = True
            break
        elif songuoi < somay:
            print("❌ Bạn đoán sai, số máy > số bạn")
        else:
            print("❌ Bạn đoán sai, số máy < số bạn")

    # Nếu sau 7 lần vẫn chưa đoán đúng thì Game Over
    if not win:
        print("💀 GAME OVER! Số máy là:", somay)

    hoi = input("Bạn có muốn chơi tiếp không? (c/k): ").strip().lower()
    if hoi == "k":
        break

print("👋 Cám ơn bạn đã chơi Game!")
