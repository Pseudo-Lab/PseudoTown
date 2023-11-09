<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { Page, Button, List, ListInput, BlockTitle } from 'konsta/svelte';
	import { apiUrl } from '../globalVars.svelte';

	let name = '';
	let discord = '';
	let user_id = 0;

	onMount(async () => {
		user_id = sessionStorage.getItem('user_id');
		let my_attr = sessionStorage.getItem('my_attr');
		if (user_id) {
			if (!my_attr) goto('/attr');
			goto('/');
		}
	});

	const onNameChange = (e) => {
		name = e.target.value;
	};
	const onDiscordChange = (e) => {
		discord = e.target.value;
	};
	const onClickStart = (e) => {
		console.log(name, discord);
		let bodyData = {
			discord: discord
		};

		fetch(`${apiUrl}/auth/user/${name}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(bodyData)
		})
			.then((response) => response.json())
			.then((data) => {
				console.log(data.user_id, data.bingo);
				sessionStorage.setItem('user_id', data.user_id);
				goto('/attr');
			})
			.catch((error) => console.error(error));
	};
</script>

<Page>
	<List strongIos insetIos>
		<ListInput label="이름" type="text" placeholder="이름을 입력하세요" onInput={onNameChange} />
		<ListInput
			label="디스코드 사용자명 (네트워킹 추첨 이벤트 당첨시 전달용)"
			type="text"
			placeholder="디스코드 설정 - 내 계정 - 사용자명"
			onInput={onDiscordChange}
		/>
	</List>
	<Button onClick={onClickStart}>네트워킹 시작</Button>
</Page>

<style>
</style>
