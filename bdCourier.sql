/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     15/1/2024 22:14:02                           */
/*==============================================================*/


drop index CLIENTE_PK;

drop table CLIENTE;

drop index DESTINATARIO_PK;

drop table DESTINATARIO;

drop index ESTA_FK;

drop index ENCOMIENDA_PK;

drop table ENCOMIENDA;

drop index RECORRE_FK;

drop index REALIZA_FK;

drop index RECIBE_FK;

drop index REGISTRA_FK;

drop index PERTENECE_FK;

drop index ENVIAR_FK;

drop index ENVIO_PK;

drop table ENVIO;

drop index ESTADOENCOMIENDA_PK;

drop table ESTADOENCOMIENDA;

drop index REPARTIDOR_PK;

drop table REPARTIDOR;

drop index RUTA_PK;

drop table RUTA;

drop index TICKET_PK;

drop table TICKET;

drop index TIPOENVIO_PK;

drop table TIPOENVIO;

/*==============================================================*/
/* Table: CLIENTE                                               */
/*==============================================================*/
create table CLIENTE (
   IDCLIENTE            SERIAL not null,
   CICLIENTE            VARCHAR(200)         null,
   NOMBRECLIENTE        VARCHAR(200)         null,
   APELLIDOCLIENTE      VARCHAR(200)         null,
   DIRECCIONCLIENTE     VARCHAR(200)         null,
   TELEFONOCLIENTE      VARCHAR(10)          null,
   constraint PK_CLIENTE primary key (IDCLIENTE)
);

/*==============================================================*/
/* Index: CLIENTE_PK                                            */
/*==============================================================*/
create unique index CLIENTE_PK on CLIENTE (
IDCLIENTE
);

/*==============================================================*/
/* Table: DESTINATARIO                                          */
/*==============================================================*/
create table DESTINATARIO (
   IDDESTINATARIO       SERIAL not null,
   CIDESTINATARIO       VARCHAR(200)         null,
   NOMBREDESTINATARIO   VARCHAR(200)         null,
   APELLIDODESTINATARIO VARCHAR(200)         null,
   DIRECCIONDESTINATARIO VARCHAR(200)         null,
   TELEFONODESTINATARIO VARCHAR(10)          null,
   constraint PK_DESTINATARIO primary key (IDDESTINATARIO)
);

/*==============================================================*/
/* Index: DESTINATARIO_PK                                       */
/*==============================================================*/
create unique index DESTINATARIO_PK on DESTINATARIO (
IDDESTINATARIO
);

/*==============================================================*/
/* Table: ENCOMIENDA                                            */
/*==============================================================*/
create table ENCOMIENDA (
   IDENCOMIENDA         SERIAL not null,
   IDESTADO             INT4                 null,
   TIPOENCOMIENDA       VARCHAR(200)         null,
   ALTURA               FLOAT8               null,
   PESO                 FLOAT8               null,
   DESCRIPCIONENCOMIENDA VARCHAR(200)         null,
   CATEGORIA            VARCHAR(200)         null,
   constraint PK_ENCOMIENDA primary key (IDENCOMIENDA)
);

/*==============================================================*/
/* Index: ENCOMIENDA_PK                                         */
/*==============================================================*/
create unique index ENCOMIENDA_PK on ENCOMIENDA (
IDENCOMIENDA
);

/*==============================================================*/
/* Index: ESTA_FK                                               */
/*==============================================================*/
create  index ESTA_FK on ENCOMIENDA (
IDESTADO
);

/*==============================================================*/
/* Table: ENVIO                                                 */
/*==============================================================*/
create table ENVIO (
   IDENVIO              SERIAL not null,
   IDTICKET             INT4                 not null,
   IDDESTINATARIO       INT4                 not null,
   IDRUTA               INT4                 null,
   IDCLIENTE            INT4                 not null,
   IDTIPOENVIO          INT4                 not null,
   IDENCOMIENDA         INT4                 not null,
   IDREPARTIDOR         INT4                 not null,
   DURACIONENVIO        TIME                 null,
   constraint PK_ENVIO primary key (IDENVIO)
);

/*==============================================================*/
/* Index: ENVIO_PK                                              */
/*==============================================================*/
create unique index ENVIO_PK on ENVIO (
IDENVIO
);

/*==============================================================*/
/* Index: ENVIAR_FK                                             */
/*==============================================================*/
create  index ENVIAR_FK on ENVIO (
IDCLIENTE
);

/*==============================================================*/
/* Index: PERTENECE_FK                                          */
/*==============================================================*/
create  index PERTENECE_FK on ENVIO (
IDTIPOENVIO
);

/*==============================================================*/
/* Index: REGISTRA_FK                                           */
/*==============================================================*/
create  index REGISTRA_FK on ENVIO (
IDTICKET
);

/*==============================================================*/
/* Index: RECIBE_FK                                             */
/*==============================================================*/
create  index RECIBE_FK on ENVIO (
IDDESTINATARIO
);

/*==============================================================*/
/* Index: REALIZA_FK                                            */
/*==============================================================*/
create  index REALIZA_FK on ENVIO (
IDREPARTIDOR
);

/*==============================================================*/
/* Index: RECORRE_FK                                            */
/*==============================================================*/
create  index RECORRE_FK on ENVIO (
IDRUTA
);

/*==============================================================*/
/* Table: ESTADOENCOMIENDA                                      */
/*==============================================================*/
create table ESTADOENCOMIENDA (
   IDESTADO             SERIAL not null,
   ACTIVOENCOMIENDA     VARCHAR(200)         null,
   FECHAESTADO          DATE                 null,
   constraint PK_ESTADOENCOMIENDA primary key (IDESTADO)
);

/*==============================================================*/
/* Index: ESTADOENCOMIENDA_PK                                   */
/*==============================================================*/
create unique index ESTADOENCOMIENDA_PK on ESTADOENCOMIENDA (
IDESTADO
);

/*==============================================================*/
/* Table: REPARTIDOR                                            */
/*==============================================================*/
create table REPARTIDOR (
   IDREPARTIDOR         SERIAL not null,
   NOMBREREPARTIDOR     VARCHAR(200)         null,
   APELLIDOREPARTIDOR   VARCHAR(200)         null,
   DIRECCIONREPARTIDOR  VARCHAR(200)         null,
   CARGOREPARTIDOR      VARCHAR(200)         null,
   constraint PK_REPARTIDOR primary key (IDREPARTIDOR)
);

/*==============================================================*/
/* Index: REPARTIDOR_PK                                         */
/*==============================================================*/
create unique index REPARTIDOR_PK on REPARTIDOR (
IDREPARTIDOR
);

/*==============================================================*/
/* Table: RUTA                                                  */
/*==============================================================*/
create table RUTA (
   IDRUTA               SERIAL not null,
   ORIGEN               VARCHAR(200)         null,
   DESTINO              VARCHAR(200)         null,
   constraint PK_RUTA primary key (IDRUTA)
);

/*==============================================================*/
/* Index: RUTA_PK                                               */
/*==============================================================*/
create unique index RUTA_PK on RUTA (
IDRUTA
);

/*==============================================================*/
/* Table: TICKET                                                */
/*==============================================================*/
create table TICKET (
   IDTICKET             SERIAL not null,
   DESCRIPCIONTICKET    VARCHAR(200)         null,
   FECHACREACION        DATE                 null,
   FECHAACTUALIZACION   DATE                 null,
   COSTOENCOMIENDA      FLOAT8               null,
   constraint PK_TICKET primary key (IDTICKET)
);

/*==============================================================*/
/* Index: TICKET_PK                                             */
/*==============================================================*/
create unique index TICKET_PK on TICKET (
IDTICKET
);

/*==============================================================*/
/* Table: TIPOENVIO                                             */
/*==============================================================*/
create table TIPOENVIO (
   IDTIPOENVIO          SERIAL not null,
   DESCRIPCIONTIPOENVIO VARCHAR(200)         null,
   FRAGILPESADO         BOOL                 null,
   constraint PK_TIPOENVIO primary key (IDTIPOENVIO)
);

/*==============================================================*/
/* Index: TIPOENVIO_PK                                          */
/*==============================================================*/
create unique index TIPOENVIO_PK on TIPOENVIO (
IDTIPOENVIO
);

alter table ENCOMIENDA
   add constraint FK_ENCOMIEN_ESTA_ESTADOEN foreign key (IDESTADO)
      references ESTADOENCOMIENDA (IDESTADO)
      on delete restrict on update restrict;

alter table ENVIO
   add constraint FK_ENVIO_ENVIAR_CLIENTE foreign key (IDCLIENTE)
      references CLIENTE (IDCLIENTE)
      on delete restrict on update restrict;

alter table ENVIO
   add constraint FK_ENVIO_PERTENECE_TIPOENVI foreign key (IDTIPOENVIO)
      references TIPOENVIO (IDTIPOENVIO)
      on delete restrict on update restrict;

alter table ENVIO
   add constraint FK_ENVIO_REALIZA_REPARTID foreign key (IDREPARTIDOR)
      references REPARTIDOR (IDREPARTIDOR)
      on delete restrict on update restrict;

alter table ENVIO
   add constraint FK_ENVIO_RECIBE_DESTINAT foreign key (IDDESTINATARIO)
      references DESTINATARIO (IDDESTINATARIO)
      on delete restrict on update restrict;

alter table ENVIO
   add constraint FK_ENVIO_RECORRE_RUTA foreign key (IDRUTA)
      references RUTA (IDRUTA)
      on delete restrict on update restrict;

alter table ENVIO
   add constraint FK_ENVIO_REGISTRA_TICKET foreign key (IDTICKET)
      references TICKET (IDTICKET)
      on delete restrict on update restrict;

alter table ENVIO
   add constraint FK_ENVIO_TIENE_ENCOMIEN foreign key (IDENCOMIENDA)
      references ENCOMIENDA (IDENCOMIENDA)
      on delete restrict on update restrict;

