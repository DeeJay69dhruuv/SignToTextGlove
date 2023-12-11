import serial

# Define the serial port parameters
port = 'COM5'  # Replace with the correct serial port for your system
baudrate = 9600  # Set the baud rate to match the ESP32's serial configuration
# Open the serial port
with serial.Serial(port, baudrate, timeout=1) as ser:
    try:
        while True:
            # Read a line from the serial port
            data = ser.readline().decode('utf-8').strip().split()
            if data:
                # Write data to a file
                with open('data_file.txt', 'w') as file:
                    file.write(' '.join(data))

    except KeyboardInterrupt:
        print("Serial reading terminated.")