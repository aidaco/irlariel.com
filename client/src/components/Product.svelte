<script>
    import { onMount } from 'svelte'

    export let data

    let title = ""
    let main_img = ""
    let desc = ""

    onMount(async () => {
        console.log("Data: " + data)
        title = data['title']
        main_img = data['imgs']['main']
        desc = data['desc']
	});
</script>

<div class='product-container'>
    <div class='main-img-container'>
        <img src={main_img} alt={desc}/>
    </div>

    <div class='product-title'>
        <strong>{title}</strong>
    </div>
</div>

<style>
    .product-container {
        width: 100%;
        height: 100%;
        background: linear-gradient(to bottom, black, gray);
        color: white;
    }

    .main-img-container {
        margin: auto;
    }

    .main-img-container img {
        max-height: 100%;
        max-width: 100%;
    }

    .product-title {
        margin: 1vw auto;
        width: 100%;
        height: 100%;
        text-align: right;
    }
</style>