with open("server-log.txt", "r") as file:
    with open("errors-only.txt", "w") as output_file:
        counter = 0
        for line in file:
            data = line.strip()
            if "ERROR" in data:
                output_file.write(data + "\n")
                counter += 1


        print("The number of errors found in the logs are " + str(counter))


