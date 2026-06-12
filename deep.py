def main():
   answer = input("What is the meaning of the universe? ").strip().lower()
   match answer:
      case "42" | "forty-two" | "forty two":
         print("Yes")
      case _:
         print("No")
main()
