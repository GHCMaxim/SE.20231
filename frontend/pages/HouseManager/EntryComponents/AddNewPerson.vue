<template>
	<div class="flex h-full flex-col items-center justify-center gap-3">
		<div
			class="mx-auto mb-10 mt-8 grid w-4/5 max-w-2xl grid-cols-2 grid-rows-4 gap-x-10 gap-y-7"
		>
			<div>
				<div class="mx-auto mb-2 text-start">Số căn cước</div>
				<input
					type="text"
					placeholder="Nhập số căn cước"
					class="input input-bordered w-full"
				/>
			</div>
			<div class="grid grid-cols-2 flex-row gap-3">
				<div>
					<div class="break mx-auto mb-2 text-start">Dân tộc</div>
					<input
						type="text"
						placeholder="Kinh"
						class="input input-bordered w-full"
					/>
				</div>
				<div>
					<div class="mx-auto mb-2 text-start">Tôn giáo</div>
					<input
						type="text"
						placeholder="Không"
						class="input input-bordered w-full"
					/>
				</div>
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
				<div class="mx-auto mb-2 text-start">Nghề nghiệp</div>
				<input
					type="text"
					placeholder="Kế toán"
					class="input input-bordered w-full"
				/>
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
				<div class="mx-auto mb-2 text-start">Nơi làm việc</div>
				<input
					type="text"
					placeholder="Số 1, Đại Cồ Việt, Hai Bà Trưng, Hà Nội"
					class="input input-bordered w-full"
				/>
			</div>
		</div>
		<button class="btn btn-primary w-80 self-center">Đăng ký</button>
	</div>
</template>
