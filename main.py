from fastapi import FastAPI, Query
from database import SessionLocal
from models import Pedido, Detalle, Producto
from schemas import PedidoResponse
from datetime import datetime
from sqlalchemy.orm import selectinload
from sqlalchemy import select

app = FastAPI()



@app.get("/pedidos/", response_model=list[PedidoResponse])
async def obtener_pedidos(
        fecha_inicial: str = Query(..., description="Fecha inicial (YYYY-MM-DD)"),
        fecha_final: str = Query(..., description="Fecha final (YYYY-MM-DD)")
):
    fecha_inicial_dt = datetime.strptime(fecha_inicial, "%Y-%m-%d")
    fecha_final_dt = datetime.strptime(fecha_final, "%Y-%m-%d")

    async with SessionLocal() as db:
        pedidos = (
            await db.execute(
                select(Pedido)
                .options(selectinload(Pedido.detalles).selectinload(
                    Detalle.producto))
                .filter(Pedido.fecha_creacion.between(fecha_inicial_dt, fecha_final_dt))
            )
        ).scalars().all()

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
                "fecha_creacion": pedido.fecha_creacion.strftime("%Y-%m-%d %H:%M:%S"),
                "estado": pedido.estado,
                "productos": productos,
                "total_pedido": total_pedido
            })
    return resultados