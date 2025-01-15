EXPLAIN ANALYZE
WITH fecha_incio_ajustada AS (
    SELECT fecha_incio - INTERVAL '1 day' AS fecha_ajustada
    FROM cld_bi_operacion_eng.fecha_incio_2_prueba
),
filtrado_microservicios AS (
    SELECT
        mv.terminal,
        mv.codigo_unico,
        mv.version_contenedor,
        mv.date_monitoring
    FROM cld_bi_operacion_eng.microservicios_versiones_t mv
    CROSS JOIN fecha_incio_ajustada fi
    WHERE mv.date_monitoring = fi.fecha_ajustada
),
BaseCTE AS (
    SELECT
        terminal,
        codigo_unico,
        version_contenedor,
        date_monitoring,
        ROW_NUMBER() OVER (
            PARTITION BY terminal, codigo_unico
            ORDER BY date_monitoring DESC
        ) AS rn
    FROM filtrado_microservicios
)
SELECT
    terminal,
    codigo_unico,
    version_contenedor,
    date_monitoring,
    '' AS serie
INTO cld_bi_operacion_eng.microservicios_gestor_de_terminales
FROM BaseCTE
WHERE rn = 1;
