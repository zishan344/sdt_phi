import axios from "axios";
const localApi = "http://127.0.0.1:8000";
const liveApi: string = "https://phi-mart-zishans-projects-327b43bc.vercel.app";
const apiClint = axios.create({
  baseURL: `${liveApi}/api/v1`,
});

export default apiClint;
