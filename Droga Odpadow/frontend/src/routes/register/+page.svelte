<script lang="ts">
</script> 
<div class="bg-gradient-to-r from-blue-200 to-cyan-200 min-h-screen items-center justify-center flex flex-col">
  <div class="bg-white px-8 py-6 rounded shadow-md w-full max-w-md">
    <h1 class="text-2xl font-bold mb-6 text-center">Register</h1>
    <form class="space-y-4" method="POST">
      <div>
        <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
        <input type="name" name="name" required id="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="" />
      </div>
      <div>
        <label for="surname" class="block text-sm font-medium text-gray-700">Surname</label>
        <input type="surname" required id="surname" name="surname" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="" />
      </div>
      <div>
        <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
        <input type="email" name="email" required id="email" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="" />
      </div>
      <div>
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <input type="password" required id="password" name="password" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="" />
      </div>
      <button type="submit" class="w-full bg-sky-500 text-white py-2 rounded-md hover:bg-sky-600 transition-colors">Register</button>
    </form>
  </div> 
  <div class="bg-linear-to-r from-purple-400 to-red-400 rounded-2xl mt-6">
    <a href="/" class="text-2xl">
      <div class="text-purple-900 text-center font-semibold py-2 px-4">
        Back to Home
      </div>
    </a>
  </div>
</div>
