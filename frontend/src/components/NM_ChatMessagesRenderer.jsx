import "../styles/chatText.css"
import "../styles/timestamp.css"

export function ChatMessagesRenderer(props){
    const messages  = props.messages
    function mappingFunct(msg, i){
        return (<div key={i} className={msg["role"] === "User" ? "userText" : "botText"}>
                {msg["role"] === "Bot" ? (
                <>
                    {msg["role"]} --- {msg["message"]}
                    <div className="timestamp"> {msg["timestamp"]} </div> 
                </>   )
                : 
                (<>
                    {msg["message"]} --- {msg["role"]}
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