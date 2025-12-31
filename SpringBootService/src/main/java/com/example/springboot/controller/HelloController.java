package com.example.springboot.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

/**
 * HelloController - REST Controller for greeting endpoints.
 * Provides simple REST endpoints for testing.
 */
@RestController
public class HelloController {

    /**
     * Simple hello endpoint.
     * @return A greeting message as JSON
     */
    @GetMapping("/hello")
    public Map<String, String> hello() {
        return Map.of("message", "Hello from Spring Boot");
    }

    /**
     * Root endpoint.
     * @return Welcome message
     */
    @GetMapping("/")
    public Map<String, String> welcome() {
        Map<String, String> response = new HashMap<>();
        response.put("welcome", "Spring Boot Service");
        response.put("version", "1.0.0");
        response.put("endpoints", "/hello, /info");
        return response;
    }

    /**
     * Info endpoint.
     * @return Application information
     */
    @GetMapping("/info")
    public Map<String, String> info() {
        Map<String, String> response = new HashMap<>();
        response.put("app_name", "Spring Boot Service");
        response.put("version", "1.0.0");
        response.put("java_version", System.getProperty("java.version"));
        response.put("os_name", System.getProperty("os.name"));
        return response;
    }

}
