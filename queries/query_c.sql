SELECT Cliente.nombreCliente, SUM(Venta.Cantidad*valorUnitario) AS FacturacionTotal
FROM Venta
JOIN Cliente ON Venta.idCliente = Cliente.idCliente
GROUP BY Cliente.nombreCliente
ORDER BY FacturacionTotal DESC LIMIT 1