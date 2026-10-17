import os
from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer


def student_details():
    return {
        "name": os.getenv("STUDENT_NAME", "Сүлеймен"),
        "surname": os.getenv("STUDENT_SURNAME", "Елдосұлы"),
        "group": os.getenv("STUDENT_GROUP", "IT2-2310"),
        "id": os.getenv("STUDENT_ID", "38320"),
    }


def student_page(student):
    lines = [
        ("Name", student["name"]),
        ("Surname", student["surname"]),
        ("Group", student["group"]),
        ("Student ID", student["id"]),
    ]
    details = "\n".join(
        f"<p><strong>{label}:</strong> {escape(value)}</p>"
        for label, value in lines
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>DevOps Student Application</title>
  <style>
    body {{ font-family: Arial, sans-serif; max-width: 600px; margin: 60px auto;
           padding: 0 20px; line-height: 1.5; color: #222; }}
    h1 {{ margin-bottom: 24px; }}
  </style>
</head>
<body>
  <h1>DevOps Student Application</h1>
  {details}
  <p>Application is running successfully!</p>
</body>
</html>"""


class StudentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b"OK\n"
            content_type = "text/plain; charset=utf-8"
        elif self.path == "/":
            body = student_page(student_details()).encode("utf-8")
            content_type = "text/html; charset=utf-8"
        else:
            self.send_error(404, "Not found")
            return

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    student = student_details()
    port = int(os.getenv("APP_PORT", "8000"))
    print("===============================", flush=True)
    print("DevOps Student Application", flush=True)
    print("===============================", flush=True)
    print(f"Student: {student['name']} {student['surname']}", flush=True)
    print(f"Group: {student['group']}", flush=True)
    print(f"Student ID: {student['id']}", flush=True)
    print(f"Application is running on port {port}", flush=True)
    HTTPServer(("0.0.0.0", port), StudentHandler).serve_forever()
