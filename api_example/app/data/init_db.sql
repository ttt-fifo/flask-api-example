CREATE TABLE language (
    id INTEGER PRIMARY KEY,
    name TEXT,
    alpha_2 TEXT,
    alpha_3 TEXT,
    scope TEXT,
    langtype TEXT
);

CREATE TABLE provider (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phonenumber TEXT,
    language TEXT,
    currency TEXT
);

CREATE TABLE area (
id INTEGER PRIMARY KEY,
name TEXT,
price REAL
);
SELECT load_extension("mod_spatialite.so");
SELECT InitSpatialMetaData(1);
SELECT AddGeometryColumn("area", "geom", 4326, "POLYGON", 2);

C
