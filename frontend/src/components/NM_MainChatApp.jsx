import { useState } from "react";
import { ChatMessagesRenderer } from "./NM_ChatMessagesRenderer";
import InputBar from "./NM_input_bar";


export function MainChatApp(){
    const manager = useState([])
    const chatArray = manager[0]
    const chatArrayUpdater = manager[1]

    const stateData = useState("")
    const currentText = stateData[0]
    const changeText = stateData[1]

    const stateForIntent = useState("start")
    const intent = stateForIntent[0]
    const setIntent = stateForIntent[1]

    const stateForFallbackCount = useState(0)
    const fallbackCount = stateForFallbackCount[0]
    const setFallbackCount = stateForFallbackCount[1]

    async function addMessage(newMessage){
        
        const old_data = chatArray

        function addusers(prev){
            return([...prev, 
                {
                    role: "user",
                    message: newMessage,
                }])
        }
        chatArrayUpdater(addusers)

        changeText("")
        
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
            const botmessage = data["reply"]
            const newIntent = data["newIntent"]
            const newFallbackCount = data["newFallbackCount"]

            setIntent(newIntent)
            setFallbackCount(newFallbackCount)


            
            function addbots(prev){
                return([...prev,
                    {
                        role: "bot",
                        message: botmessage

                    }])
            }
            
            chatArrayUpdater(addbots)
        } catch(error) {
            console.log("NAHOM" , error)
        }
    }

    return(
        <>
            <ChatMessagesRenderer messages ={chatArray}>
            </ChatMessagesRenderer>

            <InputBar 
                messageAdder={addMessage} 
                currentText={currentText}
                changeText={changeText}>
            </InputBar>
        </>
    );
}