#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;
use serde::{Serialize, Deserialize};
use serde_json::{json, Value};
use reqwest;
use rocket_contrib::json::Json;
use rocket::{post};
use reqwest::Error;
use std::env;

#[derive(Serialize, Deserialize)]
struct Message {
    towns: Vec<String>,
    token: String,
}

#[post("/computeDistanceMatrix", format = "json", data = "<message>")]
fn api_distance_matrix(message: Json<Message>) -> Result<Json<Value>, Error> {
    if message.towns.len() > 1 {
        let mut duration_matrix = vec![vec![0.0; message.towns.len()]; message.towns.len()];
        let mut distance_matrix = vec![vec![0; message.towns.len()]; message.towns.len()];
        for i in 0..message.towns.len() {
            duration_matrix[i][i]=0.0;
            distance_matrix[i][i]=0;
            for j in i+1..message.towns.len() {
                if j < message.towns.len() {
                    println!("{}", message.towns[i]);
                    println!("{}", message.towns[j]);
                    let response = reqwest::blocking::get("https://maps.googleapis.com/maps/api/distancematrix/json?destinations=".to_string()+&message.towns[i]+"&origins="+&message.towns[j]+"&units=metric&key="+&message.token)?;
                    let json = response.json::<Value>()?; 
                    println!("{}", json["rows"][0]["elements"][0]["distance"]["value"].as_i64().unwrap()/1000);
                    println!("{}", json["rows"][0]["elements"][0]["duration"]["value"].as_f64().unwrap()/3600.0);
                    duration_matrix[i][j]=json["rows"][0]["elements"][0]["duration"]["value"].as_f64().unwrap()/3600.0;
                    duration_matrix[j][i]=json["rows"][0]["elements"][0]["duration"]["value"].as_f64().unwrap()/3600.0;
                    distance_matrix[i][j]=json["rows"][0]["elements"][0]["distance"]["value"].as_i64().unwrap()/1000;
                    distance_matrix[j][i]=json["rows"][0]["elements"][0]["distance"]["value"].as_i64().unwrap()/1000; 
                }
            }
        }   
        for row in &duration_matrix {
            for element in row {
                print!("{} ", element);
            }
            println!();
        }   
        let response = json!({
            "durationMatrix": duration_matrix,
            "distanceMatrix": distance_matrix,
        });
        return Ok(Json(response));   
    }
    Ok(Json(json!({})))
}

fn main() {
    let port = env::var("PORT").unwrap_or(String::from("8101")).parse().unwrap();
    let config = rocket::config::Config::build(rocket::config::Environment::Production)
        .port(port)
        .finalize()
        .unwrap();

    rocket::custom(config)
        .mount("/", routes![api_distance_matrix])
        .launch();
}