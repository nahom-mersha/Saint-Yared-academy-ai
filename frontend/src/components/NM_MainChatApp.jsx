import { useState, useRef, useEffect } from "react";
import { ChatMessagesRenderer } from "./NM_ChatMessagesRenderer";
import InputBar from "./NM_input_bar";
import "../styles/NM_full_app_box_and_message_box.css"
import "../styles/NM_top_header.css"
import Export_button from "./NM_export_button.jsx"
import Reset_button from "./NM_reset_button.jsx";
// Sorry by "intent" I meant state
export function MainChatApp(){
    
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

    const manager = useState([initial_text["bot"]])
    const chatArray = manager[0]
    const chatArrayUpdater = manager[1]

    const stateData = useState("")
    const currentText = stateData[0]
    const changeText = stateData[1]

    const stateForIntent = useState("greet_and_ask_name")
    const intent = stateForIntent[0]
    const setIntent = stateForIntent[1]

    const stateForFallbackCount = useState(0)
    const fallbackCount = stateForFallbackCount[0]
    const setFallbackCount = stateForFallbackCount[1]

    async function addMessage(newMessage){
        
        const old_data = chatArray

        
        try {
            const response = await fetch("http://127.0.0.1:5000/chat", {
                method: "POST",
                headers: {
                    "Content-Type" : "application/json"
                },
                body: JSON.stringify({message: newMessage,
                    intent: intent,
                    fallbackCount: fallbackCount,
                    old_data: old_data})
                })
                
            const data = await response.json()
            
            const newIntent = data["bot"]["intent"]
            const newFallbackCount = data["bot"]["fallbackCount"]
            setIntent(newIntent)
            setFallbackCount(newFallbackCount)
                                
            function addMessages(prev){
                return([...prev, data["user"], data["bot"]])
            }
            chatArrayUpdater(addMessages)    
            changeText("")
            
           
            } catch(error) {
                console.log("Error caught is:" , error)
            }
            
    }
        const messagesBox = useRef(null)
        useEffect(()=>{
            const messagesBoxElement = messagesBox.current;
            if (messagesBoxElement){
                messagesBoxElement.scrollTop = messagesBoxElement.scrollHeight;
            }
        }, [chatArray])

    
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
                <InputBar 
                    messageAdder={addMessage} 
                    currentText={currentText}
                    changeText={changeText}>
                </InputBar>
            </div>
    );
}