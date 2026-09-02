
patient_name = input("Enter Patient Name: ")

requested_departments = input(
    "Enter requested departments (comma separated): "
).split(",")

available_departments = input(
    "Enter available hospital departments (comma separated): "
).split(",")

previous_departments = input(
    "Enter previously visited departments (comma separated): "
).split(",")

preferred_doctors = input(
    "Enter preferred doctors (comma separated): "
).split(",")

available_doctors = input(
    "Enter available doctors (comma separated): "
).split(",")

emergency_departments = input(
    "Enter emergency departments (comma separated): "
).split(",")


requested_departments = [d.strip() for d in requested_departments]
available_departments = [d.strip() for d in available_departments]
previous_departments = [d.strip() for d in previous_departments]
preferred_doctors = [d.strip() for d in preferred_doctors]
available_doctors = [d.strip() for d in available_doctors]
emergency_departments = [d.strip() for d in emergency_departments]

if len(requested_departments) > 0:
    first_department = requested_departments[0]
else:
    first_department = "None"


department_slice = requested_departments[:2]


requested_departments.append("General Checkup")


if "General Checkup" in requested_departments:
    requested_departments.remove("General Checkup")


if "Cardiology" in requested_departments:
    cardiology_status = "Requested"
else:
    cardiology_status = "Not Requested"

requested_set = set(requested_departments)
available_set = set(available_departments)
previous_set = set(previous_departments)
emergency_set = set(emergency_departments)


available_requested = requested_set.intersection(available_set)


common_departments = requested_set.intersection(previous_set)


unavailable_departments = requested_set.difference(available_set)


all_departments = requested_set.union(available_set)


duplicates = set()
seen = set()

for dept in requested_departments:
    if dept in seen:
        duplicates.add(dept)
    else:
        seen.add(dept)


emergency_needed = requested_set.intersection(emergency_set)

available_preferred_doctors = list(
    set(preferred_doctors).intersection(set(available_doctors))
)


if len(available_requested) > 0:
    recommended_department = list(available_requested)[0]
else:
    recommended_department = "No Department Available"


if len(emergency_needed) > 0:
    appointment_status = "Emergency Appointment Approved Immediately"
elif len(available_requested) > 0:
    appointment_status = "Appointment Confirmed"
else:
    appointment_status = "Appointment Pending"

print("\n" + "=" * 50)
print("      HOSPITAL APPOINTMENT REPORT")
print("=" * 50)

print("Patient Name :", patient_name)

print("\nRequested Departments :", requested_departments)
print("Available Departments :", available_departments)

print("\nFirst Requested Department :", first_department)
print("First Two Requested Departments :", department_slice)

print("\nAvailable Requested Departments :", list(available_requested))
print("Unavailable Departments :", list(unavailable_departments))
print("Common (Previous + Requested) :", list(common_departments))
print("Previously Visited Departments :", previous_departments)
print("Emergency Departments :", emergency_departments)
print("Departments Requiring Immediate Attention :", list(emergency_needed))
print("Duplicate Requests :", list(duplicates))

print("\nPreferred Doctors :", preferred_doctors)
print("Available Doctors :", available_doctors)
print("Available Preferred Doctors :", available_preferred_doctors)

print("\nAll Hospital Departments :", list(all_departments))

print("\nCardiology Status :", cardiology_status)
print("Recommended Department :", recommended_department)
print("Final Appointment Status :", appointment_status)

print("=" * 50)