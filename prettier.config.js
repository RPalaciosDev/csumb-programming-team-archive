import config from '@hyperupcall/prettier-config'

/** @type {import('prettier').Config} */
export default {
	...config,
	overrides: [
		{
			files: './solutions/**/*.{js,ts}',
			options: {
				useTabs: false,
				tabWidth: 4,
			},
		},
	],
}
