<script lang="ts">
<<<<<<< HEAD
	import { createEventDispatcher, onDestroy, onMount } from 'svelte';
=======
	import { createEventDispatcher, onMount } from 'svelte';
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
	const dispatch = createEventDispatcher();

	let loaderElement: HTMLElement;

<<<<<<< HEAD
	let observer;
	let intervalId;

	onMount(() => {
		observer = new IntersectionObserver(
			(entries, observer) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						intervalId = setInterval(() => {
							dispatch('visible');
						}, 100);
						// dispatch('visible');
						// observer.unobserve(loaderElement); // Stop observing until content is loaded
					} else {
						clearInterval(intervalId);
=======
	onMount(() => {
		const observer = new IntersectionObserver(
			(entries, observer) => {
				entries.forEach((entry) => {
					if (entry.isIntersecting) {
						dispatch('visible');
						// observer.unobserve(loaderElement); // Stop observing until content is loaded
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
					}
				});
			},
			{
				root: null, // viewport
				rootMargin: '0px',
				threshold: 0.1 // When 10% of the loader is visible
			}
		);

		observer.observe(loaderElement);
	});
<<<<<<< HEAD

	onDestroy(() => {
		observer.disconnect();

		if (intervalId) {
			clearInterval(intervalId);
		}
	});
=======
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
</script>

<div bind:this={loaderElement}>
	<slot />
</div>
