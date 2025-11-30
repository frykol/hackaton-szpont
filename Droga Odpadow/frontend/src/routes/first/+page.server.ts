export async function load(){

    interface User{
        wiek: number;
        nazwa: string;
    }

    let user: Array<User> = [];

    const API_URL = import.meta.env.VITE_API_URL;
    try{
        const response = await fetch(`${API_URL}/user/1`)
        if(!response.ok){
            throw new Error("Error");
        }
        user = await response.json();
    }
    catch(e){
        console.log(e)
    }

    console.log(user);

    return {user}
}