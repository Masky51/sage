import frappe

@frappe.whitelist()
def create_student(firstname,lastname,gender,profile_img):
    doc = frappe.get_doc({
    'doctype': 'Student',
    'first_name': firstname,
    'last_name' : lastname,
    'gender' : gender,
    'profile_img' : profile_img
    })
    doc.insert()
    return "Student Successfully added"

@frappe.whitelist()
def get_student(stud_id):
    student = frappe.db.get_value("Student", filters={"name": stud_id}, fieldname=["first_name", "last_name", "gender", "profile_img"])

    if student:
        return {
            "firstname": student[0],
            "lastname": student[1],
            "gender": student[2],
            "profile_img": student[3]
        }
    else:
        return None
    
@frappe.whitelist()
def update_student(student_id,firstname,lastname,gender,profile_img):
    
    doc = frappe.get_doc("Student", student_id)
    doc.first_name = firstname
    doc.last_name = lastname
    doc.gender = gender
    doc.profile_img = profile_img
    doc.save()
    return "Successfully updated student"