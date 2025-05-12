<template>
    <div>
      <button @click="login">Log in</button>
      <button @click="logout">Log out</button>
      <pre>
      <code>{{ user }}</code>
    </pre>
    </div>
  </template>
  <script>
    import { useAuth0 } from '@auth0/auth0-vue';
  
    export default {
      setup() {
        const { loginWithRedirect } = useAuth0();
        const { logout } = useAuth0();
        const { user, isAuthenticated } = useAuth0();
  
        return {
          login: () => {
            loginWithRedirect();
          },
          logout: () => {
            logout({ logoutParams: { returnTo: window.location.origin } });
        },
        user,
        isAuthenticated
        };
      }
    };
  </script>