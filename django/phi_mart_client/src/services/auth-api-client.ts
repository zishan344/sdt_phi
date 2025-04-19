import axios from "axios";
const localApi = "http://127.0.0.1:8000";
const liveApi: string = "https://phi-mart-zishans-projects-327b43bc.vercel.app";
const authApiClient = axios.create({
  baseURL: `${liveApi}/api/v1`,
});

export default authApiClient;

authApiClient.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem("authTokens");
    if (token) {
      config.headers.Authorization = `JWT ${JSON.parse(token)?.access}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);
