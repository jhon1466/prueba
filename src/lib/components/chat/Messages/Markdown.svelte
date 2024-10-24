<script>
	import { marked } from 'marked';
<<<<<<< HEAD
	import { replaceTokens, processResponseContent } from '$lib/utils';
	import { user } from '$lib/stores';

	import markedExtension from '$lib/utils/marked/extension';
	import markedKatexExtension from '$lib/utils/marked/katex-extension';

	import MarkdownTokens from './Markdown/MarkdownTokens.svelte';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();
=======
	import markedKatex from '$lib/utils/marked/katex-extension';
	import { replaceTokens, processResponseContent } from '$lib/utils';
	import { user } from '$lib/stores';

	import MarkdownTokens from './Markdown/MarkdownTokens.svelte';
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24

	export let id;
	export let content;
	export let model = null;
<<<<<<< HEAD
	export let save = false;
=======
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24

	let tokens = [];

	const options = {
		throwOnError: false
	};

<<<<<<< HEAD
	marked.use(markedKatexExtension(options));
	marked.use(markedExtension(options));
=======
	marked.use(markedKatex(options));
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24

	$: (async () => {
		if (content) {
			tokens = marked.lexer(
				replaceTokens(processResponseContent(content), model?.name, $user?.name)
			);
		}
	})();
</script>

{#key id}
<<<<<<< HEAD
	<MarkdownTokens
		{tokens}
		{id}
		{save}
		on:update={(e) => {
			dispatch('update', e.detail);
		}}
		on:code={(e) => {
			dispatch('code', e.detail);
		}}
	/>
=======
	<MarkdownTokens {tokens} {id} />
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
{/key}
