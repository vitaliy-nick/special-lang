from Classes.ascii_art_service import AsciiArtService
from Classes.cylinder import Cylinder


def user_interface():
    ascii_art_service = AsciiArtService()

    while True:
        ascii_art_service.display_ascii_art()

        print("\n Main menu:")
        print("1. Select shape, cube or cylinder.")
        print("2. Select size.")
        print("3. Set height, only for cylinder.")
        print("4. Rotate shape.")
        print("5. Save ASCII-art in file.")
        print("6. Select color.")
        print("7. Exit.")
        choice = input("Select option: ").strip()

        match choice:
            case '1':
                shape_type = input("Select shape, cube or cylinder: ").strip().lower()
                size = int(input("Enter size of shape: "))
                height = int(input("Enter height of cylinder: ")) if shape_type == "cylinder" else None
                ascii_art_service.set_shape(shape_type, size, height)
            case '2':
                size = int(input("Enter new size: "))
                if ascii_art_service.shape:
                    ascii_art_service.shape.size = size
            case '3':
                if isinstance(ascii_art_service.shape, Cylinder):
                    height = int(input("Enter new height of cylinder: "))
                    ascii_art_service.shape.height = height
                else:
                    print("Changing the height is available only for the cylinder!")
            case '4':
                angle_x = float(input("Enter rotation about X in degrees: "))
                angle_y = float(input("Enter rotation about Y in degrees: "))
                angle_z = float(input("Enter rotation about Z in degrees: "))
                ascii_art_service.rotate_shape(angle_x, angle_y, angle_z)
            case '5':
                filename = input("Enter name file for save ASCII-art with extension .txt: ")
                ascii_art_service.save_to_file(filename)
            case '6':
                print("Available colors:", ", ".join(ascii_art_service.color_service.list_colors()))
                color_name = input("Select color: ").strip()
                ascii_art_service.set_color(color_name)
            case '7':
                print("Exit!")
                break
            case _:
                print("Incorrect option: Please, try again!")
