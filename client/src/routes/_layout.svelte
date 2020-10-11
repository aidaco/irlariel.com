<script>
	import Nav from '../components/Nav.svelte';
</script>

<style>
	main {
        width: 100vw;
        height: 95vh;
        padding-top: 5%;
		background: linear-gradient(to bottom, #BA3F58, #481822);
	}
</style>

<Nav/>

<main>
	<slot></slot>
</main>