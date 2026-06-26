from controllers.media_controller import MediaController

media = MediaController()

print("=" * 50)
print(" UNIVERSAL MEDIA CONTROLLER TEST ")
print("=" * 50)

while True:

    print("""
1 -> Play / Pause
2 -> Next Track
3 -> Previous Track
4 -> Volume Up
5 -> Volume Down
6 -> Mute
0 -> Exit
""")

    choice = input("Select : ")

    if choice == "1":
        media.play_pause()

    elif choice == "2":
        media.next_track()

    elif choice == "3":
        media.previous_track()

    elif choice == "4":
        media.volume_up()

    elif choice == "5":
        media.volume_down()

    elif choice == "6":
        media.mute()

    elif choice == "0":
        print("Exiting...")
        break

    else:
        print("Invalid Choice")