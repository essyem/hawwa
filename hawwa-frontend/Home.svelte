<script>
    import axios from 'axios';
    let data = [];

    const fetchData = async () => {
        try {
            const response = await axios.get('http://localhost/api/endpoint');
            data = response.data;
        } catch (error) {
            console.error('Error fetching data', error);
        }
    };

    fetchData();
</script>

<style>
    /* Add your styles here */
</style>

<main>
    <h1>Welcome to HAWWA</h1>
    <ul>
        {#each data as item}
            <li>{item.name}</li>
        {/each}
    </ul>
</main>
