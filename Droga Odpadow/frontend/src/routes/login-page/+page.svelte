<script lang="ts">
</script> 
<div class="bg-gradient-to-r from-blue-200 to-cyan-200 min-h-screen flex items-center justify-center">
  <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
    <h1 class="text-2xl font-bold mb-6 text-center">Login</h1>
    <form class="space-y-4" method="POST">
      <div>
        <label for="email"  class="block text-sm font-medium text-gray-700">Email</label>
        <input type="email" name="email" required id="email" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="" />
        </div>
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
          <input type="password" required id="password" name="password" class="mt-1 block w-full border border-gray-300 rounded-md p-2" placeholder="" />
          </div>
          <button type="submit" class="w-full bg-sky-500 text-white py-2 rounded-md hover:bg-sky-600 transition-colors">Login</button>
        </form>
        </div> 
</div>