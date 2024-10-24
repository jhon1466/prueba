<script lang="ts">
<<<<<<< HEAD
	import DOMPurify from 'dompurify';

=======
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
	import { onDestroy } from 'svelte';
	import { marked } from 'marked';

	import tippy from 'tippy.js';
	import { roundArrow } from 'tippy.js';

	export let placement = 'top';
	export let content = `I'm a tooltip!`;
	export let touch = true;
	export let className = 'flex';
	export let theme = '';
<<<<<<< HEAD
	export let allowHTML = true;
	export let tippyOptions = {};
=======
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24

	let tooltipElement;
	let tooltipInstance;

	$: if (tooltipElement && content) {
		if (tooltipInstance) {
<<<<<<< HEAD
			tooltipInstance.setContent(DOMPurify.sanitize(content));
		} else {
			tooltipInstance = tippy(tooltipElement, {
				content: DOMPurify.sanitize(content),
				placement: placement,
				allowHTML: allowHTML,
				touch: touch,
				...(theme !== '' ? { theme } : { theme: 'dark' }),
				arrow: false,
				offset: [0, 4],
				...tippyOptions
=======
			tooltipInstance.setContent(content);
		} else {
			tooltipInstance = tippy(tooltipElement, {
				content: content,
				placement: placement,
				allowHTML: true,
				touch: touch,
				...(theme !== '' ? { theme } : { theme: 'dark' }),
				arrow: false,
				offset: [0, 4]
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
			});
		}
	} else if (tooltipInstance && content === '') {
		if (tooltipInstance) {
			tooltipInstance.destroy();
		}
	}

	onDestroy(() => {
		if (tooltipInstance) {
			tooltipInstance.destroy();
		}
	});
</script>

<<<<<<< HEAD
<div bind:this={tooltipElement} aria-label={DOMPurify.sanitize(content)} class={className}>
=======
<div bind:this={tooltipElement} aria-label={content} class={className}>
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
	<slot />
</div>
