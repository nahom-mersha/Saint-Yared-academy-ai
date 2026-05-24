import "../styles/chatText.css"
export function ChatMessagesRenderer(props){
    const messages  = props.messages
    function mappingFunct(msg, i){
        return (<div key={i} className={msg["role"] === "User" ? "userText" : "botText"}>
            {msg["role"] === "Bot" ? `${msg["role"]} --- ${msg["message"]}` : `${msg["message"]} --- ${msg["role"]}`}
        </div>);
    }
    return(
        <>
            {messages.map(mappingFunct)}
        </>
    );

}