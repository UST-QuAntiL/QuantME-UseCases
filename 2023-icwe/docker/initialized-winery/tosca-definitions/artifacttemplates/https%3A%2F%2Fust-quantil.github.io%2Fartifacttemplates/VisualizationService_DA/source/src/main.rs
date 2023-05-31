#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use]
extern crate rocket;

use serde::{Serialize, Deserialize};
use reqwest::blocking::get;
use rocket_contrib::json::Json;
use rocket::{post, Response};
use reqwest::Error;
use std::env;

#[derive(Serialize, Deserialize)]
struct Message {
    routes: Vec<Vec<String>>,
    token: String,
}

#[post("/drawMap", format = "json", data = "<message>")]
fn api_draw_map(message: Json<Message>) -> Result<Response<'static>, Error> {
    let colormap = ["17befc", "fc0303", "d803fc", "fcbd03", "03fce8", "64ff33"];
    let mut overall_route_string = String::new();

    for i in 0..message.routes.len() {
        let mut current_route_string = String::new();
        for route in &message.routes[i] {
            current_route_string = current_route_string + "|" + route;
        }
        overall_route_string = overall_route_string + "&path=color:0x" + &colormap[i%colormap.len()] + "|weight:5"+ &current_route_string;
    }

    let url = format!("https://maps.googleapis.com/maps/api/staticmap?size=640x640{}&key={}", &overall_route_string, message.token);
    let response = get(&url)?;

    let image_data: Vec<u8> = response.bytes()?.to_vec();
    let content_type = "image/png";

    Ok(Response::build()
        .header(rocket::http::ContentType(content_type.parse().unwrap()))
        .raw_header("content-disposition", "inline")
        .sized_body(std::io::Cursor::new(image_data))
        .finalize())
}

fn main() {
    let port = env::var("PORT").unwrap_or(String::from("8102")).parse().unwrap();
    let config = rocket::config::Config::build(rocket::config::Environment::Production)
        .port(port)
        .finalize()
        .unwrap();

    rocket::custom(config)
        .mount("/", routes![api_draw_map])
        .launch();
}