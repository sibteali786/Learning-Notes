---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. For more info check in plugin settings under 'Saving'


# Excalidraw Data

## Text Elements
create table brand (
        brand_id INT not null,
        brand_name VARCHAR(100) not null,
        
        constraint pk_brand primary key (brand_id)        
)

create table model (
        model_number CHAR(4) not null,
        model_name VARCHAR(100) not null,
        constraint pk_model primary key (model_number)
)

create table spaceship (
        serial_number CHAR(17) not null,
        reccomended_price NUMERIC(8,2) not null,
        year_number smallint not null,
        
        constraint pk_spaceship primary key (serial_number)
)


CREATE TABLE address (
    address_id      INT             NOT NULL,
    street_address  VARCHAR(255)    NOT NULL,
    suburb          VARCHAR(100),
    city            VARCHAR(100)    NOT NULL,
    state_province  VARCHAR(100)    NOT NULL,
    postal_code     VARCHAR(20),
    country         CHAR(2)         NOT NULL,

    CONSTRAINT pk_address PRIMARY KEY (address_id)
);

create table dealer (
        dealer_id               INT             NOT NULL,
    dealer_name             VARCHAR(100)    NOT NULL,
    address_id              INT             NOT NULL,
    country_code            VARCHAR(5),
    dealer_phone_number     VARCHAR(15)     NOT NULL,
    email_address           VARCHAR(100)    NOT NULL,
    website_url             VARCHAR(255)    NOT null,
    
    constraint pk_dealer primary key (dealer_id),
    constraint fk_dealer_address foreign key (address_id) references address(address_id),
    constraint uq_dealer_email unique (email_address),
    constraint uq_dealer_phone unique (country_code, dealer_phone_number)
)

CREATE TABLE customer (
    customer_id             INT             NOT NULL,
    customer_name           VARCHAR(100)    NOT NULL,
    address_id              INT             NOT NULL,
    country_code            VARCHAR(5),
    customer_phone_number   VARCHAR(15)     NOT NULL,
    email_address           VARCHAR(100)    NOT NULL,

    CONSTRAINT pk_customer          PRIMARY KEY (customer_id),
    CONSTRAINT fk_customer_address  FOREIGN KEY (address_id) REFERENCES address(address_id),
    CONSTRAINT uq_customer_email    UNIQUE (email_address),
    CONSTRAINT uq_customer_phone    UNIQUE (country_code, customer_phone_number)
);





 ^mCc0twND

%%
## Drawing
```compressed-json
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
```
%%