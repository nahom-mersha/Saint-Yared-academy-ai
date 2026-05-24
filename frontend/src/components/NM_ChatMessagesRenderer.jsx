export function ChatMessagesRenderer(props){
    const messages  = props.messages
    function mappingFunct(msg, i){
        return (<p key={i}>
            {msg["role"]} --- {msg["message"]}
        </p>);
    }
    return(
        <>
            {messages.map(mappingFunct)}
        </>
    );

}