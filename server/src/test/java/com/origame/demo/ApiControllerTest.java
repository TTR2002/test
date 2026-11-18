package com.origame.demo;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.context.TestPropertySource;
import org.springframework.test.web.servlet.MockMvc;

@WebMvcTest(ApiController.class)
@TestPropertySource(properties = "app.version=abc123")
class ApiControllerTest {

    @Autowired
    private MockMvc mvc;

    @Test
    void versionRenvoieLeShaInjecte() throws Exception {
        mvc.perform(get("/api/version"))
           .andExpect(status().isOk())
           .andExpect(jsonPath("$.version").value("abc123"));
    }

    @Test
    void helloSaluePersonnalise() throws Exception {
        mvc.perform(get("/api/hello").param("name", "Rodrigue"))
           .andExpect(status().isOk())
           .andExpect(jsonPath("$.message").value("Bonjour Rodrigue !"));
    }

    @Test
    void helloParDefaut() throws Exception {
        mvc.perform(get("/api/hello"))
           .andExpect(status().isOk())
           .andExpect(jsonPath("$.message").value("Bonjour OrigaMe !"));
    }
}
