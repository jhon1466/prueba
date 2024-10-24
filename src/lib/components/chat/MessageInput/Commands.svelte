<script>
	import { createEventDispatcher } from 'svelte';
	import { toast } from 'svelte-sonner';

	const dispatch = createEventDispatcher();

	import Prompts from './Commands/Prompts.svelte';
<<<<<<< HEAD
	import Knowledge from './Commands/Knowledge.svelte';
	import Models from './Commands/Models.svelte';

	import { removeLastWordFromString } from '$lib/utils';
	import { processWeb, processYoutubeVideo } from '$lib/apis/retrieval';
=======
	import Documents from './Commands/Documents.svelte';
	import Models from './Commands/Models.svelte';

	import { removeLastWordFromString } from '$lib/utils';
	import { uploadWebToVectorDB, uploadYoutubeTranscriptionToVectorDB } from '$lib/apis/rag';
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24

	export let prompt = '';
	export let files = [];

	let commandElement = null;

	export const selectUp = () => {
		commandElement?.selectUp();
	};

	export const selectDown = () => {
		commandElement?.selectDown();
	};

	let command = '';
	$: command = (prompt?.trim() ?? '').split(' ')?.at(-1) ?? '';

	const uploadWeb = async (url) => {
		console.log(url);

<<<<<<< HEAD
		const fileItem = {
=======
		const doc = {
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
			type: 'doc',
			name: url,
			collection_name: '',
			status: false,
			url: url,
			error: ''
		};

		try {
<<<<<<< HEAD
			files = [...files, fileItem];
			const res = await processWeb(localStorage.token, '', url);

			if (res) {
				fileItem.status = 'processed';
				fileItem.collection_name = res.collection_name;
				fileItem.file = {
					content: res.content,
					...fileItem.file
				};

=======
			files = [...files, doc];
			const res = await uploadWebToVectorDB(localStorage.token, '', url);

			if (res) {
				doc.status = 'processed';
				doc.collection_name = res.collection_name;
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
				files = files;
			}
		} catch (e) {
			// Remove the failed doc from the files array
			files = files.filter((f) => f.name !== url);
<<<<<<< HEAD
			toast.error(JSON.stringify(e));
=======
			toast.error(e);
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
		}
	};

	const uploadYoutubeTranscription = async (url) => {
		console.log(url);

<<<<<<< HEAD
		const fileItem = {
=======
		const doc = {
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
			type: 'doc',
			name: url,
			collection_name: '',
			status: false,
			url: url,
			error: ''
		};

		try {
<<<<<<< HEAD
			files = [...files, fileItem];
			const res = await processYoutubeVideo(localStorage.token, url);

			if (res) {
				fileItem.status = 'processed';
				fileItem.collection_name = res.collection_name;
				fileItem.file = {
					content: res.content,
					...fileItem.file
				};
=======
			files = [...files, doc];
			const res = await uploadYoutubeTranscriptionToVectorDB(localStorage.token, url);

			if (res) {
				doc.status = 'processed';
				doc.collection_name = res.collection_name;
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
				files = files;
			}
		} catch (e) {
			// Remove the failed doc from the files array
			files = files.filter((f) => f.name !== url);
			toast.error(e);
		}
	};
</script>

{#if ['/', '#', '@'].includes(command?.charAt(0))}
	{#if command?.charAt(0) === '/'}
		<Prompts bind:this={commandElement} bind:prompt bind:files {command} />
	{:else if command?.charAt(0) === '#'}
<<<<<<< HEAD
		<Knowledge
=======
		<Documents
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
			bind:this={commandElement}
			bind:prompt
			{command}
			on:youtube={(e) => {
				console.log(e);
				uploadYoutubeTranscription(e.detail);
			}}
			on:url={(e) => {
				console.log(e);
				uploadWeb(e.detail);
			}}
			on:select={(e) => {
				console.log(e);
				files = [
					...files,
					{
<<<<<<< HEAD
						type: e?.detail?.meta?.document ? 'file' : 'collection',
=======
						type: e?.detail?.type ?? 'file',
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
						...e.detail,
						status: 'processed'
					}
				];

				dispatch('select');
			}}
		/>
	{:else if command?.charAt(0) === '@'}
		<Models
			bind:this={commandElement}
			{command}
			on:select={(e) => {
				prompt = removeLastWordFromString(prompt, command);

				dispatch('select', {
					type: 'model',
					data: e.detail
				});
			}}
		/>
	{/if}
{/if}
