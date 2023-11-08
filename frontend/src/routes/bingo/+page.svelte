<script>
	import { goto } from '$app/navigation';
	import { Page, Navbar, Block, Button, List } from 'konsta/svelte';
	import { onMount } from 'svelte';
	import { bingoInfo } from '../bingoInfo.svelte';
	import { apiUrl } from '../globalVars.svelte';
	let user_id = '';
	let my_bingo = [];
	let board = [];

	console.log(bingoInfo);

	const bingo_size = 5;
	for (let y = 0; y < bingo_size; ++y) {
		board.push(new Array());
		for (let x = 0; x < bingo_size; ++x) {
			board[y].push(y * bingo_size + x);
			//board[y].push(0);
		}
	}
	console.log(board);

	const getBingoBoard = () => {
		fetch(`${apiUrl}/bingo/${user_id}`, {
			method: 'GET'
		})
			.then((response) => response.json())
			.then((data) => {
				if (data.ok == true) board = data.board;
				else {
					newBingoBoard();
				}
			})
			.catch((error) => console.error(error));
	};

	const newBingoBoard = () => {
		board[2][2] = 0;
		let bodyData = {
			board: board
		};
		fetch(`${apiUrl}/bingo/${user_id}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(bodyData)
		})
			.then((response) => response.json())
			.then((data) => {
				console.log(data);
			})
			.catch((error) => console.error(error));
	};

	onMount(async () => {
		user_id = sessionStorage.getItem('user_id');
		if (!user_id) {
			console.log('');
			goto('/login');
		}
		my_bingo = sessionStorage.getItem('bingo');
		console.log(user_id, my_bingo);

		// api로 내 빙고판 가져오기
		getBingoBoard();
	});

	const sendBingoBoard = (send_id) => {
		if (user_id == send_id) {
			console.log('보내는 사람과 받는 사람이 같습니다.');
			return;
		}

		let bodyData = {
			bingo: my_bingo
		};
		fetch(`${apiUrl}/bingo/${user_id}/add`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(bodyData)
		})
			.then((response) => response.json())
			.then((data) => {
				console.log(data);
			})
			.catch((error) => console.error(error));
	};
</script>

<Page>
	<Navbar title="네트워킹 ID {user_id}" />

	<Block>
		<div class="grid grid-cols-5 gap-4">
			{#each board as row, rowIndex (row)}
				{#each row as cell, colIndex (cell)}
					<div
						class="cell"
						style:color={cell !== rowIndex * bingo_size + colIndex ? '#ffffff' : '#000000'}
						style:background-color={cell !== rowIndex * bingo_size + colIndex
							? '#0000ff'
							: bingoInfo[rowIndex * bingo_size + colIndex].color}
					>
						{bingoInfo[rowIndex * bingo_size + colIndex].value}
					</div>
				{/each}
			{/each}
		</div>
	</Block>

	<Button>빙고 체크해주기</Button>

	<Block class="flex space-x-2">
		<Button onClick={() => goto('/')}>메인</Button>
		<Button onClick={getBingoBoard}>새로고침</Button>
	</Block>
</Page>

<style>
	.cell {
		width: 80px;
		height: 80px;
		border: 2px solid;
		display: flex;
		align-items: center;
		justify-content: center;
		cursor: pointer;
		text-align: center;
	}
</style>
