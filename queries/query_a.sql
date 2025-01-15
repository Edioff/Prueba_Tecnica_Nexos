SELECT Almacen.sucursal, SUM(Venta.valorUnitario*Venta.Cantidad) AS VentasTotales 
FROM Venta 
JOIN Almacen ON venta.idAlmacen = Almacen.idAlmacen
GROUP BY Almacen.sucursal