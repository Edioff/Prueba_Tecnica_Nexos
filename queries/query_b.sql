SELECT 
    EXTRACT(MONTH FROM fecha) AS mes,
    SUM(cantidad * valorunitario) AS total_ventas
FROM Venta
WHERE EXTRACT(YEAR FROM fecha) = EXTRACT(YEAR FROM CURRENT_DATE)
GROUP BY mes
ORDER BY mes;
