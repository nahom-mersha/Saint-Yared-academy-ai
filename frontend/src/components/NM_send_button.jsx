import { IoSend } from "react-icons/io5";
import "../styles/NM_buttons.css"
function SendButton(props){

    const currentText = props.currentText
    const messageAdder = props.messageAdder
    
    return (
        <>
            <button className="send_button_alone" onClick={() => {messageAdder(currentText)}}>
                <IoSend className="send_button_icon"> </IoSend>
            </button>
        </>
    );
} export default SendButton;