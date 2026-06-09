import "../styles/NM_buttons.css"

function Export_button(){
    async function export_funct(){
        window.open("http://127.0.0.1:5000/export")
    }
    
    return(
        <>
            <button className="button" onClick={export_funct}>Export</button>
        </>
    )
}

export default Export_button;