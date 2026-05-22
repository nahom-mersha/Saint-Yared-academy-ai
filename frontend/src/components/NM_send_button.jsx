import {sendText} from "./NM_send_button_logic.js"

function SendButton(props){    // This component should be a child of the input bar  
                        // component so that the user's input can be recieved
                        //  by this SendButton component from the input bar component
    let text = props.text
    
    return (
        <div>
            <button onClick={() => {sendText(text)}}>Send</button>
        </div>
    );
}

export default SendButton;