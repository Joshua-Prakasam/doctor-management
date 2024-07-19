import axios from "axios";
import { IDoctor, IToken, LoginInputs, SignUpInputs } from "./lib/definitions";

const BASE_URL = "http://localhost:8000";

export const signUp = (data: SignUpInputs) => {
  return axios.post<IDoctor>(`${BASE_URL}/doctors`, data);
};

export const getToken = (data: LoginInputs) => {
  return axios.post<IToken>(`${BASE_URL}/token`, data);
};
