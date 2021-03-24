#!/bin/bash
echo "Initializing QProv DB..."

psql qprov < schema.sql

echo "Imported given schema into QProv DB"

psql qprov < data.sql

echo "Imported given data into QProv DB"