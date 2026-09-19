package com.ptit.oj.model;

import java.util.Objects;

/**
 * Lop cha truu tuong cho moi thuc the co dinh danh trong he thong.
 * Minh hoa: ENCAPSULATION (id private final) + ABSTRACTION (describe()).
 */
public abstract class Entity {

    private final String id;

    protected Entity(String id) {
        if (id == null || id.trim().isEmpty()) {
            throw new IllegalArgumentException("id không được rỗng");
        }
        this.id = id;
    }

    public String getId() {
        return id;
    }

    /** Moi lop con tu mo ta minh -> goi qua tham chieu Entity se dinh huong dong (polymorphism). */
    public abstract String describe();

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        return id.equals(((Entity) o).id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(getClass(), id);
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + "{" + id + "}";
    }
}
