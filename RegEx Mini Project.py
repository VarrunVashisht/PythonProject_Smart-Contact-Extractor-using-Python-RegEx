import re

text = """
Hello Team,

Please reach out to me at john.doe@example.com or jane_smith22@company.org.
For urgent issues, call me at 123-456-7890 or our office line at (555) 234-5678.
You can also contact support: help@business.co or visit www.business.co/support.

Thanks,
Varrun Vashisht
"""

# Pattern for emails
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Pattern for phone numbers (formats like 123-456-7890 or (555) 234-5678)
phone_pattern = r"(\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4})"

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print("📧 Email Addresses Found:")
for email in emails:
    print(" -", email)

print("\n📞 Phone Numbers Found:")
for phone in phones:
    print(" -", phone)