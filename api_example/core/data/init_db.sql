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
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    language INTEGER,
    currency TEXT,
    UNIQUE(name),
    FOREIGN KEY(language) REFERENCES language(id)
);

CREATE TABLE area (
    id INTEGER PRIMARY KEY,
    provider INTEGER,
    name TEXT,
    price REAL,
    FOREIGN KEY(provider) REFERENCES provider(id)
);
SELECT load_extension("mod_spatialite.so");
SELECT InitSpatialMetaData(1);
SELECT AddGeometryColumn("area", "geom", 4326, "POLYGON", 2);
