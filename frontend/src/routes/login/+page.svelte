<script>
	import { Page, Button, List, ListInput, BlockTitle } from 'konsta/svelte';
	import pseudo_lab_icon from '$lib/images/pseudo_lab_logo.jpg';

	let name = '';
	let phoneNumber = '';

	const onNameChange = (e) => {
		name = e.target.value;
	};
	const onPhoneNumberChange = (e) => {
		phoneNumber = e.target.value;
	};
	const onClickStart = (e) => {
		console.log(name, phoneNumber);
		let data = {
			phone: phoneNumber
		};

		fetch(`http://localhost:8000/auth/user/${name}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(data)
		})
			.then((response) => response.json())
			.then((data) => console.log(data))
			.catch((error) => console.error(error));
	};
</script>

<Page>
	<img src={pseudo_lab_icon} width="100px" alt="PseudoLab" />
	<BlockTitle>7th PseudoCon Networking</BlockTitle>

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
