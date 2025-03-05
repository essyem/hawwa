<script>
    let darkMode = false;

    function toggleTheme() {
        darkMode = !darkMode;
        document.documentElement.setAttribute('data-theme', darkMode ? 'dark' : 'light');
    }
</script>

<style>
    :root {
        --background-color: white;
        --text-color: black;
    }

    [data-theme="dark"] {
        --background-color: black;
        --text-color: white;
    }

    body {
        background-color: var(--background-color);
        color: var(--text-color);
        transition: background-color 0.3s, color 0.3s;
    }
</style>

<button on:click={toggleTheme}>
    {#if darkMode} Switch to Light Mode {:else} Switch to Dark Mode {/if}
</button>
