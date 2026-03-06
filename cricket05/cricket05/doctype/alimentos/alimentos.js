frappe.ui.form.on('Alimentos', {
    onload: function(frm) {
        // guarda unidade original
        frm.doc.__last_unit = frm.doc.unidade_de_medida;
    },
    before_save: function(frm) {
        if (frm.doc.unidade_de_medida !== frm.doc.__last_unit) {
            frappe.confirm(
                'Tem certeza que deseja alterar a unidade de medida?',
                function() {
                    // Usuário confirmou → salva normalmente
                    frm.doc.__last_unit = frm.doc.unidade_de_medida;
                },
                function() {
                    // Usuário cancelou → bloqueia o save
                    frappe.validated = false;
                }
            );
        }
    },
    before_delete: function(frm) {
        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Lote",
                filters: { alimento: frm.doc.name },
                limit_page_length: 1
            },
            callback: function(r) {
                if (r.message && r.message.length > 0) {
                    frappe.confirm(
                        `O alimento "${frm.doc.nome}" possui lotes associados. Deseja inativá-lo em vez de eliminar?`,
                        function() {
                            // Usuário confirmou → inativa
                            frappe.call({
                                method: "frappe.client.set_value",
                                args: {
                                    doctype: frm.doc.doctype,
                                    name: frm.doc.name,
                                    fieldname: "ativo",
                                    value: 0
                                },
                                callback: function() {
                                    frm.reload_doc();
                                    frappe.msgprint('Alimento inativado com sucesso.');
                                }
                            });
                        },
                        function() {
                            frappe.msgprint('Ação cancelada.');
                        }
                    );
                    frappe.validated = false; // cancela a exclusão
                }
            }
        });
    }
});