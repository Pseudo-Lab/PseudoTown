/** @type {import('tailwindcss').Config} */
export default {
	content: [],
	theme: {
		extend: {}
	},
	plugins: []
};

// eslint-disable-next-line @typescript-eslint/no-var-requires
const konstaConfig = require('konsta/config');

// wrap config with konstaConfig config
module.exports = konstaConfig({
	content: ['./src/**/*.{html,js,svelte,ts}'],
	darkMode: 'media', // or 'class'
	theme: {
		extend: {}
	},
	variants: {
		extend: {}
	},
	plugins: []
});
