frappe.ui.form.on('Fornecedor', {
    refresh: function(frm) {
        // Bloqueia o NIF apenas em registros existentes
        if (!frm.is_new()) {
            frm.set_df_property('nif', 'read_only', 1);
        }
    },
    after_save: function(frm) {
        // Mensagem de sucesso
        frappe.msgprint(__('Fornecedor atualizado com sucesso!'));
    }
});

// Configuração da List View
frappe.listview_settings['Fornecedor'] = {
    add_fields: ["nif", "nome", "estado", "telefone"],

    get_indicator: function(doc) {
        if (doc.estado === "Ativo") {
            return [__("Ativo"), "green", "estado,=,Ativo"];
        } else if (doc.estado === "Inativo") {
            return [__("Inativo"), "red", "estado,=,Inativo"];
        } else {
            return [__("Desconhecido"), "gray", "estado,=, "];
        }
    }
};