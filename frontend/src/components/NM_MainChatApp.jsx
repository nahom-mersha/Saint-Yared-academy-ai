import { useState } from "react";
import { ChatMessagesRenderer } from "./NM_ChatMessagesRenderer";
import InputBar from "./NM_input_bar";


export function MainChatApp(){
    const manager = useState(["Hi"])
    const chatArray = manager[0]
    const chatArrayUpdater = manager[1]

    const stateData = useState("")
    const currentText = stateData[0]
    const changeText = stateData[1]

    async function addMessage(newMessage){
        chatArrayUpdater([...chatArray, newMessage])
        changeText("")

        const response = await fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type" : "application/json"
            },
            body: JSON.stringify({messege: newMessage})
        })

        const data = await response.json()
        const botmessage = data["reply"]
        chatArrayUpdater([...chatArray, botmessage])


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