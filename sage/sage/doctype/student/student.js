// Copyright (c) 2024, mohammed shariq and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student', {
	refresh: function(frm) {
		frm.add_custom_button('Calculate', () => Calculatesum(frm))
	}
});

function Calculatesum(frm)
{
	console.log("method triggered")
	frappe.call({
        method: 'sage.sage.student_hooks.CalculateADD',
        args: {
            a:frm.doc.a,
            b:frm.doc.b,
			stdId:frm.doc.name
        },
        callback: function(response) {
        if (response.message) {
          alert("success")

        } else {
          
        }
      }
    });
}