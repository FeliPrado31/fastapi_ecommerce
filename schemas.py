from typing import List
from pydantic import BaseModel

class ProductoDetalle(BaseModel):
    nombre: str
    precio_unitario: float
    cantidad: int
    total_producto: float

class PedidoResponse(BaseModel):
    id_pedido: int
    fecha_creacion: str
    estado: str
    productos: List[ProductoDetalle]
    total_pedido: float