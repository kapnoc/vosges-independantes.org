#![feature(proc_macro_hygiene, decl_macro)]

#[macro_use] extern crate rocket;
#[macro_use] extern crate rocket_contrib;
use rocket_contrib::templates::Template;
use rocket_contrib::serve::StaticFiles;
use rocket_contrib::databases::rusqlite;
use serde_json::json;

mod dico;
use crate::dico::static_rocket_route_info_for_dico;
use crate::dico::static_rocket_route_info_for_dico_res;

mod gallery;
use crate::gallery::static_rocket_route_info_for_gallery;

#[database("sqlite_dico")]
pub struct DicoDbConn(rusqlite::Connection);

#[get("/")]
fn index() -> Template {
    let ctx = json!({
        "title": "Accueil"
    });
    Template::render("index", &ctx)
}

fn main() {
    rocket::ignite()
        .mount("/", routes![index, dico, dico_res, gallery])
        .mount("/static", StaticFiles::from("./static"))
        .attach(Template::fairing())
        .attach(DicoDbConn::fairing())
        .launch();
}
