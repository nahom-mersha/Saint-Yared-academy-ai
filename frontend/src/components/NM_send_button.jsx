import { IoSend } from "react-icons/io5";
import "../styles/NM_send_button.css"
function SendButton(props){    // This component should be a child of the input bar  
                        // component so that the user's input can be recieved
                        //  by this SendButton component from the input bar component
    const currentText = props.currentText
    const messageAdder = props.messageAdder
    
    return (
        <div>
            <button className="send_button" onClick={() => {messageAdder(currentText)}}>
                <IoSend className="send_button_icon"> </IoSend>SEND
            </button>
        </div>
    );
}

export default SendButton;