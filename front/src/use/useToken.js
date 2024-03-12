let token = '';

export function useToken(){
  const getToken = () => token;
  const setToken = val => token = val;

  return {getToken, setToken}
}