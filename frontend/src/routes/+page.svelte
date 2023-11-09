<script>
	import { goto } from '$app/navigation';
	import { Page, Navbar, Block, Button, List } from 'konsta/svelte';
	import { onMount } from 'svelte';
	let user_id = '';

	onMount(async () => {
		user_id = sessionStorage.getItem('user_id');
		if (!user_id) goto('/login');

		let my_attr = sessionStorage.getItem('my_attr');
		if (!my_attr) goto('/attr');

		console.log(user_id, my_attr);
	});

	const onLogout = (e) => {
		sessionStorage.setItem('user_id', '');
		sessionStorage.setItem('my_attr', '');
		goto('/login');
	};
</script>

<Page>
	<Navbar title="네트워킹 ID {user_id}" titleFontSizeIos="text-[30px]" />

	<Block class="flex space-x-2">
		<!-- <Button large outline class="question-list-btn" href="/question-list">Q&A 목록</Button> -->
		<Button large outline class="bingo-btn" href="/bingo">빙고 게임</Button>
	</Block>

	<Block strong class="flex space-x-2">
		<Button onClick={onLogout}>Logout</Button>
	</Block>
</Page>

<style>
</style>
