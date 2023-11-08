<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { Page, Button, List, ListInput, BlockTitle } from 'konsta/svelte';
	import { apiUrl } from '../globalVars.svelte';

	let name = '';
	let phoneNumber = '';

	onMount(async () => {
		let user_id = sessionStorage.getItem('user_id');
		if (user_id) {
			goto('/');
		}
	});

	const onNameChange = (e) => {
		name = e.target.value;
	};
	const onPhoneNumberChange = (e) => {
		phoneNumber = e.target.value;
	};
	const onClickStart = (e) => {
		console.log(name, phoneNumber);
		let bodyData = {
			phone: phoneNumber,
			bingo: [1, 2, 3]
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
				sessionStorage.setItem('bingo', data.bingo);
				goto('/');
			})
			.catch((error) => console.error(error));
	};
</script>

<Page>
	<List strongIos insetIos>
		<ListInput label="이름" type="text" placeholder="이름을 입력하세요" onInput={onNameChange} />
		<ListInput
			label="연락처"
			type="text"
			placeholder="연락처를 입력하세요"
			onInput={onPhoneNumberChange}
		/>
		<!-- 빙고판용 성향 필요 -->
	</List>
	<Button onClick={onClickStart}>네트워킹 시작</Button>
</Page>

<!-- 개인정보 이용동의 팝업 및 OK하면 시작 -->

<style>
	img {
		display: block;
		margin: auto;
	}
</style>
