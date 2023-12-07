<script setup lang="ts"></script>

<template>
	<div class="grid grid-cols-[0fr_1fr] xl:grid-cols-[1fr_2fr]">
		<div
			class="flex h-screen w-full items-center justify-center overflow-hidden"
		>
			<img
				src="../assets/logo.png"
				alt="logo"
				class="h-auto w-96 rounded-xl bg-primary object-cover px-5 py-3"
			/>
		</div>

		<div class="mt-12 flex flex-col gap-3 px-5">
			<div class="text-5xl font-bold">Tạo tài khoản mới</div>
			<div class="text-xl">
				Đã có tài khoản?
				<router-link to="/login"> Đăng nhập </router-link>
			</div>

			<div
				class="mx-10 mb-12 mt-8 grid grid-cols-2 grid-rows-4 gap-x-10 gap-y-7"
			>
				<div>
					<div class="mx-auto mb-2 text-start">Tài khoản</div>
					<input
						type="text"
						placeholder="Nhập tài khoản"
						class="input input-bordered w-full"
					/>
				</div>
				<div>
					<div class="mx-auto mb-2 text-start">Mật khẩu</div>
					<input
						type="password"
						placeholder="Nhập mật khẩu"
						class="input input-bordered w-full"
					/>
				</div>
				<div>
					<div class="mx-auto mb-2 text-start">Họ tên</div>
					<input
						type="text"
						placeholder="Nguyễn Văn A"
						class="input input-bordered w-full"
					/>
				</div>
				<div>
					<div class="mx-auto mb-2 text-start">Giới tính</div>
					<select class="select select-bordered w-full">
						<option disabled selected>Chọn giới tính</option>
						<option>Nam</option>
						<option>Nữ</option>
					</select>
				</div>
				<div>
					<div class="mx-auto mb-2 text-start">Chức vụ</div>
					<select class="select select-bordered w-full">
						<option disabled selected>Chọn chức vụ</option>
						<option>Kế toán</option>
						<option>Ban quản lý</option>
						<option>Ban quản trị</option>
					</select>
				</div>
				<div>
					<div class="mx-auto mb-2 text-start">Ngày sinh</div>
					<input
						type="date"
						placeholder="Nhập ngày sinh"
						class="input input-bordered w-full"
					/>
				</div>
				<div>
					<div class="mx-auto mb-2 text-start">Số điện thoại</div>
					<input
						type="text"
						placeholder="0123456789"
						class="input input-bordered w-full"
					/>
				</div>
				<div>
					<div class="mx-auto mb-2 text-start">Địa chỉ</div>
					<input
						type="text"
						placeholder="Số 1, Đại Cồ Việt, Hai Bà Trưng, Hà Nội"
						class="input input-bordered w-full"
					/>
				</div>
			</div>

			<!-- TODO: register handler -->
			<router-link to="/">
				<button class="btn btn-primary w-80">Đăng ký</button>
			</router-link>
		</div>
	</div>
	Register page
</template>
