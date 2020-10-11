<nav>
    <div class='nav-flex'>
        <div class='nav-item' id='nav-home-flex'>
            <div class='nav-item'>
                <a id='home' href=".">@irlariel</a>
            </div>
        </div>
        <div class='nav-item'>
            <a href="about">about</a>
        </div>
    
        <!-- for the blog divnk, we're using rel=prefetch so that Sapper prefetches
            the blog data when we hover over the link or tap it on a touchscreen -->
        <div class='nav-item'>
            <a rel=prefetch href="blog">blog</a>
        </div>
    </div>
</nav>


<style>
    a {text-decoration: none;}

	nav {
		position: fixed;
		top: 0;
		z-index: 2;
        width: 100vw;
        height: 5vh;
		background-color: #dda7b2;
	}

    .nav-flex {
        width: 25%;
        height: 100%;
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        align-items: center;
        justify-items: stretch;
    }

	.nav-item {
        margin: none;
        padding: none;
        flex: 1;
        display: flex;
        align-content: center;
        align-items: stretch;
        justify-items: center;
	}

    #nav-home-flex {
        display: flex;
    }

    .nav-item > a {
        flex: 1;
        text-align: center;
        color: rgb(77, 29, 41);
    }

    .nav-item > #home {
        flex: 2;
        font-size: 3.5vh;
    }
</style>