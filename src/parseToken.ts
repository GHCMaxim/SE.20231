type Payload = {
	sub: string;
	role: number;
	name: string;
};

/**
 * Parse token from cookie, if minRole is provided, the function will check if the user has enough role to access the page
 */
export default function parseToken(roles?: Array<number>): Payload | undefined {
	const token = document.cookie
		.split(";")
		.find((row) => row.startsWith("token"))
		?.split("=")[1];
	if (!token) {
		alert("Token không tồn tại");
		return;
	}
	try {
		const payload = JSON.parse(atob(token.split(".")[1])) as Payload;
		if (roles && roles.length !== 0 && !roles.includes(payload.role)) {
			alert("Bạn không có quyền truy cập");
			return;
		}
		return payload;
	} catch (error) {
		alert("Token không hợp lệ");
		return;
	}
}
