import {useState} from "react"
import SendButton from "./NM_send_button.jsx";

export default function InputBar(){
    const stateData = useState("")
    const currentText = stateData[0]
    const changeText = stateData[1]

    function inputBarUpdater(event){
        const newText = event.target.value
        changeText(newText)
    }
    

    return(
        <div>
            <input value={currentText} onChange={inputBarUpdater}>

            </input>
            
            <SendButton text={currentText}>
                
            </SendButton>

        </div>
    );
}