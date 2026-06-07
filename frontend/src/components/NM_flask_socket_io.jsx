import { io } from "socket.io-client";

const socketio = io("http://localhost:5000/");

export default socketio