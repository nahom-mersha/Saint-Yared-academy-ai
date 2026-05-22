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

    function addMessage(newMessage){
        chatArrayUpdater([...chatArray, newMessage])
        changeText("")
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