function Export_button(){
    async function export_funct(){
        window.open("http://127.0.0.1:5000/export")
    }
    
    return(
        <div>
            <button onClick={export_funct}>Export</button>
        </div>
    )
}

export default Export_button;