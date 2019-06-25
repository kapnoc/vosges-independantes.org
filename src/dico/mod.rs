use std::vec::Vec;

use rusqlite;
use rocket::http::RawStr;
use rocket_contrib::templates::Template;
use serde_json::json;
use percent_encoding::percent_decode;

#[get("/dico")]
pub fn dico() -> Template {
    let ctx = json!({
        "title": "Dico"
    });
    Template::render("dico", &ctx)
}

#[get("/dico?<qweredje>")]
pub fn dico_res(conn: crate::DicoDbConn, qweredje: &RawStr) -> Template {
    let fr = percent_decode(qweredje.as_str().as_bytes()).decode_utf8().unwrap().to_string();
    let safe_qweredje = fr.replace(";", "").replace("\"", "");
    let mut stmt  = conn
        .prepare("SELECT fr, vo FROM defs WHERE fr LIKE \"%?1%\" ORDER BY id ASC"
                 .to_string().replace("?1", safe_qweredje.as_str()).as_str()).unwrap();
    let defs = stmt.query_map(&[], |row| {
        let fr = row.get::<usize, String>(0);
        let vo = row.get::<usize, String>(1);
        Ok::<(String, String), rusqlite::Error>((fr, vo))
    }).unwrap().into_iter()
        .map(|x| x.unwrap().unwrap())
        .collect::<Vec<(String, String)>>();
    let ctx = json!({
        "title": "Dico",
        "fr": &fr,
        "defs": defs
    });
    Template::render("dico", &ctx)
}
