-- Crear tabla Almacen
CREATE TABLE Almacen (
  idAlmacen SERIAL PRIMARY KEY,       -- Clave primaria auto-incremental
  nombreAlmacen VARCHAR(100) UNIQUE, -- Garantiza que no haya almacenes con el mismo nombre
  sucursal VARCHAR(100),
  direccion VARCHAR(200)
);

-- Crear tabla Cliente
CREATE TABLE Cliente (
  idCliente SERIAL PRIMARY KEY,       -- Clave primaria auto-incremental
  nombreCliente VARCHAR(100) UNIQUE, -- Garantiza nombres únicos para clientes
  direccion VARCHAR(200),
  ciudad VARCHAR(100)
);

-- Crear tabla Venta
CREATE TABLE Venta (
  idFactura SERIAL PRIMARY KEY,       -- Clave primaria auto-incremental
  idAlmacen INT REFERENCES Almacen(idAlmacen), -- Llave foránea a Almacen
  fecha TIMESTAMP,
  idCliente INT REFERENCES Cliente(idCliente), -- Llave foránea a Cliente
  Cantidad INT CHECK (Cantidad > 0),           -- Validación: cantidad debe ser mayor a 0
  valorUnitario BIGINT CHECK (valorUnitario > 0) -- Validación: valor debe ser mayor a 0
);

-- Insertar datos en Almacen
INSERT INTO Almacen (nombreAlmacen, sucursal, direccion) VALUES
('Almacen Central', 'Centro', 'Av. Principal #123'),
('Almacen Norte', 'Norte', 'Calle Norte #45'),
('Almacen Sur', 'Sur', 'Avenida Sur #67'),
('Almacen Este', 'Este', 'Calle Oriente #89');

-- Insertar datos en Cliente
INSERT INTO Cliente (nombreCliente, direccion, ciudad) VALUES
('Juan Perez', 'Calle 10', 'Ciudad A'),
('Maria Lopez', 'Carrera 8', 'Ciudad B'),
('Carlos Ruiz', 'Avenida 15', 'Ciudad C'),
('Ana Torres', 'Calle 20', 'Ciudad D'),
('Luis Gomez', 'Carrera 5', 'Ciudad E');

-- Insertar datos en Venta
INSERT INTO Venta (idAlmacen, fecha, idCliente, Cantidad, valorUnitario) VALUES
(1, '2024-01-05 10:00:00', 1, 5, 100),
(1, '2024-01-15 11:00:00', 2, 3, 200),
(2, '2024-02-12 09:00:00', 1, 2, 500),
(3, '2024-02-25 14:30:00', 3, 7, 150),
(3, '2024-03-05 10:00:00', 4, 10, 120),
(4, '2024-03-15 16:45:00', 5, 4, 300),
(2, '2024-04-10 13:20:00', 3, 1, 400),
(4, '2024-05-08 18:00:00', 4, 6, 350),
(3, '2024-05-25 09:15:00', 5, 8, 90),
(1, '2024-06-15 11:00:00', 2, 15, 75),
(2, '2024-06-30 17:00:00', 1, 20, 250),
(4, '2024-07-05 12:00:00', 3, 10, 180),
(3, '2024-08-10 08:45:00', 4, 12, 130),
(1, '2024-09-15 14:30:00', 1, 25, 50),
(2, '2024-10-01 10:15:00', 5, 30, 60);