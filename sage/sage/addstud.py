import frappe

@frappe.whitelist()
def create_student(firstname,lastname,gender,profile_img):
    print(firstname,lastname,gender,profile_img)
    doc = frappe.get_doc({
    'doctype': 'Student',
    'first_name': firstname,
    'last_name' : lastname,
    'gender' : gender,
    'profile_img' : profile_img
    })
    doc.insert()
    return "Student Successfully added"