
// import { redirect } from '@sveltejs/kit';

import { redirect, type Actions } from "@sveltejs/kit";

export const actions: Actions = {
  default: async ({ request }) => {
    const formData = await request.formData();
    const email = formData.get('email');
    const password = formData.get('password');

    // Weryfikacja danych logowania (przykład)
    if (email === 'test@example.com' && password === '123') {
      throw redirect(303, '/'); // Przekierowanie po udanym logowaniu
    }

    return { success: false, error: 'Invalid credentials' };
  }
};
