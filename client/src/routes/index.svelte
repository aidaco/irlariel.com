<script>
	import { onMount } from 'svelte';

	import Products from '../components/Products.svelte'

	function repeat_arr(n, r) {
		var arr = []
		for (var i = 0; i < r; i++) {
			arr.push(n)
		}

		return arr
	}

	const data = {
		'title': 'untitled',
		'desc': 'undescribed',
		'imgs': {
			'main': "https://picsum.photos/200/200",
		},
	}

	const products = repeat_arr(data, 5)
</script>

<svelte:head>
	<title>@irlariel</title>
</svelte:head>

<Products data={products}/>