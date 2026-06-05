import "../styles/NM_send_button.css"

function Reset_button(props){
    const chatArrayUpdater = props.chatArrayUpdater
    const changeText = props.changeText
    const setFallbackCount = props.setFallbackCount
    const setIntent = props.setIntent
    async function reset_funct(){
        
        const initial_text = {}
        const time = new Date();
        const now = time.toLocaleTimeString();
        initial_text["bot"] = {
            "role" : "Bot",
            "message" : "Hi Please tell me your name!",
            "intent" : "greet_and_ask_name",
            "fallbackCount" : 0,
            "timestamp" : now
        }

        chatArrayUpdater([initial_text["bot"]])
        setFallbackCount(0)
        setIntent("greet_and_ask_name")
        changeText("")
        
        await fetch("http://127.0.0.1:5000/reset", {
            method: "POST"
        })
    }

    return(
        <div>
            <button className="button" onClick={reset_funct}>Reset</button>
        </div>
    )
}

export default Reset_button;