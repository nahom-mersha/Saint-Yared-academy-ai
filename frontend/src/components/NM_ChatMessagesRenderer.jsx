import "../styles/chatText.css"
import "../styles/timestamp.css"
import SendButton from "./NM_send_button.jsx";

export function ChatMessagesRenderer(props){
    const messages  = props.messages
    function mappingFunct(msg, i){
        return (<div key={i} className={msg["role"] === "User" ? "userText" : "botText"}>
                {msg["role"] === "Bot" ? (
                <>
                    🤖 Bot --- {msg["message"]}
                    <div className="timestamp"> {msg["timestamp"]} </div> 
                </>   )
                : 
                (<>
                    {msg["message"]} --- 🧑 You
                    <div className="timestamp"> {msg["timestamp"]} </div> 
                </>)}
            </div>
            );
    }
    return(
        <>
            {messages.map(mappingFunct)}
        </>
    );

}