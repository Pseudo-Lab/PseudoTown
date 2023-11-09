<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { Page, Button, List, ListInput, BlockTitle } from 'konsta/svelte';
	import { apiUrl } from '../globalVars.svelte';
	import { bingoInfo } from '../bingoInfo.svelte';

	let name = '';
	let phoneNumber = '';
	let my_bingo = [0, 0, 0];
	const excludeBingoSelect = [12, 21, 23];

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
		let check_bingo = new Set(my_bingo)
		if (check_bingo.size != 3)
		{
			alert("특성을 중복으로 선택할 수 없습니다.");
			return
		}
		let bodyData = {
			phone: phoneNumber,
			bingo: my_bingo
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
	<List strongIos insetIos>
		<ListInput label="나를 표현할 수 있는 3가지 - 1" dropdown type="select" onChange={(e) => {my_bingo[0] = e.target.value}}>
			{#each bingoInfo as data, index (data)}
				{#if !(excludeBingoSelect.includes(index))} 
					<option value={index}>{data.value}</option>
				{/if}
			{/each}
		</ListInput>
		<ListInput label="나를 표현할 수 있는 3가지 - 2" dropdown type="select" onChange={(e) => {my_bingo[1] = e.target.value}}>
			{#each bingoInfo as data, index (data)}
				{#if !(excludeBingoSelect.includes(index))} 
					<option value={index}>{data.value}</option>
				{/if}
			{/each}
		</ListInput>
		<ListInput label="나를 표현할 수 있는 3가지 - 3" dropdown type="select" onChange={(e) => {my_bingo[2] = e.target.value}}>
			{#each bingoInfo as data, index (data)}
				{#if !(excludeBingoSelect.includes(index))} 
					<option value={index}>{data.value}</option>
				{/if}
			{/each}
		</ListInput>
	</List >
	<Button onClick={onClickStart}>네트워킹 시작</Button>
</Page>

<!-- 개인정보 이용동의 팝업 및 OK하면 시작 -->

<style>
	img {
		display: block;
		margin: auto;
	}
</style>
