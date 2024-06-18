class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')
        if not carro:
            carro = self.session['carro'] = {}
        self.carro = carro

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carro.keys():
            self.carro[id] = {
                'producto_id': producto.id,
                'nombre': producto.nombre,
                'cantidad': 1,
                'precio': str(producto.precio),
                'imagen': str(producto.imagen.url)
            }
        else:
            self.carro[id]['cantidad'] += 1
        self.guardar_carro()

    def guardar_carro(self):
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carro:
            del self.carro[id]
            self.guardar_carro()

    def restar_compra(self, producto):
        id = str(producto.id)
        if id in self.carro:
            if self.carro[id]['cantidad'] > 1:
                self.carro[id]['cantidad'] -= 1
            else:
                self.eliminar(producto)
            self.guardar_carro()

    def limpiar_carro(self):
        self.session['carro'] = {}
        self.guardar_carro()

    def cantidad_total(self):
        return sum(item['cantidad'] for item in self.carro.values())
