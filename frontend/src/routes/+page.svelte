<script>
	import { goto } from '$app/navigation';
	import { Page, Navbar, Block, Button, List } from 'konsta/svelte';
	import { onMount } from 'svelte';
	let user_id = '';
	let bingo = [];

	onMount(async () => {
		user_id = sessionStorage.getItem('user_id');
		if (!user_id) {
			console.log('');
			goto('/login');
		}
		bingo = sessionStorage.getItem('bingo');
		console.log(user_id, bingo);
	});

	const onLogout = (e) => {
		sessionStorage.setItem('user_id', '');
		sessionStorage.setItem('bingo', []);
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
