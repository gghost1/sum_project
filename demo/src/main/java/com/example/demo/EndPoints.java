package com.example.demo;

import lombok.AllArgsConstructor;
import org.springframework.boot.Banner;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;

@RestController
@RequestMapping("/")
@AllArgsConstructor
public class EndPoints {

    NewsModelReprository newsModelReprository;

    @GetMapping("/")
    public ModelAndView homePage() {
        List<NewsModel> newsModels = newsModelReprository.findAll();
        ModelAndView model = new ModelAndView("homePage");
        model.addObject("news", newsModels);
        return model;
    }

    @PostMapping("/addNews")
    public ResponseEntity addNews(@RequestBody NewsModel news) {
        newsModelReprository.save(news);
        return ResponseEntity.status(200).build();
    }
}
