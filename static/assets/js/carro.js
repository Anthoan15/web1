$(document).ready(function() {
    function actualizarCarro(url, productoId, isAdd) {
        $.ajax({
            url: url,
            method: 'POST',
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response) {
                if (response.status === 'ok') {
                    console.log('Producto actualizado correctamente');
                    if (isAdd === undefined) {
                        $('#cantidad-' + productoId).text(response.carro[productoId].cantidad);
                        
                        // Asegurarse de que el precio sea un número antes de usar toFixed
                        var precio = parseFloat(response.carro[productoId].precio);
                        if (!isNaN(precio)) {
                            $('#precio-' + productoId).text(precio.toFixed(2));
                        } else {
                            console.log('Error: el precio no es un número');
                        }
                    }
                    $('#importe-total').text(response.importe_total_carro + ' $');
                    $('#carro-container').html(response.widget);
                } else {
                    console.log('Error al actualizar el producto');
                }
            },
            error: function(response) {
                console.log('Error en la solicitud AJAX');
            }
        });
    }

    $(document).on('click', '.agregar-producto', function(e) {
        e.preventDefault();
        var productoId = $(this).data('producto-id');
        var url = $(this).data('url');
        actualizarCarro(url, productoId, true);
    });

    $(document).on('click', '.sumar-producto', function(e) {
        e.preventDefault();
        var productoId = $(this).data('producto-id');
        var url = $(this).data('url');
        actualizarCarro(url, productoId);
    });

    $(document).on('click', '.restar-producto', function(e) {
        e.preventDefault();
        var productoId = $(this).data('producto-id');
        var url = $(this).data('url');
        actualizarCarro(url, productoId);
    });
});
