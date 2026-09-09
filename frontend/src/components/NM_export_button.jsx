import "../styles/NM_buttons.css"

function Export_button(){
    async function export_funct(){
        const backendUrl =
            import.meta.env.VITE_BACKEND_URL || "http://127.0.0.1:5000"

        window.open(`${backendUrl}/export`)
    }
    
    return(
        <>
            <button className="button" onClick={export_funct}>Export</button>
        </>
    )
}

export default Export_button;