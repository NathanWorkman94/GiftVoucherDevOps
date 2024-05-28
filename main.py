from PIL import Image, ImageDraw, ImageFont
import os
import datetime

font_path_location = os.path.join(os.path.dirname(__file__), "Fonts", "OpenSans-Regular.ttf")
bold_font_path_location = os.path.join(os.path.dirname(__file__), "Fonts", "OpenSans-Bold.ttf")
italic_font_path_location = os.path.join(os.path.dirname(__file__), "Fonts", "OpenSans-Italic.ttf")

def calculate_font_size(text, max_size=70, threshold=46, reduction_factor=1):
    """
    Calculate the font size based on the length of the text.
    param reduction_factor: How much to reduce the size per character over the threshold.
    return: The calculated font size.
    """
    if len(text) > threshold:
        return max(max_size - ((len(text) - threshold) * reduction_factor), 12)  # 12 is the minimum size
    return max_size

def create_gift_card(background_path, texts_positions, directory, file_name, font_path=font_path_location, default_font_size=70):
    """
    Creates gift card png
    :param background_path: Path to the background image.
    :param texts_positions: List of tuples (text, position, font_size) for each text to be placed.
    :param directory: Directory where the image will be saved.
    :param font_path: Path to a .ttf font file (optional, defaults to 'arial.ttf').
    :param default_font_size: Default size of the text font.
    """
    try:
        output_path = os.path.join(directory, file_name + ".png")
        print(f"Creating gift card at: {output_path}")

        with Image.open(background_path) as img:
            draw = ImageDraw.Draw(img)

            for text, position, font_size, font_path in texts_positions:
                font = ImageFont.truetype(font_path, font_size)
                draw.text(position, text, font=font, fill=(255, 255, 255))

            img.save(output_path)
        print("Gift card created successfully")

    except Exception as e:
        print(f"An error occurred: {e}")

def process_voucher(order, reference, pin, value, website, message, save_directory):
    """
    Processes the voucher creation based on the provided details.
    """
    background_path = os.path.join(os.path.dirname(__file__), "background.png")
    mannys_background_path = os.path.join(os.path.dirname(__file__), "mannys_background.png")
    sdj_background_path = os.path.join(os.path.dirname(__file__), "sdj_background.png")

    value_font_size = 180                   # Font size for the 'Value' text
    default_font_size = 70                  # Font size for other text
    default_value_position = (1320, 75)     # Default position for two digits in Value text
    shift_per_extra_digit = 60              # Pixels to shift left for each extra digit
    message_position = (180, 863)

    # Calculate the expiry date
    current_date = datetime.datetime.now()
    expiry_date = current_date + datetime.timedelta(days=3*365)  # 3 years
    formatted_expiry_date = expiry_date.strftime('%d/%m/%Y')
    expiry_position = (990, 566)

    # Check the "Website" and set the background path
    if website == 'Mannys':
        background_path = mannys_background_path
    elif website == 'Store DJ':
        background_path = sdj_background_path
    else:
        background_path = mannys_background_path  # Default background

    texts_positions = [
        ('Order: ' + str(order), (180, 566), default_font_size, font_path_location),
        ('Reference: ' + str(reference), (180, 716), default_font_size, font_path_location),
        ('Pin: ' + str(pin), (1300, 716), default_font_size, font_path_location)
    ]
    
    # Prepare the 'Value' text
    if isinstance(value, int) or value.is_integer():
        value_text = f'${int(value)}'
    else:
        value_text = f'${value}'

    num_digits = len(value_text) - 1  # Subtract 1 for the '$' character

    # Calculate the new position
    value_position_x = default_value_position[0] - shift_per_extra_digit * max(0, num_digits - 2)
    value_position = (value_position_x, default_value_position[1])

    expiry_text = f'Expiry: {formatted_expiry_date}'
    texts_positions.append((expiry_text, expiry_position, default_font_size, font_path_location))

    # Add the 'Value' text with the new position to texts_positions
    texts_positions.append((value_text, value_position, value_font_size, bold_font_path_location))

    # Check if there's a non-empty message after conversion and stripping
    if message and message.strip() != 'nan':
        full_message = message.strip()
        texts_positions.append((full_message, message_position, default_font_size, italic_font_path_location))

    # Generate file name based on the order number
    if isinstance(value, int) or value.is_integer():
        file_name = f"{website} Gift Voucher - {order} ${int(value)}"
    else:
        file_name = f"{website} Gift Voucher - {order} ${value}"

    create_gift_card(background_path, texts_positions, save_directory, file_name)

# Manual test for process_voucher
if __name__ == "__main__":
    output_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    process_voucher('1234567', '123456', '1234', 100, 'Mannys', 'Testing!', output_dir)
    output_file = os.path.join(output_dir, 'Mannys Gift Voucher - 1234567 $100.png')
    assert os.path.exists(output_file)
    print(f"Checking if file exists at: {output_file}")
    if os.path.exists(output_file):
        print(f"Test completed. Voucher created at: {output_file}")
    else:
        print(f"File not found at: {output_file}")