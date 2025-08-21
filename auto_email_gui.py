import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox

# Email পাঠানোর ফাংশন
def send_email():
    sender_email = sender_entry.get()
    sender_password = password_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END)

    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.set_content(body)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email:\n{e}")

# GUI সেটআপ
root = tk.Tk()
root.title("Auto Email Sender")
root.geometry("500x550")

# Labels and Entries
tk.Label(root, text="Your Email:").pack(pady=5)
sender_entry = tk.Entry(root, width=50)
sender_entry.pack()

tk.Label(root, text="App Password:").pack(pady=5)
password_entry = tk.Entry(root, width=50, show="*")
password_entry.pack()

tk.Label(root, text="Receiver Email:").pack(pady=5)
receiver_entry = tk.Entry(root, width=50)
receiver_entry.pack()

tk.Label(root, text="Subject:").pack(pady=5)
subject_entry = tk.Entry(root, width=50)
subject_entry.pack()

tk.Label(root, text="Body:").pack(pady=5)
body_text = tk.Text(root, width=60, height=15)
body_text.pack(pady=5)

# Send Button
tk.Button(root, text="Send Email", command=send_email, bg="blue", fg="white", padx=10, pady=5).pack(pady=10)

root.mainloop()
