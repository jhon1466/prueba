<script lang="ts">
	import { slide } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';

	import ChevronUp from '../icons/ChevronUp.svelte';
	import ChevronDown from '../icons/ChevronDown.svelte';

	export let open = false;
	export let className = '';
	export let title = null;
</script>

<div class={className}>
	{#if title !== null}
<<<<<<< HEAD
		<button class="w-fit" on:click={() => (open = !open)}>
			<div class=" w-fit font-medium transition flex items-center justify-between gap-2">
=======
		<button class="w-full" on:click={() => (open = !open)}>
			<div class=" w-full font-medium transition flex items-center justify-between gap-2">
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
				<div>
					{title}
				</div>

				<div>
					{#if open}
						<ChevronUp strokeWidth="3.5" className="size-3.5 " />
					{:else}
						<ChevronDown strokeWidth="3.5" className="size-3.5 " />
					{/if}
				</div>
			</div>
		</button>
	{:else}
		<button on:click={() => (open = !open)}>
			<div
				class="flex items-center gap-2 text-gray-500 hover:text-gray-700 dark:hover:text-gray-300 transition"
			>
				<slot />
			</div>
		</button>
	{/if}

	{#if open}
		<div transition:slide={{ duration: 300, easing: quintOut, axis: 'y' }}>
			<slot name="content" />
		</div>
	{/if}
</div>
