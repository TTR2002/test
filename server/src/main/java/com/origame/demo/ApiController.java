package com.origame.demo;

import java.util.Collections;
import java.util.Map;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class ApiController {

    /** SHA du commit, injecté par la CI au build de l'image (variable APP_VERSION). */
    @Value("${app.version:dev}")
    private String version;

    /** Permet aux smoke tests de vérifier que c'est bien le bon commit qui est en ligne. */
    @GetMapping("/version")
    public Map<String, String> version() {
        return Collections.singletonMap("version", version);
    }

    @GetMapping("/hello")
    public Map<String, String> hello(@RequestParam(defaultValue = "OrigaMe") String name) {
        return Collections.singletonMap("message", "Bonjour " + name + " !");
    }
}
