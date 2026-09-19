package com.ptit.oj.model;

/**
 * Tai khoan quan tri. Day la vai tro DUY NHAT duoc phep tao bai tap moi:
 * canCreateProblem() cua Entity/User tra ve false, chi Admin ghi de thanh true
 * (polymorphism - noi goi khong can biet minh dang cam Student hay Admin).
 */
public class Admin extends User {

    public Admin(String id, String username, String fullName) {
        super(id, username, fullName);
    }

    @Override
    public String getRole() { return "Quản trị viên"; }

    @Override
    public String getRoleCode() { return ROLE_ADMIN; }

    /** Chi Admin duoc tao de bai - backend kiem tra lai o moi endpoint /api/admin/*. */
    @Override
    public boolean canCreateProblem() { return true; }
}
