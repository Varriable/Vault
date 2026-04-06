import { apiRequest, type User, userStore } from '$lib/index';


async function editUser(userData: Partial<User>): Promise<User> {
    const user: User = await apiRequest(`/v1/user/${userData.id}/edit`, {
        method: 'PUT',
        body: JSON.stringify(userData),
    });
    userStore.setUser(user);

    return user;
}

async function getUser(user_id : number): Promise<User> {
    const user: User = await apiRequest('/v1/user/me/',{
        body: JSON.stringify({ user_id }),
    });
    userStore.setUser(user);

    return user;
}

async function deleteUser(user_id : number): Promise<void> {    
    await apiRequest(`/v1/user/${user_id}/delete`, {
        method: 'DELETE',
    });
    userStore.clearUser();
}


export {
    editUser,
    getUser,
    deleteUser,
}