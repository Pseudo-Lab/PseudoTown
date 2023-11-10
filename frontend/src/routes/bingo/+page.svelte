<script>
	import { goto } from '$app/navigation';
	import { Page, Navbar, Block, Button, List, ListItem, ListInput } from 'konsta/svelte';
	import { onMount } from 'svelte';
	import { bingoInfo } from '../bingoInfo.svelte';
	import { apiUrl } from '../globalVars.svelte';
	let user_id = '';
	let my_attr = [];
	let board = [];
	let send_id = -1;

	//console.log(bingoInfo);

	const bingo_size = 5;
	for (let y = 0; y < bingo_size; ++y) {
		board.push(new Array());
		for (let x = 0; x < bingo_size; ++x) {
			board[y].push(y * bingo_size + x);
		}
	}
	//console.log(board);

	onMount(async () => {
		user_id = sessionStorage.getItem('user_id');
		if (!user_id) {
			console.log('');
			goto('/login');
		}
		// api로 내 빙고판 가져오기
		getBingoBoard();

		let attr = sessionStorage.getItem('my_attr');
		my_attr = attr?.split(',');
		//console.log(my_attr);
	});

	const getBingoBoard = () => {
		fetch(`${apiUrl}/bingo/${user_id}`, {
			method: 'GET',
			cache: 'no-cache'
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

	const sendBingoBoard = () => {
		if (user_id == send_id || send_id == -1) {
			alert('보내는 사람과 받는 사람이 같거나 잘못된 번호입니다.');
			return;
		}

		let bodyData = {
			user_id: user_id
		};
		fetch(`${apiUrl}/bingo/${send_id}/add`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(bodyData)
		})
			.then((response) => response.json())
			.then((data) => {
				//console.log(data);
				alert('빙고 전송에 성공하였습니다!');
			})
			.catch((error) => {
				alert('빙고 전송에 실패! 재시도가 필요합니다.');
				console.error(error);
			});
	};
</script>

<Page>
	<Navbar title="My ID {user_id}" titleFontSizeIos="text-[30px]" />
	<List strong>
		{#each my_attr as attr (attr)}
			<ListItem title={bingoInfo[attr].value} />
		{/each}
	</List>
	<Block>
		<div class="grid grid-cols-5 gap-1">
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

	<List strongIos insetIos>
		<ListInput
			label="상대 ID 입력"
			type="int"
			onInput={(e) => {
				send_id = e.target.value;
			}}
		/>
		<Button onClick={sendBingoBoard}>빙고 체크해주기</Button>
	</List>

	<Block class="flex space-x-2">
		<Button onClick={() => goto('/')}>메인</Button>
		<Button onClick={getBingoBoard}>새로고침</Button>
	</Block>
</Page>

<style>
	.cell {
		width: 16vw;
		height: 80px;
		border: 2px solid #000;
		display: flex;
		align-items: center;
		justify-content: center;
		cursor: pointer;
		text-align: center;
	}
</style>
