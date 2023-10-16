--
-- PostgreSQL database dump
--

-- Dumped from database version 12.5 (Debian 12.5-1.pgdg100+1)
-- Dumped by pg_dump version 13.2

-- Started on 2021-03-24 09:31:29

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 202 (class 1259 OID 16388)
-- Name: actedonbehalfof; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.actedonbehalfof (
    pk bigint NOT NULL,
    activity bigint,
    delegate bigint,
    id bigint,
    responsible bigint
);


ALTER TABLE public.actedonbehalfof OWNER TO qprov;

--
-- TOC entry 203 (class 1259 OID 16393)
-- Name: activity; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.activity (
    pk bigint NOT NULL,
    end_time timestamp without time zone,
    start_time timestamp without time zone,
    id bigint
);


ALTER TABLE public.activity OWNER TO qprov;

--
-- TOC entry 204 (class 1259 OID 16398)
-- Name: agent; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.agent (
    pk bigint NOT NULL,
    id bigint
);


ALTER TABLE public.agent OWNER TO qprov;

--
-- TOC entry 205 (class 1259 OID 16403)
-- Name: alternateof; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.alternateof (
    pk bigint NOT NULL,
    alternate1 bigint,
    alternate2 bigint
);


ALTER TABLE public.alternateof OWNER TO qprov;

--
-- TOC entry 206 (class 1259 OID 16408)
-- Name: bundle; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.bundle (
    pk bigint NOT NULL,
    id bigint,
    namespace bigint
);


ALTER TABLE public.bundle OWNER TO qprov;

--
-- TOC entry 207 (class 1259 OID 16413)
-- Name: bundle_statement_join; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.bundle_statement_join (
    bundle bigint NOT NULL,
    statement bigint NOT NULL
);


ALTER TABLE public.bundle_statement_join OWNER TO qprov;

--
-- TOC entry 208 (class 1259 OID 16416)
-- Name: calibration_matrix; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.calibration_matrix (
    database_id uuid NOT NULL,
    calibration_matrix oid,
    calibration_time timestamp without time zone,
    qpu_database_id uuid
);


ALTER TABLE public.calibration_matrix OWNER TO qprov;

--
-- TOC entry 209 (class 1259 OID 16421)
-- Name: classical_data; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.classical_data (
    database_id uuid NOT NULL,
    classical_data_value character varying(255)
);


ALTER TABLE public.classical_data OWNER TO qprov;

--
-- TOC entry 210 (class 1259 OID 16426)
-- Name: collection; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.collection (
    pk bigint NOT NULL,
    id bigint,
    value bigint
);


ALTER TABLE public.collection OWNER TO qprov;

--
-- TOC entry 211 (class 1259 OID 16431)
-- Name: compile_activity; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.compile_activity (
    database_id uuid NOT NULL,
    compilation_time numeric(19,2),
    optimization_goal character varying(255),
    random_seed character varying(255)
);


ALTER TABLE public.compile_activity OWNER TO qprov;

--
-- TOC entry 212 (class 1259 OID 16439)
-- Name: compiler; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.compiler (
    database_id uuid NOT NULL,
    name character varying(255),
    provider_name character varying(255),
    version character varying(255)
);


ALTER TABLE public.compiler OWNER TO qprov;

--
-- TOC entry 213 (class 1259 OID 16447)
-- Name: data_preparation_service; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.data_preparation_service (
    database_id uuid NOT NULL,
    name character varying(255),
    provider_name character varying(255),
    version character varying(255)
);


ALTER TABLE public.data_preparation_service OWNER TO qprov;

--
-- TOC entry 214 (class 1259 OID 16455)
-- Name: dictionary_; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.dictionary_ (
    pk bigint NOT NULL,
    id bigint,
    value bigint
);


ALTER TABLE public.dictionary_ OWNER TO qprov;

--
-- TOC entry 215 (class 1259 OID 16460)
-- Name: dictionarymembership; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.dictionarymembership (
    pk bigint NOT NULL,
    dictionary__dictionarymember_0 bigint
);


ALTER TABLE public.dictionarymembership OWNER TO qprov;

--
-- TOC entry 216 (class 1259 OID 16465)
-- Name: document; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.document (
    pk bigint NOT NULL,
    kind integer,
    ns bigint
);


ALTER TABLE public.document OWNER TO qprov;

--
-- TOC entry 217 (class 1259 OID 16470)
-- Name: document_statement_join; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.document_statement_join (
    document bigint NOT NULL,
    statement bigint NOT NULL
);


ALTER TABLE public.document_statement_join OWNER TO qprov;

--
-- TOC entry 218 (class 1259 OID 16473)
-- Name: emptycollection; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.emptycollection (
    pk bigint NOT NULL,
    id bigint,
    value bigint
);


ALTER TABLE public.emptycollection OWNER TO qprov;

--
-- TOC entry 219 (class 1259 OID 16478)
-- Name: emptydictionary; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.emptydictionary (
    pk bigint NOT NULL,
    id bigint,
    value bigint
);


ALTER TABLE public.emptydictionary OWNER TO qprov;

--
-- TOC entry 220 (class 1259 OID 16483)
-- Name: entity; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.entity (
    pk bigint NOT NULL,
    id bigint,
    value bigint
);


ALTER TABLE public.entity OWNER TO qprov;

--
-- TOC entry 221 (class 1259 OID 16488)
-- Name: execute_activity; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.execute_activity (
    database_id uuid NOT NULL,
    applied_error_mitigation character varying(255),
    execution_time numeric(19,2),
    number_of_shots integer NOT NULL
);


ALTER TABLE public.execute_activity OWNER TO qprov;

--
-- TOC entry 222 (class 1259 OID 16493)
-- Name: gate; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.gate (
    database_id uuid NOT NULL,
    name character varying(255),
    qpu_database_id uuid
);


ALTER TABLE public.gate OWNER TO qprov;

--
-- TOC entry 223 (class 1259 OID 16498)
-- Name: gate_characteristics; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.gate_characteristics (
    database_id uuid NOT NULL,
    calibration_time timestamp without time zone,
    gate_fidelity numeric(20,15),
    gate_time numeric(20,15),
    gate_database_id uuid
);


ALTER TABLE public.gate_characteristics OWNER TO qprov;

--
-- TOC entry 224 (class 1259 OID 16503)
-- Name: hadmember; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.hadmember (
    pk bigint NOT NULL,
    collection bigint
);


ALTER TABLE public.hadmember OWNER TO qprov;

--
-- TOC entry 225 (class 1259 OID 16508)
-- Name: hadmember_elements; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.hadmember_elements (
    collection bigint NOT NULL,
    entity bigint NOT NULL
);


ALTER TABLE public.hadmember_elements OWNER TO qprov;

--
-- TOC entry 271 (class 1259 OID 16785)
-- Name: hibernate_sequence; Type: SEQUENCE; Schema: public; Owner: qprov
--

CREATE SEQUENCE public.hibernate_sequence
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.hibernate_sequence OWNER TO qprov;

--
-- TOC entry 226 (class 1259 OID 16511)
-- Name: hibernate_sequences; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.hibernate_sequences (
    sequence_name character varying(255) NOT NULL,
    sequence_next_hi_value bigint
);


ALTER TABLE public.hibernate_sequences OWNER TO qprov;

--
-- TOC entry 227 (class 1259 OID 16516)
-- Name: idocument; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.idocument (
    pk bigint NOT NULL,
    datetimeitem timestamp without time zone,
    bindings bigint,
    latest bigint,
    previous bigint,
    provenance bigint,
    template bigint
);


ALTER TABLE public.idocument OWNER TO qprov;

--
-- TOC entry 228 (class 1259 OID 16521)
-- Name: internationalizedstring; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.internationalizedstring (
    pk bigint NOT NULL,
    lang character varying(255),
    value_ character varying(255),
    label_actedonbehalfof_pk bigint,
    label_activity_pk bigint,
    label_wasassociatedwith_pk bigint,
    label_used_pk bigint,
    label_wasgeneratedby_pk bigint,
    label_wasattributedto_pk bigint,
    label_wasinvalidatedby_pk bigint,
    label_wasendedby_pk bigint,
    label_wasstartedby_pk bigint,
    label_entity_pk bigint,
    label_wasinformedby_pk bigint,
    label_wasinfluencedby_oj bigint,
    label_agent_pk bigint,
    label_wasderivedfrom_pk bigint
);


ALTER TABLE public.internationalizedstring OWNER TO qprov;

--
-- TOC entry 229 (class 1259 OID 16529)
-- Name: key; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.key (
    pk bigint NOT NULL,
    gyearitem date,
    datetimeitem timestamp without time zone,
    double_ double precision,
    float_ real,
    long_ bigint,
    string text,
    type bigint,
    qn bigint
);


ALTER TABLE public.key OWNER TO qprov;

--
-- TOC entry 230 (class 1259 OID 16537)
-- Name: label; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.label (
    pk bigint NOT NULL,
    gyearitem date,
    datetimeitem timestamp without time zone,
    double_ double precision,
    float_ real,
    long_ bigint,
    string text,
    type bigint,
    qn bigint
);


ALTER TABLE public.label OWNER TO qprov;

--
-- TOC entry 231 (class 1259 OID 16545)
-- Name: location; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.location (
    pk bigint NOT NULL,
    gyearitem date,
    datetimeitem timestamp without time zone,
    double_ double precision,
    float_ real,
    long_ bigint,
    string text,
    type bigint,
    qn bigint,
    activity bigint,
    usage bigint,
    generation bigint,
    invalidation bigint,
    end_ bigint,
    start_ bigint,
    entity bigint,
    agent bigint
);


ALTER TABLE public.location OWNER TO qprov;

--
-- TOC entry 232 (class 1259 OID 16553)
-- Name: mentionof; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.mentionof (
    pk bigint NOT NULL,
    bundle bigint,
    generalentity_mentionof_pk bigint,
    specificentity_mentionof_pk bigint
);


ALTER TABLE public.mentionof OWNER TO qprov;

--
-- TOC entry 233 (class 1259 OID 16558)
-- Name: nameddocument; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.nameddocument (
    pk bigint NOT NULL,
    name character varying(255),
    value bigint
);


ALTER TABLE public.nameddocument OWNER TO qprov;

--
-- TOC entry 234 (class 1259 OID 16563)
-- Name: namespace; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.namespace (
    pk bigint NOT NULL,
    default_namespace character varying(255),
    parent bigint
);


ALTER TABLE public.namespace OWNER TO qprov;

--
-- TOC entry 235 (class 1259 OID 16568)
-- Name: namespace_map; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.namespace_map (
    pk bigint NOT NULL,
    namespace_value character varying(255),
    namespaces character varying(255) NOT NULL
);


ALTER TABLE public.namespace_map OWNER TO qprov;

--
-- TOC entry 236 (class 1259 OID 16576)
-- Name: organization; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.organization (
    pk bigint NOT NULL,
    id bigint
);


ALTER TABLE public.organization OWNER TO qprov;

--
-- TOC entry 237 (class 1259 OID 16581)
-- Name: other; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.other (
    pk bigint NOT NULL,
    gyearitem date,
    datetimeitem timestamp without time zone,
    double_ double precision,
    float_ real,
    long_ bigint,
    string text,
    type bigint,
    qn bigint,
    element bigint,
    others_actedonbehalfof_pk bigint,
    others_activity_pk bigint,
    others_wasassociatedwith_pk bigint,
    others_used_pk bigint,
    others_wasgeneratedby_pk bigint,
    others_wasattributedto_pk bigint,
    others_wasinvalidatedby_pk bigint,
    others_wasendedby_pk bigint,
    others_wasstartedby_pk bigint,
    others_entity_pk bigint,
    others_wasinformedby_pk bigint,
    others_wasinfluencedby_pk bigint,
    others_agent_pk bigint,
    others_wasderivedfrom_pk bigint
);


ALTER TABLE public.other OWNER TO qprov;

--
-- TOC entry 238 (class 1259 OID 16589)
-- Name: pdocument; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.pdocument (
    pk bigint NOT NULL,
    datetimeitem timestamp without time zone,
    document bigint,
    previous bigint,
    provenance bigint
);


ALTER TABLE public.pdocument OWNER TO qprov;

--
-- TOC entry 239 (class 1259 OID 16594)
-- Name: person; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.person (
    pk bigint NOT NULL,
    id bigint
);


ALTER TABLE public.person OWNER TO qprov;

--
-- TOC entry 240 (class 1259 OID 16599)
-- Name: plan; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.plan (
    pk bigint NOT NULL,
    id bigint,
    value bigint
);


ALTER TABLE public.plan OWNER TO qprov;

--
-- TOC entry 241 (class 1259 OID 16604)
-- Name: prefix_map; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.prefix_map (
    pk bigint NOT NULL,
    prefix_value character varying(255),
    prefix character varying(255) NOT NULL
);


ALTER TABLE public.prefix_map OWNER TO qprov;

--
-- TOC entry 242 (class 1259 OID 16612)
-- Name: prepare_data_activity; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.prepare_data_activity (
    database_id uuid NOT NULL,
    applied_encoding character varying(255)
);


ALTER TABLE public.prepare_data_activity OWNER TO qprov;

--
-- TOC entry 243 (class 1259 OID 16617)
-- Name: primarysource; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.primarysource (
    pk bigint NOT NULL,
    activity bigint,
    generated_entity bigint,
    generation bigint,
    id bigint,
    usage bigint,
    used_entity bigint
);


ALTER TABLE public.primarysource OWNER TO qprov;

--
-- TOC entry 245 (class 1259 OID 16630)
-- Name: prov_template; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.prov_template (
    pk bigint NOT NULL
);


ALTER TABLE public.prov_template OWNER TO qprov;

--
-- TOC entry 244 (class 1259 OID 16622)
-- Name: provider; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.provider (
    database_id uuid NOT NULL,
    name character varying(255),
    offeringurl character varying(255)
);


ALTER TABLE public.provider OWNER TO qprov;

--
-- TOC entry 246 (class 1259 OID 16635)
-- Name: qpu; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.qpu (
    database_id uuid NOT NULL,
    is_simulator boolean NOT NULL,
    last_calibrated timestamp without time zone,
    last_updated timestamp without time zone,
    max_shots integer NOT NULL,
    name character varying(255),
    queue_size integer NOT NULL,
    version character varying(255),
    provider_database_id uuid
);


ALTER TABLE public.qpu OWNER TO qprov;

--
-- TOC entry 247 (class 1259 OID 16643)
-- Name: qualifiedname; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.qualifiedname (
    pk bigint NOT NULL,
    refitem character varying(255),
    uri text
);


ALTER TABLE public.qualifiedname OWNER TO qprov;

--
-- TOC entry 248 (class 1259 OID 16651)
-- Name: quantum_circuit; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.quantum_circuit (
    database_id uuid NOT NULL,
    code_url character varying(255),
    depth integer NOT NULL,
    name character varying(255),
    size integer NOT NULL,
    width integer NOT NULL
);


ALTER TABLE public.quantum_circuit OWNER TO qprov;

--
-- TOC entry 249 (class 1259 OID 16659)
-- Name: qubit; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.qubit (
    database_id uuid NOT NULL,
    name character varying(255),
    qpu_database_id uuid
);


ALTER TABLE public.qubit OWNER TO qprov;

--
-- TOC entry 251 (class 1259 OID 16669)
-- Name: qubit_characteristics; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.qubit_characteristics (
    database_id uuid NOT NULL,
    calibration_time timestamp without time zone,
    readout_error numeric(20,15),
    t1time numeric(20,15),
    t2time numeric(20,15),
    qubit_database_id uuid
);


ALTER TABLE public.qubit_characteristics OWNER TO qprov;

--
-- TOC entry 250 (class 1259 OID 16664)
-- Name: qubit_connectivity; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.qubit_connectivity (
    qubit1 uuid NOT NULL,
    qubit2 uuid NOT NULL
);


ALTER TABLE public.qubit_connectivity OWNER TO qprov;

--
-- TOC entry 252 (class 1259 OID 16674)
-- Name: qubits_gates; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.qubits_gates (
    qubit_id uuid NOT NULL,
    gate_id uuid NOT NULL
);


ALTER TABLE public.qubits_gates OWNER TO qprov;

--
-- TOC entry 253 (class 1259 OID 16679)
-- Name: quotation; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.quotation (
    pk bigint NOT NULL,
    activity bigint,
    generated_entity bigint,
    generation bigint,
    id bigint,
    usage bigint,
    used_entity bigint
);


ALTER TABLE public.quotation OWNER TO qprov;

--
-- TOC entry 254 (class 1259 OID 16684)
-- Name: revision; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.revision (
    pk bigint NOT NULL,
    activity bigint,
    generated_entity bigint,
    generation bigint,
    id bigint,
    usage bigint,
    used_entity bigint
);


ALTER TABLE public.revision OWNER TO qprov;

--
-- TOC entry 255 (class 1259 OID 16689)
-- Name: role; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.role (
    pk bigint NOT NULL,
    gyearitem date,
    datetimeitem timestamp without time zone,
    double_ double precision,
    float_ real,
    long_ bigint,
    string text,
    type bigint,
    qn bigint,
    role__wasassociatedwith_pk bigint,
    role__used_pk bigint,
    role__wasgeneratedby_pk bigint,
    role__wasinvalidatedby_pk bigint,
    role__wasendedby_pk bigint,
    role__wasstartedby_pk bigint
);


ALTER TABLE public.role OWNER TO qprov;

--
-- TOC entry 256 (class 1259 OID 16697)
-- Name: softwareagent; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.softwareagent (
    pk bigint NOT NULL,
    id bigint
);


ALTER TABLE public.softwareagent OWNER TO qprov;

--
-- TOC entry 257 (class 1259 OID 16702)
-- Name: specializationof; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.specializationof (
    pk bigint NOT NULL,
    general bigint,
    specific bigint
);


ALTER TABLE public.specializationof OWNER TO qprov;

--
-- TOC entry 258 (class 1259 OID 16707)
-- Name: type; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.type (
    pk bigint NOT NULL,
    gyearitem date,
    datetimeitem timestamp without time zone,
    double_ double precision,
    float_ real,
    long_ bigint,
    string text,
    type bigint,
    qn bigint,
    type__actedonbehalfof_pk bigint,
    type__activity_pk bigint,
    type__wasassociatedwith_pk bigint,
    type__used_pk bigint,
    type__wasgeneratedby_pk bigint,
    type__wasattributedto_pk bigint,
    type__wasinvalidatedby_pk bigint,
    type__wasendedby_pk bigint,
    type__wasstartedby_pk bigint,
    type__entity_pk bigint,
    type__wasinformedby_pk bigint,
    type__wasinfluencedby_pk bigint,
    type__agent_pk bigint,
    type__wasderivedfrom_pk bigint
);


ALTER TABLE public.type OWNER TO qprov;

--
-- TOC entry 259 (class 1259 OID 16715)
-- Name: typedvalue; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.typedvalue (
    pk bigint NOT NULL,
    gyearitem date,
    datetimeitem timestamp without time zone,
    double_ double precision,
    float_ real,
    long_ bigint,
    string text,
    type bigint,
    qn bigint
);


ALTER TABLE public.typedvalue OWNER TO qprov;

--
-- TOC entry 260 (class 1259 OID 16723)
-- Name: used; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.used (
    pk bigint NOT NULL,
    timeitem timestamp without time zone,
    activity bigint,
    entity bigint,
    id bigint
);


ALTER TABLE public.used OWNER TO qprov;

--
-- TOC entry 261 (class 1259 OID 16728)
-- Name: value; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.value (
    pk bigint NOT NULL,
    gyearitem date,
    datetimeitem timestamp without time zone,
    double_ double precision,
    float_ real,
    long_ bigint,
    string text,
    type bigint,
    qn bigint
);


ALTER TABLE public.value OWNER TO qprov;

--
-- TOC entry 262 (class 1259 OID 16736)
-- Name: wasassociatedwith; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasassociatedwith (
    pk bigint NOT NULL,
    activity bigint,
    agent bigint,
    id bigint,
    plan bigint
);


ALTER TABLE public.wasassociatedwith OWNER TO qprov;

--
-- TOC entry 263 (class 1259 OID 16741)
-- Name: wasattributedto; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasattributedto (
    pk bigint NOT NULL,
    agent bigint,
    entity bigint,
    id bigint
);


ALTER TABLE public.wasattributedto OWNER TO qprov;

--
-- TOC entry 264 (class 1259 OID 16746)
-- Name: wasderivedfrom; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasderivedfrom (
    pk bigint NOT NULL,
    activity bigint,
    generated_entity bigint,
    generation bigint,
    id bigint,
    usage bigint,
    used_entity bigint
);


ALTER TABLE public.wasderivedfrom OWNER TO qprov;

--
-- TOC entry 265 (class 1259 OID 16751)
-- Name: wasendedby; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasendedby (
    pk bigint NOT NULL,
    timeitem timestamp without time zone,
    activity bigint,
    ender bigint,
    id bigint,
    trigger_ bigint
);


ALTER TABLE public.wasendedby OWNER TO qprov;

--
-- TOC entry 266 (class 1259 OID 16756)
-- Name: wasgeneratedby; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasgeneratedby (
    pk bigint NOT NULL,
    timeitem timestamp without time zone,
    activity bigint,
    entity bigint,
    id bigint
);


ALTER TABLE public.wasgeneratedby OWNER TO qprov;

--
-- TOC entry 267 (class 1259 OID 16761)
-- Name: wasinfluencedby; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasinfluencedby (
    pk bigint NOT NULL,
    id bigint,
    influencee bigint,
    influencer bigint
);


ALTER TABLE public.wasinfluencedby OWNER TO qprov;

--
-- TOC entry 268 (class 1259 OID 16766)
-- Name: wasinformedby; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasinformedby (
    pk bigint NOT NULL,
    id bigint,
    informant bigint,
    informed bigint
);


ALTER TABLE public.wasinformedby OWNER TO qprov;

--
-- TOC entry 269 (class 1259 OID 16771)
-- Name: wasinvalidatedby; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasinvalidatedby (
    pk bigint NOT NULL,
    timeitem timestamp without time zone,
    activity bigint,
    entity bigint,
    id bigint
);


ALTER TABLE public.wasinvalidatedby OWNER TO qprov;

--
-- TOC entry 270 (class 1259 OID 16776)
-- Name: wasstartedby; Type: TABLE; Schema: public; Owner: qprov
--

CREATE TABLE public.wasstartedby (
    pk bigint NOT NULL,
    timeitem timestamp without time zone,
    activity bigint,
    id bigint,
    starter bigint,
    trigger_ bigint
);


ALTER TABLE public.wasstartedby OWNER TO qprov;

--
-- TOC entry 3068 (class 2606 OID 16392)
-- Name: actedonbehalfof actedonbehalfof_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.actedonbehalfof
    ADD CONSTRAINT actedonbehalfof_pkey PRIMARY KEY (pk);


--
-- TOC entry 3070 (class 2606 OID 16397)
-- Name: activity activity_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.activity
    ADD CONSTRAINT activity_pkey PRIMARY KEY (pk);


--
-- TOC entry 3072 (class 2606 OID 16402)
-- Name: agent agent_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.agent
    ADD CONSTRAINT agent_pkey PRIMARY KEY (pk);


--
-- TOC entry 3074 (class 2606 OID 16407)
-- Name: alternateof alternateof_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.alternateof
    ADD CONSTRAINT alternateof_pkey PRIMARY KEY (pk);


--
-- TOC entry 3076 (class 2606 OID 16412)
-- Name: bundle bundle_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.bundle
    ADD CONSTRAINT bundle_pkey PRIMARY KEY (pk);


--
-- TOC entry 3078 (class 2606 OID 16420)
-- Name: calibration_matrix calibration_matrix_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.calibration_matrix
    ADD CONSTRAINT calibration_matrix_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3080 (class 2606 OID 16425)
-- Name: classical_data classical_data_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.classical_data
    ADD CONSTRAINT classical_data_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3082 (class 2606 OID 16430)
-- Name: collection collection_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.collection
    ADD CONSTRAINT collection_pkey PRIMARY KEY (pk);


--
-- TOC entry 3084 (class 2606 OID 16438)
-- Name: compile_activity compile_activity_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.compile_activity
    ADD CONSTRAINT compile_activity_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3086 (class 2606 OID 16446)
-- Name: compiler compiler_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.compiler
    ADD CONSTRAINT compiler_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3088 (class 2606 OID 16454)
-- Name: data_preparation_service data_preparation_service_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.data_preparation_service
    ADD CONSTRAINT data_preparation_service_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3090 (class 2606 OID 16459)
-- Name: dictionary_ dictionary__pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.dictionary_
    ADD CONSTRAINT dictionary__pkey PRIMARY KEY (pk);


--
-- TOC entry 3092 (class 2606 OID 16464)
-- Name: dictionarymembership dictionarymembership_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.dictionarymembership
    ADD CONSTRAINT dictionarymembership_pkey PRIMARY KEY (pk);


--
-- TOC entry 3094 (class 2606 OID 16469)
-- Name: document document_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.document
    ADD CONSTRAINT document_pkey PRIMARY KEY (pk);


--
-- TOC entry 3096 (class 2606 OID 16477)
-- Name: emptycollection emptycollection_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.emptycollection
    ADD CONSTRAINT emptycollection_pkey PRIMARY KEY (pk);


--
-- TOC entry 3098 (class 2606 OID 16482)
-- Name: emptydictionary emptydictionary_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.emptydictionary
    ADD CONSTRAINT emptydictionary_pkey PRIMARY KEY (pk);


--
-- TOC entry 3100 (class 2606 OID 16487)
-- Name: entity entity_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.entity
    ADD CONSTRAINT entity_pkey PRIMARY KEY (pk);


--
-- TOC entry 3102 (class 2606 OID 16492)
-- Name: execute_activity execute_activity_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.execute_activity
    ADD CONSTRAINT execute_activity_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3106 (class 2606 OID 16502)
-- Name: gate_characteristics gate_characteristics_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.gate_characteristics
    ADD CONSTRAINT gate_characteristics_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3104 (class 2606 OID 16497)
-- Name: gate gate_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.gate
    ADD CONSTRAINT gate_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3108 (class 2606 OID 16507)
-- Name: hadmember hadmember_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.hadmember
    ADD CONSTRAINT hadmember_pkey PRIMARY KEY (pk);


--
-- TOC entry 3110 (class 2606 OID 16515)
-- Name: hibernate_sequences hibernate_sequences_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.hibernate_sequences
    ADD CONSTRAINT hibernate_sequences_pkey PRIMARY KEY (sequence_name);


--
-- TOC entry 3112 (class 2606 OID 16520)
-- Name: idocument idocument_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.idocument
    ADD CONSTRAINT idocument_pkey PRIMARY KEY (pk);


--
-- TOC entry 3114 (class 2606 OID 16528)
-- Name: internationalizedstring internationalizedstring_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT internationalizedstring_pkey PRIMARY KEY (pk);


--
-- TOC entry 3116 (class 2606 OID 16536)
-- Name: key key_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.key
    ADD CONSTRAINT key_pkey PRIMARY KEY (pk);


--
-- TOC entry 3118 (class 2606 OID 16544)
-- Name: label label_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.label
    ADD CONSTRAINT label_pkey PRIMARY KEY (pk);


--
-- TOC entry 3120 (class 2606 OID 16552)
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (pk);


--
-- TOC entry 3122 (class 2606 OID 16557)
-- Name: mentionof mentionof_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.mentionof
    ADD CONSTRAINT mentionof_pkey PRIMARY KEY (pk);


--
-- TOC entry 3124 (class 2606 OID 16562)
-- Name: nameddocument nameddocument_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.nameddocument
    ADD CONSTRAINT nameddocument_pkey PRIMARY KEY (pk);


--
-- TOC entry 3130 (class 2606 OID 16575)
-- Name: namespace_map namespace_map_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.namespace_map
    ADD CONSTRAINT namespace_map_pkey PRIMARY KEY (pk, namespaces);


--
-- TOC entry 3128 (class 2606 OID 16567)
-- Name: namespace namespace_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.namespace
    ADD CONSTRAINT namespace_pkey PRIMARY KEY (pk);


--
-- TOC entry 3132 (class 2606 OID 16580)
-- Name: organization organization_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT organization_pkey PRIMARY KEY (pk);


--
-- TOC entry 3134 (class 2606 OID 16588)
-- Name: other other_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT other_pkey PRIMARY KEY (pk);


--
-- TOC entry 3136 (class 2606 OID 16593)
-- Name: pdocument pdocument_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.pdocument
    ADD CONSTRAINT pdocument_pkey PRIMARY KEY (pk);


--
-- TOC entry 3138 (class 2606 OID 16598)
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (pk);


--
-- TOC entry 3140 (class 2606 OID 16603)
-- Name: plan plan_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT plan_pkey PRIMARY KEY (pk);


--
-- TOC entry 3142 (class 2606 OID 16611)
-- Name: prefix_map prefix_map_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.prefix_map
    ADD CONSTRAINT prefix_map_pkey PRIMARY KEY (pk, prefix);


--
-- TOC entry 3144 (class 2606 OID 16616)
-- Name: prepare_data_activity prepare_data_activity_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.prepare_data_activity
    ADD CONSTRAINT prepare_data_activity_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3146 (class 2606 OID 16621)
-- Name: primarysource primarysource_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.primarysource
    ADD CONSTRAINT primarysource_pkey PRIMARY KEY (pk);


--
-- TOC entry 3150 (class 2606 OID 16634)
-- Name: prov_template prov_template_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.prov_template
    ADD CONSTRAINT prov_template_pkey PRIMARY KEY (pk);


--
-- TOC entry 3148 (class 2606 OID 16629)
-- Name: provider provider_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.provider
    ADD CONSTRAINT provider_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3152 (class 2606 OID 16642)
-- Name: qpu qpu_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qpu
    ADD CONSTRAINT qpu_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3154 (class 2606 OID 16650)
-- Name: qualifiedname qualifiedname_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qualifiedname
    ADD CONSTRAINT qualifiedname_pkey PRIMARY KEY (pk);


--
-- TOC entry 3158 (class 2606 OID 16658)
-- Name: quantum_circuit quantum_circuit_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.quantum_circuit
    ADD CONSTRAINT quantum_circuit_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3164 (class 2606 OID 16673)
-- Name: qubit_characteristics qubit_characteristics_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubit_characteristics
    ADD CONSTRAINT qubit_characteristics_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3162 (class 2606 OID 16668)
-- Name: qubit_connectivity qubit_connectivity_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubit_connectivity
    ADD CONSTRAINT qubit_connectivity_pkey PRIMARY KEY (qubit1, qubit2);


--
-- TOC entry 3160 (class 2606 OID 16663)
-- Name: qubit qubit_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubit
    ADD CONSTRAINT qubit_pkey PRIMARY KEY (database_id);


--
-- TOC entry 3166 (class 2606 OID 16678)
-- Name: qubits_gates qubits_gates_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubits_gates
    ADD CONSTRAINT qubits_gates_pkey PRIMARY KEY (qubit_id, gate_id);


--
-- TOC entry 3168 (class 2606 OID 16683)
-- Name: quotation quotation_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.quotation
    ADD CONSTRAINT quotation_pkey PRIMARY KEY (pk);


--
-- TOC entry 3170 (class 2606 OID 16688)
-- Name: revision revision_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.revision
    ADD CONSTRAINT revision_pkey PRIMARY KEY (pk);


--
-- TOC entry 3172 (class 2606 OID 16696)
-- Name: role role_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT role_pkey PRIMARY KEY (pk);


--
-- TOC entry 3174 (class 2606 OID 16701)
-- Name: softwareagent softwareagent_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.softwareagent
    ADD CONSTRAINT softwareagent_pkey PRIMARY KEY (pk);


--
-- TOC entry 3176 (class 2606 OID 16706)
-- Name: specializationof specializationof_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.specializationof
    ADD CONSTRAINT specializationof_pkey PRIMARY KEY (pk);


--
-- TOC entry 3178 (class 2606 OID 16714)
-- Name: type type_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT type_pkey PRIMARY KEY (pk);


--
-- TOC entry 3180 (class 2606 OID 16722)
-- Name: typedvalue typedvalue_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.typedvalue
    ADD CONSTRAINT typedvalue_pkey PRIMARY KEY (pk);


--
-- TOC entry 3156 (class 2606 OID 16784)
-- Name: qualifiedname uk8mbalbc1v1um9bc2tc6jiiwsa; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qualifiedname
    ADD CONSTRAINT uk8mbalbc1v1um9bc2tc6jiiwsa UNIQUE (uri);


--
-- TOC entry 3126 (class 2606 OID 16782)
-- Name: nameddocument ukcu3pv50xb9hj3kr2wjd58jrjj; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.nameddocument
    ADD CONSTRAINT ukcu3pv50xb9hj3kr2wjd58jrjj UNIQUE (name);


--
-- TOC entry 3182 (class 2606 OID 16727)
-- Name: used used_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.used
    ADD CONSTRAINT used_pkey PRIMARY KEY (pk);


--
-- TOC entry 3184 (class 2606 OID 16735)
-- Name: value value_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.value
    ADD CONSTRAINT value_pkey PRIMARY KEY (pk);


--
-- TOC entry 3186 (class 2606 OID 16740)
-- Name: wasassociatedwith wasassociatedwith_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasassociatedwith
    ADD CONSTRAINT wasassociatedwith_pkey PRIMARY KEY (pk);


--
-- TOC entry 3188 (class 2606 OID 16745)
-- Name: wasattributedto wasattributedto_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasattributedto
    ADD CONSTRAINT wasattributedto_pkey PRIMARY KEY (pk);


--
-- TOC entry 3190 (class 2606 OID 16750)
-- Name: wasderivedfrom wasderivedfrom_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasderivedfrom
    ADD CONSTRAINT wasderivedfrom_pkey PRIMARY KEY (pk);


--
-- TOC entry 3192 (class 2606 OID 16755)
-- Name: wasendedby wasendedby_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasendedby
    ADD CONSTRAINT wasendedby_pkey PRIMARY KEY (pk);


--
-- TOC entry 3194 (class 2606 OID 16760)
-- Name: wasgeneratedby wasgeneratedby_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasgeneratedby
    ADD CONSTRAINT wasgeneratedby_pkey PRIMARY KEY (pk);


--
-- TOC entry 3196 (class 2606 OID 16765)
-- Name: wasinfluencedby wasinfluencedby_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinfluencedby
    ADD CONSTRAINT wasinfluencedby_pkey PRIMARY KEY (pk);


--
-- TOC entry 3198 (class 2606 OID 16770)
-- Name: wasinformedby wasinformedby_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinformedby
    ADD CONSTRAINT wasinformedby_pkey PRIMARY KEY (pk);


--
-- TOC entry 3200 (class 2606 OID 16775)
-- Name: wasinvalidatedby wasinvalidatedby_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinvalidatedby
    ADD CONSTRAINT wasinvalidatedby_pkey PRIMARY KEY (pk);


--
-- TOC entry 3202 (class 2606 OID 16780)
-- Name: wasstartedby wasstartedby_pkey; Type: CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasstartedby
    ADD CONSTRAINT wasstartedby_pkey PRIMARY KEY (pk);


--
-- TOC entry 3362 (class 2606 OID 17582)
-- Name: wasendedby fk15psdr545ht5ucyc959k5svmf; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasendedby
    ADD CONSTRAINT fk15psdr545ht5ucyc959k5svmf FOREIGN KEY (trigger_) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3356 (class 2606 OID 17552)
-- Name: wasderivedfrom fk1a8rea2ooj041juxomgip3ecw; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasderivedfrom
    ADD CONSTRAINT fk1a8rea2ooj041juxomgip3ecw FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3278 (class 2606 OID 17162)
-- Name: other fk1b6itmt5voowrasv28utvvalh; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fk1b6itmt5voowrasv28utvvalh FOREIGN KEY (others_wasinformedby_pk) REFERENCES public.wasinformedby(pk);


--
-- TOC entry 3346 (class 2606 OID 17502)
-- Name: wasassociatedwith fk1td7kl8xjseagk65kjsbe0723; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasassociatedwith
    ADD CONSTRAINT fk1td7kl8xjseagk65kjsbe0723 FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3247 (class 2606 OID 17007)
-- Name: internationalizedstring fk2lf5xqttrig6p47x6ybi9ohei; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fk2lf5xqttrig6p47x6ybi9ohei FOREIGN KEY (label_wasinformedby_pk) REFERENCES public.wasinformedby(pk);


--
-- TOC entry 3339 (class 2606 OID 17467)
-- Name: typedvalue fk2np6yrka45nqu7xmh5m8nexam; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.typedvalue
    ADD CONSTRAINT fk2np6yrka45nqu7xmh5m8nexam FOREIGN KEY (type) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3275 (class 2606 OID 17147)
-- Name: other fk32vo8idq7bp0wv8e8jd0eqivc; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fk32vo8idq7bp0wv8e8jd0eqivc FOREIGN KEY (others_wasinvalidatedby_pk) REFERENCES public.wasinvalidatedby(pk);


--
-- TOC entry 3244 (class 2606 OID 16992)
-- Name: internationalizedstring fk3a1mglmrl4s9g12vfxhpf1e0e; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fk3a1mglmrl4s9g12vfxhpf1e0e FOREIGN KEY (label_wasinvalidatedby_pk) REFERENCES public.wasinvalidatedby(pk);


--
-- TOC entry 3361 (class 2606 OID 17577)
-- Name: wasendedby fk3aq8k2hndp17qbvpq5jcmpfsc; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasendedby
    ADD CONSTRAINT fk3aq8k2hndp17qbvpq5jcmpfsc FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3301 (class 2606 OID 17277)
-- Name: qubits_gates fk3hurdbwsto0e9x08jwgeup050; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubits_gates
    ADD CONSTRAINT fk3hurdbwsto0e9x08jwgeup050 FOREIGN KEY (gate_id) REFERENCES public.gate(database_id);


--
-- TOC entry 3209 (class 2606 OID 16817)
-- Name: alternateof fk3l6encqrqno4si7xda9tfk0ft; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.alternateof
    ADD CONSTRAINT fk3l6encqrqno4si7xda9tfk0ft FOREIGN KEY (alternate1) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3298 (class 2606 OID 17262)
-- Name: qubit_connectivity fk3mul4x3rq0b9hcd3dwq1vh4cl; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubit_connectivity
    ADD CONSTRAINT fk3mul4x3rq0b9hcd3dwq1vh4cl FOREIGN KEY (qubit2) REFERENCES public.qubit(database_id);


--
-- TOC entry 3233 (class 2606 OID 16937)
-- Name: idocument fk3xl8a7mdqnegvp82eh0kfeqmd; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.idocument
    ADD CONSTRAINT fk3xl8a7mdqnegvp82eh0kfeqmd FOREIGN KEY (bindings) REFERENCES public.document(pk);


--
-- TOC entry 3376 (class 2606 OID 17652)
-- Name: wasstartedby fk3y6qvuldw45xam53ytx8uboac; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasstartedby
    ADD CONSTRAINT fk3y6qvuldw45xam53ytx8uboac FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3221 (class 2606 OID 16877)
-- Name: document_statement_join fk441w99l04vvyjmbpes2nvytbx; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.document_statement_join
    ADD CONSTRAINT fk441w99l04vvyjmbpes2nvytbx FOREIGN KEY (document) REFERENCES public.document(pk);


--
-- TOC entry 3357 (class 2606 OID 17557)
-- Name: wasderivedfrom fk45vjhxqa9gpmjoqp3gvgds17j; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasderivedfrom
    ADD CONSTRAINT fk45vjhxqa9gpmjoqp3gvgds17j FOREIGN KEY (usage) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3367 (class 2606 OID 17607)
-- Name: wasinfluencedby fk4rev1l63ht7kd2m144vbg08gy; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinfluencedby
    ADD CONSTRAINT fk4rev1l63ht7kd2m144vbg08gy FOREIGN KEY (influencee) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3330 (class 2606 OID 17422)
-- Name: type fk4xxxk3e3x4layoxx840d14v9; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fk4xxxk3e3x4layoxx840d14v9 FOREIGN KEY (type__wasgeneratedby_pk) REFERENCES public.wasgeneratedby(pk);


--
-- TOC entry 3363 (class 2606 OID 17587)
-- Name: wasgeneratedby fk4yp4n0sx1y29ucdflw23dfb3; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasgeneratedby
    ADD CONSTRAINT fk4yp4n0sx1y29ucdflw23dfb3 FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3326 (class 2606 OID 17402)
-- Name: type fk53i3rkf1tdfs56vfa0lmecuot; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fk53i3rkf1tdfs56vfa0lmecuot FOREIGN KEY (type__actedonbehalfof_pk) REFERENCES public.actedonbehalfof(pk);


--
-- TOC entry 3364 (class 2606 OID 17592)
-- Name: wasgeneratedby fk54hkfnwjr0m1bb24jgu0prqnk; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasgeneratedby
    ADD CONSTRAINT fk54hkfnwjr0m1bb24jgu0prqnk FOREIGN KEY (entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3241 (class 2606 OID 16977)
-- Name: internationalizedstring fk55un0pmhdlgifqi0mcvhaf6ee; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fk55un0pmhdlgifqi0mcvhaf6ee FOREIGN KEY (label_used_pk) REFERENCES public.used(pk);


--
-- TOC entry 3279 (class 2606 OID 17167)
-- Name: other fk5gn4ldpd7by3t395jf3xax9ao; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fk5gn4ldpd7by3t395jf3xax9ao FOREIGN KEY (others_wasinfluencedby_pk) REFERENCES public.wasinfluencedby(pk);


--
-- TOC entry 3371 (class 2606 OID 17627)
-- Name: wasinformedby fk5jpxwd7danov314lis6jr0rot; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinformedby
    ADD CONSTRAINT fk5jpxwd7danov314lis6jr0rot FOREIGN KEY (informed) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3335 (class 2606 OID 17447)
-- Name: type fk5n9fmi9m6na3l0kkbx3m4pe6; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fk5n9fmi9m6na3l0kkbx3m4pe6 FOREIGN KEY (type__wasinformedby_pk) REFERENCES public.wasinformedby(pk);


--
-- TOC entry 3320 (class 2606 OID 17372)
-- Name: role fk5u0k9fvluymrkt332iehxcg9y; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT fk5u0k9fvluymrkt332iehxcg9y FOREIGN KEY (role__wasstartedby_pk) REFERENCES public.wasstartedby(pk);


--
-- TOC entry 3211 (class 2606 OID 16827)
-- Name: bundle fk5vx0ei20u9ddndies65iinkwe; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.bundle
    ADD CONSTRAINT fk5vx0ei20u9ddndies65iinkwe FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3316 (class 2606 OID 17352)
-- Name: role fk6bnw3fxq3o5g3n987mkot5wjf; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT fk6bnw3fxq3o5g3n987mkot5wjf FOREIGN KEY (role__used_pk) REFERENCES public.used(pk);


--
-- TOC entry 3288 (class 2606 OID 17212)
-- Name: prefix_map fk6e0fbq04unf2e6e32r6laji3p; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.prefix_map
    ADD CONSTRAINT fk6e0fbq04unf2e6e32r6laji3p FOREIGN KEY (pk) REFERENCES public.namespace(pk);


--
-- TOC entry 3348 (class 2606 OID 17512)
-- Name: wasassociatedwith fk6ggxoja5urdca0rvvpsnoqnfy; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasassociatedwith
    ADD CONSTRAINT fk6ggxoja5urdca0rvvpsnoqnfy FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3366 (class 2606 OID 17602)
-- Name: wasinfluencedby fk6gyragvavhlw8n1hj2v5tkbu4; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinfluencedby
    ADD CONSTRAINT fk6gyragvavhlw8n1hj2v5tkbu4 FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3336 (class 2606 OID 17452)
-- Name: type fk6ogljlcyp8f68etss84xlmqrm; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fk6ogljlcyp8f68etss84xlmqrm FOREIGN KEY (type__wasinfluencedby_pk) REFERENCES public.wasinfluencedby(pk);


--
-- TOC entry 3228 (class 2606 OID 16912)
-- Name: gate fk6tym2b9g5cx01hcdiefyul412; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.gate
    ADD CONSTRAINT fk6tym2b9g5cx01hcdiefyul412 FOREIGN KEY (qpu_database_id) REFERENCES public.qpu(database_id);


--
-- TOC entry 3355 (class 2606 OID 17547)
-- Name: wasderivedfrom fk78b78cll4r8qdadvhbybp9scq; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasderivedfrom
    ADD CONSTRAINT fk78b78cll4r8qdadvhbybp9scq FOREIGN KEY (generation) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3271 (class 2606 OID 17127)
-- Name: other fk7a1io074lda2ur8b1kdp2kpii; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fk7a1io074lda2ur8b1kdp2kpii FOREIGN KEY (others_wasassociatedwith_pk) REFERENCES public.wasassociatedwith(pk);


--
-- TOC entry 3350 (class 2606 OID 17522)
-- Name: wasattributedto fk7addylg0pelepyunbu0jy7v9e; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasattributedto
    ADD CONSTRAINT fk7addylg0pelepyunbu0jy7v9e FOREIGN KEY (agent) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3276 (class 2606 OID 17152)
-- Name: other fk7eaufdq7ax1gpaes7gi3uy77e; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fk7eaufdq7ax1gpaes7gi3uy77e FOREIGN KEY (others_wasendedby_pk) REFERENCES public.wasendedby(pk);


--
-- TOC entry 3296 (class 2606 OID 17252)
-- Name: qpu fk7lk1io0n49sioan40km010ar1; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qpu
    ADD CONSTRAINT fk7lk1io0n49sioan40km010ar1 FOREIGN KEY (provider_database_id) REFERENCES public.provider(database_id);


--
-- TOC entry 3270 (class 2606 OID 17122)
-- Name: other fk7mmti9jydwuxm1l3uhixf1wst; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fk7mmti9jydwuxm1l3uhixf1wst FOREIGN KEY (others_activity_pk) REFERENCES public.activity(pk);


--
-- TOC entry 3332 (class 2606 OID 17432)
-- Name: type fk7ojf19wc1yk7jh1aku85fbpbl; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fk7ojf19wc1yk7jh1aku85fbpbl FOREIGN KEY (type__wasinvalidatedby_pk) REFERENCES public.wasinvalidatedby(pk);


--
-- TOC entry 3256 (class 2606 OID 17052)
-- Name: location fk7v9xl5b6yskv2mf2oq4ew1i5a; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT fk7v9xl5b6yskv2mf2oq4ew1i5a FOREIGN KEY (invalidation) REFERENCES public.wasinvalidatedby(pk);


--
-- TOC entry 3255 (class 2606 OID 17047)
-- Name: location fk7vy1pp4hbgkijjonb9fs8e872; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT fk7vy1pp4hbgkijjonb9fs8e872 FOREIGN KEY (generation) REFERENCES public.wasgeneratedby(pk);


--
-- TOC entry 3369 (class 2606 OID 17617)
-- Name: wasinformedby fk7xrj8v951kdp0exdoqk07qww; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinformedby
    ADD CONSTRAINT fk7xrj8v951kdp0exdoqk07qww FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3300 (class 2606 OID 17272)
-- Name: qubit_characteristics fk81cil66vto5ly0w7ignl2s08v; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubit_characteristics
    ADD CONSTRAINT fk81cil66vto5ly0w7ignl2s08v FOREIGN KEY (qubit_database_id) REFERENCES public.qubit(database_id);


--
-- TOC entry 3327 (class 2606 OID 17407)
-- Name: type fk81i8vmhtu7u36tqojs3wjd7ov; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fk81i8vmhtu7u36tqojs3wjd7ov FOREIGN KEY (type__activity_pk) REFERENCES public.activity(pk);


--
-- TOC entry 3232 (class 2606 OID 16932)
-- Name: hadmember_elements fk85sgrw48uycp7swdolmteog6; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.hadmember_elements
    ADD CONSTRAINT fk85sgrw48uycp7swdolmteog6 FOREIGN KEY (collection) REFERENCES public.hadmember(pk);


--
-- TOC entry 3343 (class 2606 OID 17487)
-- Name: used fk8fbm6e4tx0fi93kbdltcg7evx; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.used
    ADD CONSTRAINT fk8fbm6e4tx0fi93kbdltcg7evx FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3299 (class 2606 OID 17267)
-- Name: qubit_connectivity fk8vr244rtf0kfedd4s1onpubpx; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubit_connectivity
    ADD CONSTRAINT fk8vr244rtf0kfedd4s1onpubpx FOREIGN KEY (qubit1) REFERENCES public.qubit(database_id);


--
-- TOC entry 3257 (class 2606 OID 17057)
-- Name: location fk99ccdu8fc8qtvch30ujoxijjs; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT fk99ccdu8fc8qtvch30ujoxijjs FOREIGN KEY (end_) REFERENCES public.wasendedby(pk);


--
-- TOC entry 3370 (class 2606 OID 17622)
-- Name: wasinformedby fk9fp1t2thuens7sb4bdui2acyf; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinformedby
    ADD CONSTRAINT fk9fp1t2thuens7sb4bdui2acyf FOREIGN KEY (informant) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3236 (class 2606 OID 16952)
-- Name: idocument fk9n02j8i6aiw3nis60lhlrxgxo; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.idocument
    ADD CONSTRAINT fk9n02j8i6aiw3nis60lhlrxgxo FOREIGN KEY (provenance) REFERENCES public.idocument(pk);


--
-- TOC entry 3219 (class 2606 OID 16867)
-- Name: dictionarymembership fk9vfnexup6sqq155vmidswue87; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.dictionarymembership
    ADD CONSTRAINT fk9vfnexup6sqq155vmidswue87 FOREIGN KEY (dictionary__dictionarymember_0) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3251 (class 2606 OID 17027)
-- Name: label fk_1c26al0yhr4uec2urudtg9ub6; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.label
    ADD CONSTRAINT fk_1c26al0yhr4uec2urudtg9ub6 FOREIGN KEY (type) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3250 (class 2606 OID 17022)
-- Name: key fk_2brvrxab1cq7aitwwjahhrid8; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.key
    ADD CONSTRAINT fk_2brvrxab1cq7aitwwjahhrid8 FOREIGN KEY (qn) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3259 (class 2606 OID 17067)
-- Name: location fk_2ec1exsn5nfg7bxudaukm7vyi; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT fk_2ec1exsn5nfg7bxudaukm7vyi FOREIGN KEY (type) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3292 (class 2606 OID 17232)
-- Name: primarysource fk_3eqr40y97hxg4clonmat9q1i4; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.primarysource
    ADD CONSTRAINT fk_3eqr40y97hxg4clonmat9q1i4 FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3260 (class 2606 OID 17072)
-- Name: location fk_3y7mhwytlw5wec3uio427btlw; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT fk_3y7mhwytlw5wec3uio427btlw FOREIGN KEY (qn) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3304 (class 2606 OID 17292)
-- Name: quotation fk_40k62wy8ihao0hojh19j9blvc; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.quotation
    ADD CONSTRAINT fk_40k62wy8ihao0hojh19j9blvc FOREIGN KEY (generated_entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3285 (class 2606 OID 17197)
-- Name: person fk_4ht90pj9rj91hj3dqhx5c40ut; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT fk_4ht90pj9rj91hj3dqhx5c40ut FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3249 (class 2606 OID 17017)
-- Name: key fk_53mp18mmls29e6srd40et0qg5; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.key
    ADD CONSTRAINT fk_53mp18mmls29e6srd40et0qg5 FOREIGN KEY (type) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3314 (class 2606 OID 17342)
-- Name: revision fk_5rlv50kvfww41eba21iet8xv9; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.revision
    ADD CONSTRAINT fk_5rlv50kvfww41eba21iet8xv9 FOREIGN KEY (used_entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3337 (class 2606 OID 17457)
-- Name: type fk_5uj1b5sieanedt31v8on15ey; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fk_5uj1b5sieanedt31v8on15ey FOREIGN KEY (type) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3306 (class 2606 OID 17302)
-- Name: quotation fk_6hpjlnwu78wn22ty3jgn5dtgu; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.quotation
    ADD CONSTRAINT fk_6hpjlnwu78wn22ty3jgn5dtgu FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3305 (class 2606 OID 17297)
-- Name: quotation fk_7y0jq320jyjewqmfw0wv3xa21; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.quotation
    ADD CONSTRAINT fk_7y0jq320jyjewqmfw0wv3xa21 FOREIGN KEY (generation) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3303 (class 2606 OID 17287)
-- Name: quotation fk_8aacoqlxvblqk7icnm99pbdw3; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.quotation
    ADD CONSTRAINT fk_8aacoqlxvblqk7icnm99pbdw3 FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3222 (class 2606 OID 16882)
-- Name: emptycollection fk_8w6ykun9o5ja8i951ol3gml2h; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.emptycollection
    ADD CONSTRAINT fk_8w6ykun9o5ja8i951ol3gml2h FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3321 (class 2606 OID 17377)
-- Name: role fk_93vn3jeavtylq20tjdx2p2kkd; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT fk_93vn3jeavtylq20tjdx2p2kkd FOREIGN KEY (type) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3267 (class 2606 OID 17107)
-- Name: organization fk_9c1nn4d3fbggryxbf3lvko4ct; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.organization
    ADD CONSTRAINT fk_9c1nn4d3fbggryxbf3lvko4ct FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3290 (class 2606 OID 17222)
-- Name: primarysource fk_9efpp3pffg67ii87jr0m8sorg; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.primarysource
    ADD CONSTRAINT fk_9efpp3pffg67ii87jr0m8sorg FOREIGN KEY (generated_entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3289 (class 2606 OID 17217)
-- Name: primarysource fk_afr07wrsvhttu80tiuxrqryto; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.primarysource
    ADD CONSTRAINT fk_afr07wrsvhttu80tiuxrqryto FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3224 (class 2606 OID 16892)
-- Name: emptydictionary fk_bx885y7y8ljov9me7lbbhcr45; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.emptydictionary
    ADD CONSTRAINT fk_bx885y7y8ljov9me7lbbhcr45 FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3338 (class 2606 OID 17462)
-- Name: type fk_d2y1bqmn14vox71i9svyvqv8g; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fk_d2y1bqmn14vox71i9svyvqv8g FOREIGN KEY (qn) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3310 (class 2606 OID 17322)
-- Name: revision fk_dc6opx57fwqfhr6q2fhuc165e; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.revision
    ADD CONSTRAINT fk_dc6opx57fwqfhr6q2fhuc165e FOREIGN KEY (generated_entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3287 (class 2606 OID 17207)
-- Name: plan fk_fkvy0l2hpqx5qhpts6c6pe3j5; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT fk_fkvy0l2hpqx5qhpts6c6pe3j5 FOREIGN KEY (value) REFERENCES public.value(pk);


--
-- TOC entry 3309 (class 2606 OID 17317)
-- Name: revision fk_g1pre1hntvt660iussccjqucd; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.revision
    ADD CONSTRAINT fk_g1pre1hntvt660iussccjqucd FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3323 (class 2606 OID 17387)
-- Name: softwareagent fk_ghaxal7i72lqdpov245cb79n9; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.softwareagent
    ADD CONSTRAINT fk_ghaxal7i72lqdpov245cb79n9 FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3307 (class 2606 OID 17307)
-- Name: quotation fk_gl292sjmdjqegofqhqbiy2724; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.quotation
    ADD CONSTRAINT fk_gl292sjmdjqegofqhqbiy2724 FOREIGN KEY (usage) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3225 (class 2606 OID 16897)
-- Name: emptydictionary fk_h4i7668ux5itb8o4au751sa9q; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.emptydictionary
    ADD CONSTRAINT fk_h4i7668ux5itb8o4au751sa9q FOREIGN KEY (value) REFERENCES public.value(pk);


--
-- TOC entry 3280 (class 2606 OID 17172)
-- Name: other fk_hi8xklbj4m2x5j51brcpr384d; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fk_hi8xklbj4m2x5j51brcpr384d FOREIGN KEY (type) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3286 (class 2606 OID 17202)
-- Name: plan fk_hsr05bdke4lpwp1a0y6y0y60p; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT fk_hsr05bdke4lpwp1a0y6y0y60p FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3344 (class 2606 OID 17492)
-- Name: value fk_iilat1rwaagowxpmqljx3g2br; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.value
    ADD CONSTRAINT fk_iilat1rwaagowxpmqljx3g2br FOREIGN KEY (type) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3281 (class 2606 OID 17177)
-- Name: other fk_ju87l2h43qnqt42nsymopf2g; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fk_ju87l2h43qnqt42nsymopf2g FOREIGN KEY (qn) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3312 (class 2606 OID 17332)
-- Name: revision fk_kcnl9g6wcjnw2b0vgag3vw6ua; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.revision
    ADD CONSTRAINT fk_kcnl9g6wcjnw2b0vgag3vw6ua FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3345 (class 2606 OID 17497)
-- Name: value fk_kqb916vj6menbjxfc58xk0gq; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.value
    ADD CONSTRAINT fk_kqb916vj6menbjxfc58xk0gq FOREIGN KEY (qn) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3294 (class 2606 OID 17242)
-- Name: primarysource fk_mkdm4tsgw2qns8r4idb14opkc; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.primarysource
    ADD CONSTRAINT fk_mkdm4tsgw2qns8r4idb14opkc FOREIGN KEY (used_entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3308 (class 2606 OID 17312)
-- Name: quotation fk_ne9bw48auvxa0hff2gvlqmp2i; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.quotation
    ADD CONSTRAINT fk_ne9bw48auvxa0hff2gvlqmp2i FOREIGN KEY (used_entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3291 (class 2606 OID 17227)
-- Name: primarysource fk_nglagrmhp7i0uj1ll7mwumlf2; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.primarysource
    ADD CONSTRAINT fk_nglagrmhp7i0uj1ll7mwumlf2 FOREIGN KEY (generation) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3322 (class 2606 OID 17382)
-- Name: role fk_omwry4ff31815wq8twlxq5nnq; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT fk_omwry4ff31815wq8twlxq5nnq FOREIGN KEY (qn) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3313 (class 2606 OID 17337)
-- Name: revision fk_p105tyjv87j45443xym2uwwm1; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.revision
    ADD CONSTRAINT fk_p105tyjv87j45443xym2uwwm1 FOREIGN KEY (usage) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3223 (class 2606 OID 16887)
-- Name: emptycollection fk_pexi16i88iqxage4al00yu2ux; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.emptycollection
    ADD CONSTRAINT fk_pexi16i88iqxage4al00yu2ux FOREIGN KEY (value) REFERENCES public.value(pk);


--
-- TOC entry 3293 (class 2606 OID 17237)
-- Name: primarysource fk_pojm3dybxggy1kd3p0qacxs2a; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.primarysource
    ADD CONSTRAINT fk_pojm3dybxggy1kd3p0qacxs2a FOREIGN KEY (usage) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3252 (class 2606 OID 17032)
-- Name: label fk_prnxd8y6dgcudrw7le62843f0; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.label
    ADD CONSTRAINT fk_prnxd8y6dgcudrw7le62843f0 FOREIGN KEY (qn) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3216 (class 2606 OID 16852)
-- Name: collection fk_r9q44g5m560nwr74y2s74byye; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.collection
    ADD CONSTRAINT fk_r9q44g5m560nwr74y2s74byye FOREIGN KEY (value) REFERENCES public.value(pk);


--
-- TOC entry 3217 (class 2606 OID 16857)
-- Name: dictionary_ fk_rq02lnh41del6eulu97fn9bos; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.dictionary_
    ADD CONSTRAINT fk_rq02lnh41del6eulu97fn9bos FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3218 (class 2606 OID 16862)
-- Name: dictionary_ fk_s1qxf19gwptqdp33w8lw9beaa; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.dictionary_
    ADD CONSTRAINT fk_s1qxf19gwptqdp33w8lw9beaa FOREIGN KEY (value) REFERENCES public.value(pk);


--
-- TOC entry 3311 (class 2606 OID 17327)
-- Name: revision fk_swq2ml7fga6f4y9cbmhl143uo; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.revision
    ADD CONSTRAINT fk_swq2ml7fga6f4y9cbmhl143uo FOREIGN KEY (generation) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3215 (class 2606 OID 16847)
-- Name: collection fk_tatos8vkiqwj0k6a8j89xkkfc; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.collection
    ADD CONSTRAINT fk_tatos8vkiqwj0k6a8j89xkkfc FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3207 (class 2606 OID 16807)
-- Name: activity fka4hugv8l1m1htu9htlhafmnup; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.activity
    ADD CONSTRAINT fka4hugv8l1m1htu9htlhafmnup FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3324 (class 2606 OID 17392)
-- Name: specializationof fkawxjobv7hfvs5qc3gypoibg3v; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.specializationof
    ADD CONSTRAINT fkawxjobv7hfvs5qc3gypoibg3v FOREIGN KEY (general) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3234 (class 2606 OID 16942)
-- Name: idocument fkbj1m5hhvrfxk8m8xp4si5sao4; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.idocument
    ADD CONSTRAINT fkbj1m5hhvrfxk8m8xp4si5sao4 FOREIGN KEY (latest) REFERENCES public.idocument(pk);


--
-- TOC entry 3283 (class 2606 OID 17187)
-- Name: pdocument fkbufkaq66i1mhnxwttm9iywhc1; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.pdocument
    ADD CONSTRAINT fkbufkaq66i1mhnxwttm9iywhc1 FOREIGN KEY (previous) REFERENCES public.pdocument(pk);


--
-- TOC entry 3341 (class 2606 OID 17477)
-- Name: used fkbvwjyc3md6y1r5qdggwtpfnnv; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.used
    ADD CONSTRAINT fkbvwjyc3md6y1r5qdggwtpfnnv FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3248 (class 2606 OID 17012)
-- Name: internationalizedstring fkbwr87klpihnwvgc1eglcpa7sb; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fkbwr87klpihnwvgc1eglcpa7sb FOREIGN KEY (label_wasinfluencedby_oj) REFERENCES public.wasinfluencedby(pk);


--
-- TOC entry 3246 (class 2606 OID 17002)
-- Name: internationalizedstring fkc0tq1kvhf6k8k5s8j9lg1h4u; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fkc0tq1kvhf6k8k5s8j9lg1h4u FOREIGN KEY (label_wasstartedby_pk) REFERENCES public.wasstartedby(pk);


--
-- TOC entry 3328 (class 2606 OID 17412)
-- Name: type fkc1o873o353l7ljq91nxv8svvh; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fkc1o873o353l7ljq91nxv8svvh FOREIGN KEY (type__wasassociatedwith_pk) REFERENCES public.wasassociatedwith(pk);


--
-- TOC entry 3205 (class 2606 OID 16797)
-- Name: actedonbehalfof fkc3o7i4197xflx1deyrxrw9964; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.actedonbehalfof
    ADD CONSTRAINT fkc3o7i4197xflx1deyrxrw9964 FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3237 (class 2606 OID 16957)
-- Name: idocument fkc8qtckqer0qaijgy4r1gkernq; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.idocument
    ADD CONSTRAINT fkc8qtckqer0qaijgy4r1gkernq FOREIGN KEY (template) REFERENCES public.document(pk);


--
-- TOC entry 3258 (class 2606 OID 17062)
-- Name: location fkcio6o2jpao8tj14ilbrdsqffp; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT fkcio6o2jpao8tj14ilbrdsqffp FOREIGN KEY (start_) REFERENCES public.wasstartedby(pk);


--
-- TOC entry 3238 (class 2606 OID 16962)
-- Name: internationalizedstring fkcl09c1rfeiaqlypven26rgex2; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fkcl09c1rfeiaqlypven26rgex2 FOREIGN KEY (label_actedonbehalfof_pk) REFERENCES public.actedonbehalfof(pk);


--
-- TOC entry 3374 (class 2606 OID 17642)
-- Name: wasinvalidatedby fkcmocvk8ei9ouyy7m9d48n6gex; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinvalidatedby
    ADD CONSTRAINT fkcmocvk8ei9ouyy7m9d48n6gex FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3375 (class 2606 OID 17647)
-- Name: wasstartedby fkcsr25u4mlixv77bj0qk9oprp2; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasstartedby
    ADD CONSTRAINT fkcsr25u4mlixv77bj0qk9oprp2 FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3229 (class 2606 OID 16917)
-- Name: gate_characteristics fkcvd50xn4iqdcs66npuowrovqa; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.gate_characteristics
    ADD CONSTRAINT fkcvd50xn4iqdcs66npuowrovqa FOREIGN KEY (gate_database_id) REFERENCES public.gate(database_id);


--
-- TOC entry 3349 (class 2606 OID 17517)
-- Name: wasassociatedwith fkcwadt2af1yy28d5og9sqosrik; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasassociatedwith
    ADD CONSTRAINT fkcwadt2af1yy28d5og9sqosrik FOREIGN KEY (plan) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3359 (class 2606 OID 17567)
-- Name: wasendedby fkd8ed0jw3gh9rrpr1e80j2ygpa; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasendedby
    ADD CONSTRAINT fkd8ed0jw3gh9rrpr1e80j2ygpa FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3243 (class 2606 OID 16987)
-- Name: internationalizedstring fkd9vqxuq3tbi3i4a1mpfdp7774; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fkd9vqxuq3tbi3i4a1mpfdp7774 FOREIGN KEY (label_wasattributedto_pk) REFERENCES public.wasattributedto(pk);


--
-- TOC entry 3239 (class 2606 OID 16967)
-- Name: internationalizedstring fkddrrakrlmpaylpbn3kxm9gifb; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fkddrrakrlmpaylpbn3kxm9gifb FOREIGN KEY (label_activity_pk) REFERENCES public.activity(pk);


--
-- TOC entry 3377 (class 2606 OID 17657)
-- Name: wasstartedby fkdpcbjsqm6be8hdkp8h5p6f1n5; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasstartedby
    ADD CONSTRAINT fkdpcbjsqm6be8hdkp8h5p6f1n5 FOREIGN KEY (starter) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3373 (class 2606 OID 17637)
-- Name: wasinvalidatedby fke8a9qp7407dyctwnqm1u8cbde; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinvalidatedby
    ADD CONSTRAINT fke8a9qp7407dyctwnqm1u8cbde FOREIGN KEY (entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3378 (class 2606 OID 17662)
-- Name: wasstartedby fkex96io3saf2dtpjnphgjig1xc; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasstartedby
    ADD CONSTRAINT fkex96io3saf2dtpjnphgjig1xc FOREIGN KEY (trigger_) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3302 (class 2606 OID 17282)
-- Name: qubits_gates fkf14ty1hkigtjx759e44h0n0g2; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubits_gates
    ADD CONSTRAINT fkf14ty1hkigtjx759e44h0n0g2 FOREIGN KEY (qubit_id) REFERENCES public.qubit(database_id);


--
-- TOC entry 3226 (class 2606 OID 16902)
-- Name: entity fkf2gf3cyuvy1qofsb99cc2van2; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.entity
    ADD CONSTRAINT fkf2gf3cyuvy1qofsb99cc2van2 FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3318 (class 2606 OID 17362)
-- Name: role fkf2mvhvwq2jsimqw235t79gki3; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT fkf2mvhvwq2jsimqw235t79gki3 FOREIGN KEY (role__wasinvalidatedby_pk) REFERENCES public.wasinvalidatedby(pk);


--
-- TOC entry 3204 (class 2606 OID 16792)
-- Name: actedonbehalfof fkf4tek3tncgja9aa8eaukmhv7r; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.actedonbehalfof
    ADD CONSTRAINT fkf4tek3tncgja9aa8eaukmhv7r FOREIGN KEY (delegate) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3242 (class 2606 OID 16982)
-- Name: internationalizedstring fkf9hjvc1atab8w48cxw4x80dt3; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fkf9hjvc1atab8w48cxw4x80dt3 FOREIGN KEY (label_wasgeneratedby_pk) REFERENCES public.wasgeneratedby(pk);


--
-- TOC entry 3284 (class 2606 OID 17192)
-- Name: pdocument fkfh9nofre2csbtkx3v7vm6x08d; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.pdocument
    ADD CONSTRAINT fkfh9nofre2csbtkx3v7vm6x08d FOREIGN KEY (provenance) REFERENCES public.idocument(pk);


--
-- TOC entry 3264 (class 2606 OID 17092)
-- Name: nameddocument fkfjfl3cf97uy6e5xcr6762sb6m; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.nameddocument
    ADD CONSTRAINT fkfjfl3cf97uy6e5xcr6762sb6m FOREIGN KEY (value) REFERENCES public.pdocument(pk);


--
-- TOC entry 3265 (class 2606 OID 17097)
-- Name: namespace fkfk70mp9bhjbwwfkhxm06dn3j0; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.namespace
    ADD CONSTRAINT fkfk70mp9bhjbwwfkhxm06dn3j0 FOREIGN KEY (parent) REFERENCES public.namespace(pk);


--
-- TOC entry 3269 (class 2606 OID 17117)
-- Name: other fkg44tp0f0ufsu42giif6c9h0ad; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fkg44tp0f0ufsu42giif6c9h0ad FOREIGN KEY (others_actedonbehalfof_pk) REFERENCES public.actedonbehalfof(pk);


--
-- TOC entry 3274 (class 2606 OID 17142)
-- Name: other fkg6q89vo440pwowix2llp78s15; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fkg6q89vo440pwowix2llp78s15 FOREIGN KEY (others_wasattributedto_pk) REFERENCES public.wasattributedto(pk);


--
-- TOC entry 3297 (class 2606 OID 17257)
-- Name: qubit fkgf0t7lf8vp69cfos2miu5lufd; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.qubit
    ADD CONSTRAINT fkgf0t7lf8vp69cfos2miu5lufd FOREIGN KEY (qpu_database_id) REFERENCES public.qpu(database_id);


--
-- TOC entry 3273 (class 2606 OID 17137)
-- Name: other fkgifh8a18fn0dtuc0jj3fyh7m6; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fkgifh8a18fn0dtuc0jj3fyh7m6 FOREIGN KEY (others_wasgeneratedby_pk) REFERENCES public.wasgeneratedby(pk);


--
-- TOC entry 3365 (class 2606 OID 17597)
-- Name: wasgeneratedby fkgj0nt5yp9p5sbw9m91rcfqt2a; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasgeneratedby
    ADD CONSTRAINT fkgj0nt5yp9p5sbw9m91rcfqt2a FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3208 (class 2606 OID 16812)
-- Name: agent fkhcu979fpy9507xtxlsunxsx6f; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.agent
    ADD CONSTRAINT fkhcu979fpy9507xtxlsunxsx6f FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3334 (class 2606 OID 17442)
-- Name: type fki36c3guaxcqhj25o5vt29bc5w; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fki36c3guaxcqhj25o5vt29bc5w FOREIGN KEY (type__wasstartedby_pk) REFERENCES public.wasstartedby(pk);


--
-- TOC entry 3351 (class 2606 OID 17527)
-- Name: wasattributedto fkiqvbj453r7d5ibubvv2grgu1u; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasattributedto
    ADD CONSTRAINT fkiqvbj453r7d5ibubvv2grgu1u FOREIGN KEY (entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3317 (class 2606 OID 17357)
-- Name: role fkixjir4plla6n39dwwc01krltg; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT fkixjir4plla6n39dwwc01krltg FOREIGN KEY (role__wasgeneratedby_pk) REFERENCES public.wasgeneratedby(pk);


--
-- TOC entry 3210 (class 2606 OID 16822)
-- Name: alternateof fkjq659c9u6bhk2w926g5o6dk85; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.alternateof
    ADD CONSTRAINT fkjq659c9u6bhk2w926g5o6dk85 FOREIGN KEY (alternate2) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3360 (class 2606 OID 17572)
-- Name: wasendedby fkjvldbvg609p29ka49w0fna22h; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasendedby
    ADD CONSTRAINT fkjvldbvg609p29ka49w0fna22h FOREIGN KEY (ender) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3347 (class 2606 OID 17507)
-- Name: wasassociatedwith fkk61q2ytdyl7hu6sc6f2ajxnhm; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasassociatedwith
    ADD CONSTRAINT fkk61q2ytdyl7hu6sc6f2ajxnhm FOREIGN KEY (agent) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3358 (class 2606 OID 17562)
-- Name: wasderivedfrom fkkd7g0xixjcwxd812hk4j7pfn7; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasderivedfrom
    ADD CONSTRAINT fkkd7g0xixjcwxd812hk4j7pfn7 FOREIGN KEY (used_entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3331 (class 2606 OID 17427)
-- Name: type fkkg36d73uxlrwl5ngjv2mnbxs3; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fkkg36d73uxlrwl5ngjv2mnbxs3 FOREIGN KEY (type__wasattributedto_pk) REFERENCES public.wasattributedto(pk);


--
-- TOC entry 3235 (class 2606 OID 16947)
-- Name: idocument fkkniy46gesj43kf9ard5to6yi0; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.idocument
    ADD CONSTRAINT fkkniy46gesj43kf9ard5to6yi0 FOREIGN KEY (previous) REFERENCES public.idocument(pk);


--
-- TOC entry 3263 (class 2606 OID 17087)
-- Name: mentionof fkkq5bltmwm8a3fv30ehpjd080d; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.mentionof
    ADD CONSTRAINT fkkq5bltmwm8a3fv30ehpjd080d FOREIGN KEY (specificentity_mentionof_pk) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3282 (class 2606 OID 17182)
-- Name: pdocument fklavkpin2ts9v81x4tc3qxg45t; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.pdocument
    ADD CONSTRAINT fklavkpin2ts9v81x4tc3qxg45t FOREIGN KEY (document) REFERENCES public.document(pk);


--
-- TOC entry 3240 (class 2606 OID 16972)
-- Name: internationalizedstring fklgfvqymlhy4sp4cm9utq3f50y; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fklgfvqymlhy4sp4cm9utq3f50y FOREIGN KEY (label_wasassociatedwith_pk) REFERENCES public.wasassociatedwith(pk);


--
-- TOC entry 3315 (class 2606 OID 17347)
-- Name: role fkltcqoqpapd0hk9aiuxpel3y4p; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT fkltcqoqpapd0hk9aiuxpel3y4p FOREIGN KEY (role__wasassociatedwith_pk) REFERENCES public.wasassociatedwith(pk);


--
-- TOC entry 3272 (class 2606 OID 17132)
-- Name: other fkm6tqe82b0u4y88rgvgn6ki140; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fkm6tqe82b0u4y88rgvgn6ki140 FOREIGN KEY (others_used_pk) REFERENCES public.used(pk);


--
-- TOC entry 3372 (class 2606 OID 17632)
-- Name: wasinvalidatedby fkmd82pqmb8iu7vyo9hfypmjka2; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinvalidatedby
    ADD CONSTRAINT fkmd82pqmb8iu7vyo9hfypmjka2 FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3213 (class 2606 OID 16837)
-- Name: bundle_statement_join fkmhxrjynrjl9ackaosawpvfnt1; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.bundle_statement_join
    ADD CONSTRAINT fkmhxrjynrjl9ackaosawpvfnt1 FOREIGN KEY (bundle) REFERENCES public.bundle(pk);


--
-- TOC entry 3266 (class 2606 OID 17102)
-- Name: namespace_map fknh1xxs1glr3rs37y3tiv08kgv; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.namespace_map
    ADD CONSTRAINT fknh1xxs1glr3rs37y3tiv08kgv FOREIGN KEY (pk) REFERENCES public.namespace(pk);


--
-- TOC entry 3354 (class 2606 OID 17542)
-- Name: wasderivedfrom fknspiah430p0fdscj9wrtkspqc; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasderivedfrom
    ADD CONSTRAINT fknspiah430p0fdscj9wrtkspqc FOREIGN KEY (generated_entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3342 (class 2606 OID 17482)
-- Name: used fknv4xtxhs0mt0dpwisbmh80uen; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.used
    ADD CONSTRAINT fknv4xtxhs0mt0dpwisbmh80uen FOREIGN KEY (entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3319 (class 2606 OID 17367)
-- Name: role fko0xmo2uflbrt9hk63xyg22qfw; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.role
    ADD CONSTRAINT fko0xmo2uflbrt9hk63xyg22qfw FOREIGN KEY (role__wasendedby_pk) REFERENCES public.wasendedby(pk);


--
-- TOC entry 3353 (class 2606 OID 17537)
-- Name: wasderivedfrom fko2xp0d58sheae2gr6qwbdf86c; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasderivedfrom
    ADD CONSTRAINT fko2xp0d58sheae2gr6qwbdf86c FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3277 (class 2606 OID 17157)
-- Name: other fko78fygmotmwkpxdiqpy0wouyk; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fko78fygmotmwkpxdiqpy0wouyk FOREIGN KEY (others_wasstartedby_pk) REFERENCES public.wasstartedby(pk);


--
-- TOC entry 3329 (class 2606 OID 17417)
-- Name: type fkoglkjynkpy2bao8pikmmvnxd2; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fkoglkjynkpy2bao8pikmmvnxd2 FOREIGN KEY (type__used_pk) REFERENCES public.used(pk);


--
-- TOC entry 3253 (class 2606 OID 17037)
-- Name: location fkondwm4g7pojb1oa3llvy8ntif; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT fkondwm4g7pojb1oa3llvy8ntif FOREIGN KEY (activity) REFERENCES public.activity(pk);


--
-- TOC entry 3254 (class 2606 OID 17042)
-- Name: location fkoy5y8wkls1axqqgf43r5riy7u; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT fkoy5y8wkls1axqqgf43r5riy7u FOREIGN KEY (usage) REFERENCES public.used(pk);


--
-- TOC entry 3214 (class 2606 OID 16842)
-- Name: calibration_matrix fkpa9im7t6ltcmyhsqvdf3aaux5; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.calibration_matrix
    ADD CONSTRAINT fkpa9im7t6ltcmyhsqvdf3aaux5 FOREIGN KEY (qpu_database_id) REFERENCES public.qpu(database_id);


--
-- TOC entry 3325 (class 2606 OID 17397)
-- Name: specializationof fkpfs0iny8t3cnmd9vo4qt97ohf; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.specializationof
    ADD CONSTRAINT fkpfs0iny8t3cnmd9vo4qt97ohf FOREIGN KEY (specific) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3352 (class 2606 OID 17532)
-- Name: wasattributedto fkppkt8cuegeyencjuynv35q8c4; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasattributedto
    ADD CONSTRAINT fkppkt8cuegeyencjuynv35q8c4 FOREIGN KEY (id) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3220 (class 2606 OID 16872)
-- Name: document fkq5p3r6d4e8qqj5pap89wg4ogn; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.document
    ADD CONSTRAINT fkq5p3r6d4e8qqj5pap89wg4ogn FOREIGN KEY (ns) REFERENCES public.namespace(pk);


--
-- TOC entry 3268 (class 2606 OID 17112)
-- Name: other fkqfjpjpjwhl2nkf8ucd7p0wfym; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.other
    ADD CONSTRAINT fkqfjpjpjwhl2nkf8ucd7p0wfym FOREIGN KEY (element) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3212 (class 2606 OID 16832)
-- Name: bundle fkqoao7sllao453oi54fmy6nxv8; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.bundle
    ADD CONSTRAINT fkqoao7sllao453oi54fmy6nxv8 FOREIGN KEY (namespace) REFERENCES public.namespace(pk);


--
-- TOC entry 3261 (class 2606 OID 17077)
-- Name: mentionof fkr0jjcvvngxi8dnxq8gahrtjno; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.mentionof
    ADD CONSTRAINT fkr0jjcvvngxi8dnxq8gahrtjno FOREIGN KEY (bundle) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3231 (class 2606 OID 16927)
-- Name: hadmember_elements fkr5fmjkaxrq7o1qap1mm8phr1f; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.hadmember_elements
    ADD CONSTRAINT fkr5fmjkaxrq7o1qap1mm8phr1f FOREIGN KEY (entity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3245 (class 2606 OID 16997)
-- Name: internationalizedstring fkrslii3kge7f8f3l4kyik7qlvm; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.internationalizedstring
    ADD CONSTRAINT fkrslii3kge7f8f3l4kyik7qlvm FOREIGN KEY (label_wasendedby_pk) REFERENCES public.wasendedby(pk);


--
-- TOC entry 3295 (class 2606 OID 17247)
-- Name: prov_template fkrymoiamqbwcm17v78ao2h7cn6; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.prov_template
    ADD CONSTRAINT fkrymoiamqbwcm17v78ao2h7cn6 FOREIGN KEY (pk) REFERENCES public.document(pk);


--
-- TOC entry 3333 (class 2606 OID 17437)
-- Name: type fks0d00f6ohgpd1skd0c0so082h; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.type
    ADD CONSTRAINT fks0d00f6ohgpd1skd0c0so082h FOREIGN KEY (type__wasendedby_pk) REFERENCES public.wasendedby(pk);


--
-- TOC entry 3203 (class 2606 OID 16787)
-- Name: actedonbehalfof fks3x4969ivoq491e8o7ybth7ku; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.actedonbehalfof
    ADD CONSTRAINT fks3x4969ivoq491e8o7ybth7ku FOREIGN KEY (activity) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3340 (class 2606 OID 17472)
-- Name: typedvalue fks3y8lm3ljf9p0mdg3ug5k1w05; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.typedvalue
    ADD CONSTRAINT fks3y8lm3ljf9p0mdg3ug5k1w05 FOREIGN KEY (qn) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3262 (class 2606 OID 17082)
-- Name: mentionof fksbi5vl1c147npj7l45i4nol2d; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.mentionof
    ADD CONSTRAINT fksbi5vl1c147npj7l45i4nol2d FOREIGN KEY (generalentity_mentionof_pk) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3227 (class 2606 OID 16907)
-- Name: entity fkscxjw7x0mg8r0xbnv5b33qrwg; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.entity
    ADD CONSTRAINT fkscxjw7x0mg8r0xbnv5b33qrwg FOREIGN KEY (value) REFERENCES public.value(pk);


--
-- TOC entry 3206 (class 2606 OID 16802)
-- Name: actedonbehalfof fksgwweuv208iswog23xc396x3p; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.actedonbehalfof
    ADD CONSTRAINT fksgwweuv208iswog23xc396x3p FOREIGN KEY (responsible) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3230 (class 2606 OID 16922)
-- Name: hadmember fksipdneoifdrpqi86vssqijyj9; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.hadmember
    ADD CONSTRAINT fksipdneoifdrpqi86vssqijyj9 FOREIGN KEY (collection) REFERENCES public.qualifiedname(pk);


--
-- TOC entry 3368 (class 2606 OID 17612)
-- Name: wasinfluencedby fksjoxgmn8vwlnlmdex0ihxj0oq; Type: FK CONSTRAINT; Schema: public; Owner: qprov
--

ALTER TABLE ONLY public.wasinfluencedby
    ADD CONSTRAINT fksjoxgmn8vwlnlmdex0ihxj0oq FOREIGN KEY (influencer) REFERENCES public.qualifiedname(pk);


-- Completed on 2021-03-24 09:31:30

--
-- PostgreSQL database dump complete
--

