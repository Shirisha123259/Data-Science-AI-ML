contacts = {
    "Rahul": "9876543210",
    "Anita": "9123456789",
    "Suresh": "9988776655"
}
contacts["Priya"] = "9012345678"
contacts["Rahul"] = "9999999999"
existing_contact = contacts.get("Anita", "Contact not found")
missing_contact = contacts.get("Kiran", "Contact not found")
print("Safe Lookup Results:")
print("Anita:", existing_contact)
print("Kiran:", missing_contact)
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")
