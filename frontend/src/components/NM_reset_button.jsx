import "../styles/NM_send_button.css"

function Reset_button(props){
    const chatArrayUpdater = props.chatArrayUpdater
    async function reset_funct(){
        chatArrayUpdater([])
        
        await fetch("http://127.0.0.1:5000/reset", {
            method: "POST"
        })
    }

    return(
        <div>
            <button className="send_button" onClick={reset_funct}>Reset</button>
        </div>
    )
}

export default Reset_button;