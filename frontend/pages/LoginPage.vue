<template>
	<div class="grid h-screen w-full grid-cols-[1fr_600px]">
		<img
			src="../assets/login-bg.png"
			alt="login-bg"
			class="h-full max-h-screen w-full object-cover"
		/>
		<div class="mt-16 flex flex-col items-center justify-start gap-6">
			<img
				src="../assets/logo.png"
				alt="logo"
				class="h-auto w-80 rounded-xl bg-primary px-5 py-3"
			/>

			<div class="flex w-80 flex-col items-start">
				<div class="mb-2 justify-items-start text-lg">Tài khoản</div>
				<input
					type="text"
					placeholder="Nhập tài khoản"
					class="input input-bordered w-full max-w-xs"
				/>
			</div>

			<div class="flex w-80 flex-col items-start">
				<div class="mb-2 justify-items-start text-lg">Mật khẩu</div>
				<input
					type="password"
					placeholder="Nhập mật khẩu"
					class="input input-bordered w-full max-w-xs"
				/>
			</div>

			<!-- TODO: thay route -->
			<router-link to="/" class="w-80 text-end">
				Quên mật khẩu?
			</router-link>

			<!-- TODO: login handler -->
			<router-link to="/">
				<button class="btn btn-primary w-80">Đăng nhập</button>
			</router-link>

			<div class="w-80">
				Chưa có tài khoản?
				<router-link to="/register"> Đăng ký </router-link>
			</div>
		</div>
	</div>
</template>
