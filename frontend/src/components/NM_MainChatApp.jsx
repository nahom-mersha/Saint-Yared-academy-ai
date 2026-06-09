import socketio from "./NM_flask_socket_io.jsx"
import { useState, useRef, useEffect } from "react";
import { ChatMessagesRenderer } from "./NM_ChatMessagesRenderer";
import InputBar from "./NM_input_bar";
import "../styles/NM_full_app_box_and_message_box.css"
import "../styles/NM_top_header.css"
import Export_button from "./NM_export_button.jsx"
import Reset_button from "./NM_reset_button.jsx";
// Sorry by "intent" I meant state
export function MainChatApp(){
    const manager = useState([])
    const chatArray = manager[0]
    const chatArrayUpdater = manager[1]

    const stateData = useState("")
    const currentText = stateData[0]
    const changeText = stateData[1]

    const stateForIntent = useState("")
    const intent = stateForIntent[0]
    const setIntent = stateForIntent[1]

    const stateForFallbackCount = useState(0)
    const fallbackCount = stateForFallbackCount[0]
    const setFallbackCount = stateForFallbackCount[1]

    useEffect(()=> {
        const bot_reply_handler = (data) =>  {
            const newIntent = data["bot"]["intent"]
            const newFallbackCount = data["bot"]["fallbackCount"]
            setIntent(newIntent)
            setFallbackCount(newFallbackCount)
                                
            function addMessages(prev){
                return([...prev, data["user"], data["bot"]])
            }
            chatArrayUpdater(addMessages)    
            changeText("")
        };
        socketio.on("bot_reply", bot_reply_handler);
        socketio.on("get_history", set_up_history)
        socketio.emit("start_chat")
        return () => {
            socketio.off("bot_reply", bot_reply_handler)
            socketio.off("get_history", set_up_history)
        };
    }, []);
    function addMessage(newMessage){
        const body = {message: newMessage,
            intent: intent,
            fallbackCount: fallbackCount,
            old_data: chatArray}
        socketio.emit("user_text", body)       
    }
    function set_up_history(initial_data){
        console.log(initial_data)
        setIntent(initial_data.state)
        chatArrayUpdater(initial_data.history)
        setFallbackCount(initial_data.fall_back)
    }
    const messagesBox = useRef(null);
    useEffect(()=>{
        const messagesBoxElement = messagesBox.current;
        if (messagesBoxElement){
            messagesBoxElement.scrollTop = messagesBoxElement.scrollHeight;
        }}, [chatArray])

    return(
        <div className="FullAppBox">
            <div className="top_header">
                <Export_button></Export_button>
                <Reset_button chatArrayUpdater={chatArrayUpdater} 
                                changeText={changeText} 
                                setFallbackCount={setFallbackCount} 
                                setIntent={setIntent}>
                </Reset_button>
            </div>

            <div className="messagesBoxCSS" ref={messagesBox}>
                <ChatMessagesRenderer messages ={chatArray}>
                </ChatMessagesRenderer>
            </div>
            
            <div>
                <InputBar 
                    messageAdder={addMessage} 
                    currentText={currentText}
                    changeText={changeText}>
                </InputBar>
            </div>
        </div>
    );
}