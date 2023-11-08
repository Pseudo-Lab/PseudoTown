<script>
	import { goto } from '$app/navigation';
	import { Page, Navbar, Block, Button, List } from 'konsta/svelte';
	import { onMount } from 'svelte';
	let user_id = '';
	let my_bingo = [];
	let board = [];
	const bingo_size = 5;
	for (let y = 0; y < bingo_size; ++y) {
		board.push([]);
		for (let x = 0; x < bingo_size; ++x) {
			// board[y].push(y * bingo_size + x + 1);
			board[y].push(0);
		}
	}
	console.log(board);

	onMount(async () => {
		user_id = sessionStorage.getItem('user_id');
		if (!user_id) {
			console.log('');
			goto('/login');
		}
		my_bingo = sessionStorage.getItem('bingo');
		console.log(user_id, my_bingo);

		// api로 내 빙고판 가져오기
		board = board;
	});
</script>

<Page>
	<Navbar title="네트워킹 ID {user_id}" />

	<Block>
		<div class="grid grid-cols-5 gap-1">
			{#each board as row, rowIndex (row)}
				{#each row as cell, colIndex (cell)}
					<div class="cell" class:checked={cell} on:click={() => toggleCell(rowIndex, colIndex)}>
						{cell !== 0 ? 'O' : '내용'}
					</div>
				{/each}
			{/each}
		</div>
	</Block>

	<Button>빙고 체크해주기</Button>

	<Block class="flex space-x-2">
		<Button>메인</Button>
		<Button>새로고침</Button>
	</Block>
</Page>

<style>
	.cell {
		width: 80px;
		height: 80px;
		border: 1px solid #000;
		display: flex;
		align-items: center;
		justify-content: center;
		cursor: pointer;
	}
	.checked {
		background-color: #00ff00; /* 빙고 체크시 배경색 변경 */
	}
</style>
