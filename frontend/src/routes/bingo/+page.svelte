<script>
	import { goto } from '$app/navigation';
	import { Page, Navbar, Block, Button, List } from 'konsta/svelte';
	import { onMount } from 'svelte';
	let user_id = '';
	let bingo = [];
	let board = [
		[1, 2, 3, 4, 5],
		[6, 7, 8, 9, 10],
		[11, 12, 13, 14, 15],
		[16, 17, 18, 19, 20],
		[21, 22, 23, 24, 25]
	];

	onMount(async () => {
		user_id = sessionStorage.getItem('user_id');
		if (!user_id) {
			console.log('');
			goto('/login');
		}
		my_bingo = sessionStorage.getItem('bingo');
		console.log(user_id, my_bingo);
	});
</script>

<Page>
	<Navbar title="네트워킹 ID {user_id}" />

	<Block>
		<div class="grid grid-cols-5 gap-4">
			{#each board as row, rowIndex (row)}
				{#each row as cell, colIndex (cell)}
					<div class="cell" class:checked={cell} on:click={() => toggleCell(rowIndex, colIndex)}>
						{cell === 0 ? 'O' : 'X'}
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
		width: 70px;
		height: 70px;
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
