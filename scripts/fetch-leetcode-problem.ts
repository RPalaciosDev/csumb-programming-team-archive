#!/usr/bin/env -S node --disable-warning=ExperimentalWarning
import path from 'node:path'
import fs from 'node:fs/promises'
import { parseArgs } from 'node:util'
import TurndownService from 'turndown'

const turndownService = new TurndownService()

type LeetCodeQuestion = {
	acRate: number
	content: string
	difficulty: 'Easy' | 'Medium' | 'Hard'
	freqBar: unknown
	frontendQuestionId: string
	isFavor: boolean
	likes: number
	isPaidOnly: boolean
	questionId: string,
	status: unknown
	title: string
	titleSlug: string
	topicTags: { name: string; id: string; slug: string }[]
	hasSolution: number
	hasVideoSolution: number
}

{
	const { values } = parseArgs({
		options: {
			slug: {
				type: 'string'
			}
		}
	})
	const problemSlug = values.slug

	if (!problemSlug) {
		console.error(`USAGE: fetch-leetcode-problem --slug=two-sum`)
		process.exit(1)
	}

	const problem = await fetchLeetCodeProblem(problemSlug)
	const question: LeetCodeQuestion = problem.question
	const markdownContent = htmlToMarkdown(question.content)

	const file = `./solutions/leetcode/${question.frontendQuestionId}-${question.titleSlug}/README.md`
	const content = `# ${question.frontendQuestionId}. ${question.title}

**Difficulty:** ${question.difficulty}

## Problem Description

${markdownContent}`

	await fs.mkdir(path.dirname(file), { recursive: true })
	await fs.writeFile(file, content)
	console.info('Done!')
}

function htmlToMarkdown(text: string) {
	text = turndownService.turndown(text)
	text = text.replaceAll('**Output:**', '\n**Output:**')
	text = text.replaceAll('**Explanation:** ', '\n**Explanation:**\n')
	text = text.replaceAll(/\*\*Example (\d+):\*\*/g, '## Example $1')
	text = text.replaceAll('**Constraints:**', '## Constraints')
	text = text.replaceAll(/^\*   /mg, '- ')

	return text
}

async function fetchLeetCodeProblem(problemSlug: string) {
	const res = await fetch('https://leetcode.com/graphql', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			'User-Agent':
				'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
			Referer: `https://leetcode.com/problems/${problemSlug}/`, // Supposedly important for some APIs
		},
		body: JSON.stringify({
			query: `
query questionContent($titleSlug: String!) {
	question(titleSlug: $titleSlug) {
		acRate
		content
		difficulty
		freqBar
		frontendQuestionId: questionFrontendId
		hasSolution
		hasVideoSolution
		isFavor
		likes
		isPaidOnly
		questionId
		status
		title
		titleSlug
		topicTags {
			name
			id
			slug
		}
	}
}
`,
			variables: {
				titleSlug: problemSlug,
			},
			operationName: 'questionContent',
		}),
	})
	if (!res.ok) {
		throw new Error(`Failed to fetch GraphQL data: ${res.status} ${res.statusText}`)
	}

	const result = await res.json()
	if (result.errors) {
		console.error('GraphQL Errors:', result.errors)
		throw new Error()
	}

	return result.data
}
