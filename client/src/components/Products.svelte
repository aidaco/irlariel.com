<script>
    import { onMount } from 'svelte';

    import Product from './Product.svelte'

    export let data;

    onMount(async () => {
        console.log("Product data: "+typeof(data))
    })
</script>

<div id='grid-frame'>
    <div id='product-grid'>
        {#each data as product}
            <div class='product-grid-unit'>
                <Product data={product}/>
            </div>
        {/each}
    </div>
</div>

<style>
    #grid-frame {
        width: 100vw;
        height: 100%;
        display: flex;
        align-content: center;
    }

    #product-grid {
        flex: 1;
        padding: 1vw 2vh;
        display: grid;
        grid-template-columns: 20% 20% 20% 20%;
        gap: ;
    }

    .product-grid-unit {
        grid-column: auto;
        grid-row: auto;
    }
</style>