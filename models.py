from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    pedidos = relationship('Pedido', backref='cliente', lazy=True)

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)

class Pedido(Base):
    __tablename__ = "pedido"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey('cliente.id'), nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.now())
    estado = Column(String(20), default='pendiente')
    detalles = relationship('Detalle', backref='pedido', lazy=True)

class Detalle(Base):
    __tablename__ = "detalle"
    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey('pedido.id'), nullable=False)
    producto_id = Column(Integer, ForeignKey('producto.id'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    producto = relationship('Producto', backref='detalles', lazy=True)