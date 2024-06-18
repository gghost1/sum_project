package com.example.demo;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface NewsModelReprository extends JpaRepository<NewsModel, Long> {
    List<NewsModel> findAll();
}
