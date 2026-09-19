package com.ptit.oj.model;

public class Teacher extends User {

    private final String department;

    public Teacher(String id, String username, String fullName, String department) {
        super(id, username, fullName);
        this.department = department;
    }

    public String getDepartment() { return department; }

    @Override
    public String getRole() { return "Giảng viên"; }

    @Override
    public String getRoleCode() { return ROLE_TEACHER; }

    // Khong ghi de canCreateProblem(): tu khi co vai tro ADMIN thi chi Admin
    // moi duoc tao de bai, giang vien chi xem duoc toan bo lich su nop.

    @Override
    public String describe() {
        return super.describe() + " - Bộ môn " + department;
    }
}
