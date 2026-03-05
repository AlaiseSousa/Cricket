// Copyright (c) 2026, . and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Alimentos", {
// 	refresh(frm) {

// 	},
// });
frappe.listview_settings['Alimentos'] = {
    add_fields: ["nome", "unidade_de_medida", "tipo_materia_prima", "ativo"],
    get_indicator: function(doc) {
        if(doc.ativo) {
            return [__("Ativo"), "green", "ativo,=,1"];
        } else {
            return [__("Inativo"), "red", "ativo,=,0"];
        }
    },
    filters: [["ativo", "=", 1]] // mostra apenas ativos por padrão
};


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
    }
});