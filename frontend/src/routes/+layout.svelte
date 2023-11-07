<script>
	// import Header from './Header.svelte';
	import pseudo_lab_icon from '$lib/images/pseudo_lab_logo.jpg';
	import '../app.css';
	// import './styles.css';
	import { Page, App, Block, BlockTitle } from 'konsta/svelte';
</script>

<Block outlineIos>
	<img src={pseudo_lab_icon} width="80px" alt="PseudoLab" />
	<h1>7th PseudoCon</h1>
</Block>

<App theme="ios">
	<slot />
</App>

<style>
	img {
		display: block;
		margin: auto;
	}

	h1 {
		text-align: center;
	}
</style>
