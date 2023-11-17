// Creditos al profesor Jose Urzua https://codepen.io/jourzua/pen/NWeNYow?externo=1 por la asociacion entre Regiónes y comunas
// Creditos a @juanbrujo por los arrays de strings con las comunas https://gist.github.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd 

function cargarComuna(){
    let select = document.getElementById("region");
    let region = select.value;
    
    let selectTipos = document.getElementById("comuna");
    selectTipos.innerHTML = "";
    
    if (region == "Región Arica y Parinacota") {
        (["Arica", "Camarones", "Putre", "Gral. Lagos"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Tarapacá") {
        (["Iquique", "Alto Hospicio", "Pozo Almonte", "Camiña", "Colchane", "Huara", "Pica"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Antofagasta") {
        (["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollague", "San Pedro de Atacama", "Tocopilla", "Maria Elena"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Atacama") {
        (["Copiapo", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Coquimbo") {
        (["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbala", "Monte Patria", "Punitaqui", "Rio Hurtado"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Valparaíso") {
        (["Valparaiso", "Casablanca", "Concon", "Juan Fernandez", "Puchuncavi", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa Maria", "Quilpue", "Limache", "Olmue", "Villa Alemana"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región Metropolitana de Santiago") {
        (["Cerrillos", "Cerro Navia", "Conchali", "El Bosque", "Estacion Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipu", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolen", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "Santiago", "San Joaquin", "San Miguel", "San Ramon", "Vitacura", "Puente Alto", "Pirque", "San Jose de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhue", "Curacavi", "Maria Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option); 
            });
    } else if (region == "Región del Libertador Bernardo Ohiggins") {
        (["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machali", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requinoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chepica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región del Maule") {
        (["Talca", "Constitucion", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Rio Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curico", "Hualañe", "Licanten", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquen", "Linares", "Colbun", "Longavi", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región del Ñuble") {
        (["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ranquil", "Treguaco", "Bulnes", "Chillan Viejo", "Chillan", "El Carmen", "Pemuco", "Pinto", "Quillon", "San Ignacio", "Yungay", "Coihueco", "Ñiquen", "San Carlos", "San Fabian", "San Nicolas"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región del Biobío") {
        (["Concepcion", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tome", "Hualpen", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los alamos", "Tirua", "Los angeles", "Antuco", "Cabrero", "Laja", "Mulchen", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Barbara", "Tucapel", "Yumbel", "Alto Biobio"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de La Araucanía") {
        (["Temuco", "Carahue", "Capitan Pastene","Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquen", "Pucon", "Saavedra", "Teodoro Schmidt", "Tolten", "Vilcun", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautin", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Puren", "Renaico", "Traiguen", "Victoria"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Los Ríos") {
        (["Valdivia", "Corral", "Lanco", "Los Lagos", "Mafil", "Mariquina", "Paillaco", "Panguipulli", "La Union", "Futrono", "Lago Ranco", "Rio Bueno"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Los Lagos") {
        (["Puerto Montt", "Calbuco", "Cochamo", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullin", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Velez", "Dalcahue", "Puqueldon", "Queilen", "Quellon", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Rio Negro", "San Juan de la Costa", "San Pablo", "Chaiten", "Futaleufu", "Hualaihue", "Palena"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región Aisén del General Carlos Ibáñez del Campo") {
        (["Coyhaique", "Lago Verde", "Aisen", "Cisnes", "Guaitecas", "Cochrane", "O'Higgins", "Tortel", "Chile Chico", "Rio Ibañez"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Magallanes y la Antártica Chilena") {
        (["Punta Arenas", "Laguna Blanca", "Rio Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "Antartica", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    }

}