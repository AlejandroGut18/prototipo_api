import type { PageServerLoad } from "./$types";

import { PUBLIC_API_URL } from "$env/static/public";
import { error } from "@sveltejs/kit";

export const load: PageServerLoad = async () => {
	const response = await fetch(`${PUBLIC_API_URL}/api/torneos`)
	const data = await response.json()
	if (response.ok){
		return {
			torneos: data
		}
	}
	error(response.status)
};