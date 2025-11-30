<script lang="ts">


    let {data} = $props()

    let zm: number = $state(0);
    let x: number = $state(0);
    let y: number = $derived(zm + x);

    function inc(){
        zm += 1;
        console.log(zm);
    }

     function incx(){
        x += 1;
        console.log(x);
    }


</script>

<div><p>asd</p></div>
<div class="flex flex-row gap-3 justify-around p-4 bg-red-500">
{#each data.user as user}
    <p class="bold text-3xl bg-sky-800">{user.nazwa}</p>
{/each}
</div>
<button onclick={inc} class="p-5 bg-red-500">Test</button>
<p>{zm}</p>

<button onclick={incx} class="p-5 bg-red-500">Test2</button>
<p>{x}</p>

<h1>{y}</h1>