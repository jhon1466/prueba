<script lang="ts">
	import { settings } from '$lib/stores';
<<<<<<< HEAD
	import ProfileImageBase from './ProfileImageBase.svelte';

	export let className = 'size-8';
	export let src = '';
</script>

<div class={`flex-shrink-0 ${($settings?.chatDirection ?? 'LTR') === 'LTR' ? 'mr-3' : 'ml-3'}`}>
	<ProfileImageBase {src} {className} />
=======
	import { WEBUI_BASE_URL } from '$lib/constants';

	export let className = 'size-8';

	export let src = '/user.png';
</script>

<div class={`flex-shrink-0 ${($settings?.chatDirection ?? 'LTR') === 'LTR' ? 'mr-3' : 'ml-3'}`}>
	<img
		crossorigin="anonymous"
		src={src.startsWith(WEBUI_BASE_URL) ||
		src.startsWith('https://www.gravatar.com/avatar/') ||
		src.startsWith('data:') ||
		src.startsWith('/')
			? src
			: `/user.png`}
		class=" {className} object-cover rounded-full -translate-y-[1px]"
		alt="profile"
		draggable="false"
	/>
>>>>>>> 1bfc1be0c8a242212d2b3944ec9970f3c9acab24
</div>
