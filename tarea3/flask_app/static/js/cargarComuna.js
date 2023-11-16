// Créditos al profesor José Urzúa https://codepen.io/jourzua/pen/NWeNYow?externo=1 por la asociación entre regiones y comunas
// Créditos a @juanbrujo por los arrays de strings con las comunas https://gist.github.com/juanbrujo/0fd2f4d126b3ce5a95a7dd1f28b3d8dd 
function cargarComuna(){
    let select = document.getElementById("region");
    let region = select.value;
    
    let selectTipos = document.getElementById("comuna");
    selectTipos.innerHTML = "";
    
    if (region == "Región Arica y Parinacota") {
        (["Arica", "Camarones", "Putre", "General Lagos"]).forEach(
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
        (["Antofagasta", "Mejillones", "Sierra Gorda", "Taltal", "Calama", "Ollagüe", "San Pedro de Atacama", "Tocopilla", "María Elena"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Atacama") {
        (["Copiapó", "Caldera", "Tierra Amarilla", "Chañaral", "Diego de Almagro", "Vallenar", "Alto del Carmen", "Freirina", "Huasco"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
         });
    } else if (region == "Región de Coquimbo") {
        (["La Serena", "Coquimbo", "Andacollo", "La Higuera", "Paiguano", "Vicuña", "Illapel", "Canela", "Los Vilos", "Salamanca", "Ovalle", "Combarbalá", "Monte Patria", "Punitaqui", "Río Hurtado"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Valparaíso") {
        (["Valparaíso", "Casablanca", "Concón", "Juan Fernández", "Puchuncaví", "Quintero", "Viña del Mar", "Isla de Pascua", "Los Andes", "Calle Larga", "Rinconada", "San Esteban", "La Ligua", "Cabildo", "Papudo", "Petorca", "Zapallar", "Quillota", "Calera", "Hijuelas", "La Cruz", "Nogales", "San Antonio", "Algarrobo", "Cartagena", "El Quisco", "El Tabo", "Santo Domingo", "San Felipe", "Catemu", "Llaillay", "Panquehue", "Putaendo", "Santa María", "Quilpué", "Limache", "Olmué", "Villa Alemana"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región Metropolitana de Santiago") {
        (["Cerrillos", "Cerro Navia", "Conchalí", "El Bosque", "Estación Central", "Huechuraba", "Independencia", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "Ñuñoa", "Pedro Aguirre Cerda", "Peñalolén", "Providencia", "Pudahuel", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "Santiago", "San Joaquín", "San Miguel", "San Ramón", "Vitacura", "Puente Alto", "Pirque", "San José de Maipo", "Colina", "Lampa", "Tiltil", "San Bernardo", "Buin", "Calera de Tango", "Paine", "Melipilla", "Alhué", "Curacaví", "María Pinto", "San Pedro", "Talagante", "El Monte", "Isla de Maipo", "Padre Hurtado", "Peñaflor"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option); 
            });
    } else if (region == "Región del Libertador Bernardo Ohiggins") {
        (["Rancagua", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "Las Cabras", "Machalí", "Malloa", "Mostazal", "Olivar", "Peumo", "Pichidegua", "Quinta de Tilcoco", "Rengo", "Requínoa", "San Vicente", "Pichilemu", "La Estrella", "Litueche", "Marchihue", "Navidad", "Paredones", "San Fernando", "Chépica", "Chimbarongo", "Lolol", "Nancagua", "Palmilla", "Peralillo", "Placilla", "Pumanque", "Santa Cruz"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región del Maule") {
        (["Talca", "Constitución", "Curepto", "Empedrado", "Maule", "Pelarco", "Pencahue", "Río Claro", "San Clemente", "San Rafael", "Cauquenes", "Chanco", "Pelluhue", "Curicó", "Hualañé", "Licantén", "Molina", "Rauco", "Romeral", "Sagrada Familia", "Teno", "Vichuquén", "Linares", "Colbún", "Longaví", "Parral", "Retiro", "San Javier", "Villa Alegre", "Yerbas Buenas"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región del Ñuble") {
        (["Cobquecura", "Coelemu", "Ninhue", "Portezuelo", "Quirihue", "Ránquil", "Treguaco", "Bulnes", "Chillán Viejo", "Chillán", "El Carmen", "Pemuco", "Pinto", "Quillón", "San Ignacio", "Yungay", "Coihueco", "Ñiquén", "San Carlos", "San Fabián", "San Nicolás"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región del Biobío") {
        (["Concepción", "Coronel", "Chiguayante", "Florida", "Hualqui", "Lota", "Penco", "San Pedro de la Paz", "Santa Juana", "Talcahuano", "Tomé", "Hualpén", "Lebu", "Arauco", "Cañete", "Contulmo", "Curanilahue", "Los Álamos", "Tirúa", "Los Ángeles", "Antuco", "Cabrero", "Laja", "Mulchén", "Nacimiento", "Negrete", "Quilaco", "Quilleco", "San Rosendo", "Santa Bárbara", "Tucapel", "Yumbel", "Alto Biobío"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de La Araucanía") {
        (["Temuco", "Carahue", "Capitan Pastene","Cunco", "Curarrehue", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Melipeuco", "Nueva Imperial", "Padre las Casas", "Perquenco", "Pitrufquén", "Pucón", "Saavedra", "Teodoro Schmidt", "Toltén", "Vilcún", "Villarrica", "Cholchol", "Angol", "Collipulli", "Curacautín", "Ercilla", "Lonquimay", "Los Sauces", "Lumaco", "Purén", "Renaico", "Traiguén", "Victoria"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Los Ríos") {
        (["Valdivia", "Corral", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "La Unión", "Futrono", "Lago Ranco", "Río Bueno"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Los Lagos") {
        (["Puerto Montt", "Calbuco", "Cochamó", "Fresia", "Frutillar", "Los Muermos", "Llanquihue", "Maullín", "Puerto Varas", "Castro", "Ancud", "Chonchi", "Curaco de Vélez", "Dalcahue", "Puqueldón", "Queilén", "Quellón", "Quemchi", "Quinchao", "Osorno", "Puerto Octay", "Purranque", "Puyehue", "Río Negro", "San Juan de la Costa", "San Pablo", "Chaitén", "Futaleufú", "Hualaihué", "Palena"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región Aisén del General Carlos Ibáñez del Campo") {
        (["Coyhaique", "Lago Verde", "Aisén", "Cisnes", "Guaitecas", "Cochrane", "O'Higgins", "Tortel", "Chile Chico", "Río Ibáñez"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    } else if (region == "Región de Magallanes y la Antártica Chilena") {
        (["Punta Arenas", "Laguna Blanca", "Río Verde", "San Gregorio", "Cabo de Hornos (Ex Navarino)", "Antártica", "Porvenir", "Primavera", "Timaukel", "Natales", "Torres del Paine"]).forEach(
            (element) => {
                let option = document.createElement("option");
                option.text = element;
                option.value= element;
                selectTipos.add(option);
            });
    }
}