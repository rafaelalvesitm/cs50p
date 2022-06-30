def main():
    # Ask for the user to input a file name
    input_string = input("File name: ").lower().strip()
    # Print the fila MIME type to the screen
    print(mime_type(input_string))

def mime_type(string):
    if string.endswith(".gif"):
        return "image/gif"
    elif string.endswith(".jpg") or string.endswith(".jpeg"):
        return "image/jpeg"
    elif string.endswith(".png"):
        return "image/png"
    elif string.endswith(".pdf"):
        return "application/pdf"
    elif string.endswith(".txt"):
        return "text/plain"
    elif string.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


# Use this function ONLY if python is in version 3.10
def mime_type_with_match(string):
    # get the file extension
    extension = string.split(".")[-1]
    # get the MIME type for the file extension
    match extension:
        case "gif":
            return "image/gif"
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _ :
            return "application/octet-stream"

if __name__ == "__main__":
    main()