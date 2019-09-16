use rocket::http::RawStr;
use rocket_contrib::templates::Template;
use serde_json::json;

#[get("/gal'rie")]
pub fn gallery() -> Template {
    let ctx = json!({
        "title": "Gallerie"
    });
    Template::render("index", &ctx)
}
