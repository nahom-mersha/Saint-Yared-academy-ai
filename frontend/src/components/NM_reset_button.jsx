import { useEffect } from "react"
import "../styles/NM_send_button.css"
import socketio from "./NM_flask_socket_io"

function Reset_button(props){

    const chatArrayUpdater = props.chatArrayUpdater
    const changeText = props.changeText
    const setFallbackCount = props.setFallbackCount
    const setIntent = props.setIntent
    
    useEffect( () => {
        const reset_handler = (status) => {
            if (status.result == "success"){
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
            }
        }
        socketio.on("reset_success", reset_handler);
        return () =>{
            socketio.off("reset_success", reset_handler)
        }
    }, []);
    

    
    function reset_funct(){
        socketio.emit("reset")
    }

    return(
        <div>
            <button className="button" onClick={reset_funct}>Reset</button>
        </div>
    )
}

export default Reset_button;