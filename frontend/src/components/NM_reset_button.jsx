import { useEffect } from "react"
import "../styles/NM_buttons.css"
import socketio from "./NM_flask_socket_io"

function Reset_button(props){
    const chatArrayUpdater = props.chatArrayUpdater
    const changeText = props.changeText
    const setFallbackCount = props.setFallbackCount
    const setState = props.setState
    
    useEffect( () => {
        const reset_handler = (initial) => {
            chatArrayUpdater([initial])
                setFallbackCount(0)
                setState("greet_and_ask_name")
                changeText("")
        }
        socketio.on("reset_success", reset_handler);
        return () =>{
            socketio.off("reset_success", reset_handler)
        }}, []);
    function reset_funct(){
        socketio.emit("reset")
    }
    return(
        <>
            <button className="button" onClick={reset_funct}>Reset</button>
        </>
)} export default Reset_button;