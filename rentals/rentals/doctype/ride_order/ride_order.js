// Copyright (c) 2024, MN and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {

        if(frm.doc.status === "New"){

            frm.add_custom_button("Accept", ()=>{

                frm.set_value("status", "Accept");
                frm.save();
            }, "Actions")

            frm.add_custom_button("Reject", ()=>{

                frm.set_value("status", "Reject");
                frm.save();
            }, "Actions")
        }
        
	},
});
