package com.ptit.oj.repository;

import com.ptit.oj.model.Entity;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

/**
 * Cai dat kho du lieu bang HashMap trong bo nho (du cho bai tap lon).
 *
 * Cac phuong thuc deu synchronized: khi chay che do web, nhieu request co the
 * doc/ghi cung luc tu cac thread khac nhau cua HttpServer, ma LinkedHashMap
 * khong an toan da luong.
 */
public class InMemoryRepository<T extends Entity> implements Repository<T> {

    private final Map<String, T> storage = new LinkedHashMap<>();

    @Override
    public synchronized void save(T entity) {
        if (entity == null) throw new IllegalArgumentException("Không được lưu entity null");
        storage.put(entity.getId(), entity);
    }

    @Override
    public synchronized Optional<T> findById(String id) {
        return Optional.ofNullable(storage.get(id));
    }

    /** Tra ve ban sao de nguoi goi duyet danh sach ma khong so bi sua dong thoi. */
    @Override
    public synchronized List<T> findAll() {
        return new ArrayList<>(storage.values());
    }

    @Override
    public synchronized int count() {
        return storage.size();
    }

    @Override
    public synchronized boolean deleteById(String id) {
        return storage.remove(id) != null;
    }
}
