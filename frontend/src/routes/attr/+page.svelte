<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { Page, Button, List, ListInput, BlockTitle } from 'konsta/svelte';
	import { apiUrl } from '../globalVars.svelte';
	import { bingoInfo } from '../bingoInfo.svelte';

	let user_id = -1;
	let my_attr = [-1, -1, -1];
	const excludeBingoSelect = [12];

	onMount(async () => {
		user_id = sessionStorage.getItem('user_id');
		if (!user_id) goto('/login');
		let my_attr_item = sessionStorage.getItem('my_attr');
		if (my_attr_item) goto('/');
		my_attr = [0, 0, 0];
	});

	const getAttribute = () => {
		fetch(`${apiUrl}/bingo/attr/${user_id}`, {
			method: 'GET'
		})
			.then((response) => response.json())
			.then((data) => {
				console.log(data);
				if (data.ok == true) my_attr = data.attribute;
			})
			.catch((error) => console.error(error));
	};

	const onClickStart = (e) => {
		let check_bingo = new Set(my_attr);
		if (check_bingo.size != 3) {
			alert('특성을 중복으로 선택할 수 없습니다.');
			return;
		}

		let bodyData = {
			attribute: my_attr
		};

		fetch(`${apiUrl}/bingo/attr/${user_id}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(bodyData)
		})
			.then((response) => response.json())
			.then((data) => {
				sessionStorage.setItem('my_attr', my_attr);
				if (data.ok == true) goto('/');
			})
			.catch((error) => console.error(error));
	};
</script>

<Page>
	<BlockTitle>나를 표현할 수 있는 3가지 특성 선택 (중복X, 추후 변경은 어렵습니다.)</BlockTitle>
	<List strongIos insetIos>
		<ListInput
			label="첫 번쨰 특성"
			dropdown
			type="select"
			onChange={(e) => {
				my_attr[0] = e.target.value;
			}}
		>
			{#each bingoInfo as data, index (data)}
				{#if !excludeBingoSelect.includes(index)}
					<option class="list-input" value={index}>{data.value}</option>
				{/if}
			{/each}
		</ListInput>
		<ListInput
			label="두 번째 특성"
			dropdown
			type="select"
			onChange={(e) => {
				my_attr[1] = e.target.value;
			}}
		>
			{#each bingoInfo as data, index (data)}
				{#if !excludeBingoSelect.includes(index)}
					<option class="list-input" value={index}>{data.value}</option>
				{/if}
			{/each}
		</ListInput>
		<ListInput
			label="세 번째 특성"
			dropdown
			type="select"
			onChange={(e) => {
				my_attr[2] = e.target.value;
			}}
		>
			{#each bingoInfo as data, index (data)}
				{#if !excludeBingoSelect.includes(index)}
					<option class="list-input" value={index}>{data.value}</option>
				{/if}
			{/each}
		</ListInput>
	</List>
	<Button onClick={onClickStart}>네트워킹 시작</Button>
</Page>

<style>
	.list-input {
		background-color: white;
		color: black;
	}
</style>
