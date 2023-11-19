document.addEventListener("DOMContentLoaded", function() {
  // Obtener los datos de las estadísticas
  fetch("/get-stats-data")
    .then(response => response.json())
    .then(data => {
      // Generar el gráfico de frecuencias de deportes
      Highcharts.chart('chart-deportes', {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Frecuencias de Deportes'
        },
        xAxis: {
          categories: data.nombres_deportes
        },
        yAxis: {
          title: {
            text: 'Frecuencia'
          }
        },
        series: [{
          name: 'Frecuencia',
          data: data.frecuencias_deportes
        }]
      });

      // Generar el gráfico de frecuencias de tipos de artesanía
      Highcharts.chart('chart-artesania', {
        chart: {
          type: 'column'
        },
        title: {
          text: 'Frecuencias de Tipos de Artesanía'
        },
        xAxis: {
          categories: data.nombres_tipos_artesania
        },
        yAxis: {
          title: {
            text: 'Frecuencia'
          }
        },
        series: [{
          name: 'Frecuencia',
          data: data.frecuencias_tipos_artesania
        }]
      });
    })
    .catch(error => {
      console.log("Error al obtener los datos de las estadísticas");
      console.log(error);
    });
});