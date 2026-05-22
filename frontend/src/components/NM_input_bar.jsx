import {useState} from "react"
import SendButton from "./NM_send_button.jsx";
import "../styles/NM_input_bar_and_container.css"

export default function InputBar(props){
    // const stateData = useState("")
    // const currentText = stateData[0]
    // const changeText = stateData[1]
    const messageAdder = props.messageAdder 
    const currentText = props.currentText
    const changeText = props.changeText
    

    function inputBarUpdater(event){
        const newText = event.target.value
        changeText(newText)
    }
    

    return(
        <div className="input_bar_and_send">
            <input className="input_bar" value={currentText} onChange={inputBarUpdater}>

            </input>
            <SendButton currentText={currentText} messageAdder={messageAdder}>
                
            </SendButton>
            

        </div>
    );
}