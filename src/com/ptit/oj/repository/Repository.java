package com.ptit.oj.repository;

import com.ptit.oj.model.Entity;

import java.util.List;
import java.util.Optional;

/**
 * Interface kho du lieu dung GENERIC: dung chung cho Problem, Submission, User...
 * Doi sang CSDL that chi can viet mot lop implement khac, phan con lai khong sua.
 */
public interface Repository<T extends Entity> {

    void save(T entity);

    Optional<T> findById(String id);

    List<T> findAll();

    int count();

    boolean deleteById(String id);
}
