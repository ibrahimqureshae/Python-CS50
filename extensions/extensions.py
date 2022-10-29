# Take input
# Check the extension
name, delim, extension = input ("File Name: ").strip().lower().rpartition(".")



# Print the media type/MIME Type
match extension:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case other:
        print("application/octet-stream")