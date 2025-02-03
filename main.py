from fastapi import FastAPI, Query
from database import SessionLocal
from models import Pedido, Detalle, Producto
from schemas import PedidoResponse
from datetime import datetime

app = FastAPI()

@app.get("/pedidos/", response_model=list[PedidoResponse])
async def obtener_pedidos(
    fecha_inicial: str = Query(..., description="Fecha inicial (YYYY-MM-DD)"),
    fecha_final: str = Query(..., description="Fecha final (YYYY-MM-DD)")
):
    """
    Endpoint para obtener pedidos dentro de un rango de fechas,
    incluyendo el total del pedido y el total por cada producto.
    """
    fecha_inicial_dt = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final_dt = datetime.strptime(fecha_final, "%Y-%m-%d")

    db = SessionLocal()
    pedidos = (
        db.query(Pedido)
        .filter(Pedido.fecha_creacion.between(fecha_inicial_dt, fecha_final_dt))
        .all()
    )

    resultados = []
    for pedido in pedidos:
        detalles = pedido.detalles
        productos = []
        total_pedido = 0

        for detalle in detalles:
            producto = detalle.producto
            total_producto = producto.precio * detalle.cantidad
            total_pedido += total_producto
            productos.append({
                "nombre": producto.nombre,
                "precio_unitario": producto.precio,
                "cantidad": detalle.cantidad,
                "total_producto": total_producto
            })

        resultados.append({
            "id_pedido": pedido.id,
            "fecha_creacion": pedido.fecha_creacion,
            "estado": pedido.estado,
            "productos": productos,
            "total_pedido": total_pedido
        })

    return resultados